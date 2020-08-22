import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(
        id = 'num1',
        type = 'number',
        value = 1
    ),

    dcc.Input(
        id = 'num2',
        type = 'number',
        value = 1
    ),

    html.Table([
        html.Tr([html.Td('x + y'), html.Td(id='tr1')]),
        html.Tr([html.Td('x - y'), html.Td(id='tr2')]),
        html.Tr([html.Td('x * y'), html.Td(id='tr3')]),
        html.Tr([html.Td('x / y'), html.Td(id='tr4')]),
        html.Tr([html.Td('x // y'), html.Td(id='tr5')])
    ])
])
@app.callback(  # 5 wyników
    [Output(component_id='tr1',component_property='children'),
    Output(component_id='tr2',component_property='children'),
    Output(component_id='tr3',component_property='children'),
    Output(component_id='tr4',component_property='children'),
    Output(component_id='tr5',component_property='children')],

    [Input('num1','value'), # 2 wejścia
     Input('num2','value')]
)
def update_table(x,y):
    if y==0:
        return x+y, x-y, x*y, 'ZeroDivisionError', 'ZeroDivisionError'
    return x+y, x-y, x*y, x/y, x//y


if __name__ == '__main__':
    app.run_server(debug=True, port=8051, dev_tools_hot_reload=True)
