import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Notowania spółki amazon"),
    html.Table([
        html.Tr([
            html.Th('Date'),
            html.Th('Open'),
            html.Th('High'),
            html.Th('Low'),
            html.Th('Close'),
            html.Th('Volume')
        ]),
        html.Tr([
            html.Td('2019-10-10'),
            html.Td('20'),
            html.Td('201'),
            html.Td('2'),
            html.Td('258'),
            html.Td('2010'),
        ]),
        html.Tr([
            html.Td('2020-10-10'),
            html.Td('102'),
            html.Td('1'),
            html.Td('0'),
            html.Td('2'),
            html.Td('20100'),
        ])
    ])
]
)

if __name__ == '__main__':
    app.run_server(debug=True , port = 8050, dev_tools_hot_reload=True)
