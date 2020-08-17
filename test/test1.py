import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

colors = {
    'background':'#2315a1',
    'text': '#121212'
}

app.layout = html.Div(children=[

    html.H2(children='Hello Dash!',
            style = {
                'color':colors['background'],
            'textAlign': 'center',
            'font-size': 30}
            ),
    html.Div('Hey Space',
             style={
                 'font-size': colors['text'],
                 'textAlign': 'center',
                 'background-color': 'grey'
             }),
    html.A(html.Button('Refresh Data'),href='/'),

    dcc.Graph(
        figure=go.Figure([
            go.Bar(
                x = ['2017','2018','2019','2020'],
                y = [1500,180,220,500],
                name = 'sprzedaż',
                marker_color = '#2c2fd1'
            ),
            go.Bar(
                x = ['2017','2018','2019','2020'],
                y = [150,18,250,100],
                name = 'online',
                marker_color = '#ff0303',
                marker_line_color = '#121212',
                marker_line_width = 2,
            )
        ],
        layout=go.Layout(
            title= 'Doświadczenie Maciej Sikora',
            # plot_bgcolor='black',
            paper_bgcolor='#78788a'
        )
        )
    ),
# dcc.Graph(
#         figure=go.Figure([
#             go.Bar(
#                 x = ['2017','2018','2019','2020'],
#                 y = [1500,180,220,500],
#                 name = 'sprzedaż'
#             ),
#             go.Bar(
#                 x = ['2017','2018','2019','2020'],
#                 y = [150,18,250,100],
#                 name = 'online'
#             )
#         ])
#     ),

],
style={
    'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server(debug=True , port = 8051, dev_tools_hot_reload=True)



