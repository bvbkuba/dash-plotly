# Tworzymy graf z danymi i Sliderem(przesuwak)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('../databasesss/graph_callback_data.csv')

app = dash.Dash(__name__)


app.layout = html.Div([
    dcc.Graph(id = 'graph1'),
    dcc.Slider(
        id = 'Slider1',
        min = df.year.min(),
        max = df.year.max(),
        value = df.year.min(),#wartość domyślna
        marks={str(year): str(year) for year in df.year.unique()},  #tworzymy unikalną skale z lat - wartości w marks to słowniki
        step = None

    )
])
@app.callback(
    Output('graph1', 'figure'),
    [Input('Slider1','value')]
)
def update_graph(selected_year):
    dff = df.query(f"year == {selected_year}")
    traces = []
    for cont in df.continent.unique():
        dff_cont = dff[dff.continent == cont]
        traces.append(
            go.Scatter(
                x = dff_cont.gdpPercap,
                y = dff_cont.lifeExp,
                mode='markers',
                name = cont,
                opacity=0.6,  #przeźroczystość punktów
                marker = {
                    'size': 15,
                    'line': {'width': 1.5, 'color': 'white'}  #charakterystyka lini
                }
            )
        )

    return {'data': traces, 'layout': go.Layout(
        title_text = 'Wykres', xaxis = {'type': 'log', 'title': 'PKB per capita'},
    yaxis={'title': 'Oczekiwana wartość zycia'}  #oś y
    ,hovermode='closest'  #dobiera najbliższa wartosc dla wskaznika pkb per capita
    )}




if __name__ == '__main__':
    app.run_server(debug=True, port=8050, dev_tools_hot_reload=True)
