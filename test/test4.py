import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)


def fetch(company="AMZN"):
    import pandas_datareader.data as web
    return web.DataReader(name=company, data_source='stooq')


df = fetch()
df.reset_index(inplace=True)
df = df[:30]
min_val = min(len(df), 30)
app.layout = html.Div([
    html.H4('Notowania spółki Amazon'),
    html.Table([
                   html.Tr([html.Th(col) for col in df.columns])] +
               [html.Tr([html.Td(df.iloc[i][col]) for col in df.columns]) for i in range(min_val)]
               ),
    dcc.Graph(
        figure = go.Figure(
            data = [
                go.Scatter(
                    x = df.Date,
                    y = df.Close,
                    mode = 'lines',
                    fill = 'tozeroy',
                    name = 'Amazon'
                )
            ],
            layout =  go.Layout(
                yaxis_type = 'log',
                title_text = 'Wykres cen Amazon',
                height = 300,
                showlegend = True,
            )
        )
    ),
    dcc.Graph(                   #graf
        figure = go.Figure(    #figura
            data = [                #podajemy dane do wykresu
                go.Bar(         #okreslamy rodzaj wykresu
                    x = df.Date,
                    y = df.Volume,
                    name = 'Volume',
                    marker_color = 'red',
                    marker_line_color = 'blue'
            )
        ],
            layout = go.Layout(
                yaxis_type = 'log',
                height = 300,
                title_text = 'Charts volumenu',
                showlegend = True
        )
    )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8059, dev_tools_hot_reload=True)
