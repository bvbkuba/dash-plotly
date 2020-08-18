import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Input(id = 'input_1', type = 'text', value = '')
    ]),
    html.Button(id = 'button_1', children = 'Submit', n_clicks = 0),
    html.Div(id = 'div_1', children = 'Input text and press Submit'),
])
@app.callback(
    Output(component_id = 'div_1',component_property = 'children'),
    [Input(component_id= 'input_1', component_property = 'value'),
     Input(component_id = 'button_1', component_property = 'n_clicks')]

)
def update_output(value, n_clicks):
    return f"Wprowadziłeś {value} i przycisnąłeś {n_clicks} razy."
if __name__ == '__main__':
    app.run_server(debug=True , port = 8052, dev_tools_hot_reload=True)
