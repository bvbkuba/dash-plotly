# Tworzymy graf z danymi i Sliderem(przesuwak)

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd

df = pd.read_csv('../databasesss/graph_callback_data.csv')

app = dash.Dash(__name__)

# list_of_column = [col for col in df]
# list_of_year = [year for year in df.year.unique()]
# print(list_of_column,list_of_year)

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
    dff = df.query(f"year == {selected_year}") #df query służy do zapytania w prostej formie loggicznej <>=/
    traces = []
    for cont in df.continent.unique():   #lista kontynentów ['Asia' 'Europe' 'Africa' 'Americas' 'Oceania']
        dff_cont = dff[dff.continent == cont]  # gdy kolumna cont jest równa kontynentowi w df
        traces.append(
            go.Scatter(   #ślad dla danego obiektu
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
    return {'data': traces, 'layout': go.Layout(   #traces to lista obiektów
        title_text = 'Wykres', xaxis = {'type': 'log', 'title': 'PKB per capita'},
    yaxis={'title': 'Oczekiwana wartość zycia'}  #oś y
    ,hovermode='closest'  #dobiera najbliższa wahite'rtosc dla wskaznika pkb per capita
    )}

##reasumując funkcja dzięki dekoratorowi jest wywoływana i dla każdego roku wybranego przez nas będzie pokazywać ślady w danym roku

print(df.continent.unique())  # information for me



if __name__ == '__main__':
    app.run_server(debug=True, port=8050, dev_tools_hot_reload=True)
