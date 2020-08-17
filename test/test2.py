import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H2(children='Hello Dash!'),
    html.A(html.Button('Refresh Data'),href='/'),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x = ['2017','2018','2019','2020'],
                y = [1500,180,220,500],
                name = 'sprzedaż'
            ),
            go.Bar(
                x = ['2017','2018','2019','2020'],
                y = [150,18,250,100],
                name = 'online'
            )
        ])
    ),



])

if __name__ == '__main__':
    app.run_server(debug=True , port = 8051, dev_tools_hot_reload=True)
