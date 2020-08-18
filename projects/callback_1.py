import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input,Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input_1', value='', type='text'),
    html.Div(id='div_1',children=''),

])
@app.callback(
    Output(component_id='div_1',component_property='children'),
    [Input(component_id='input_1',component_property='value')]

)

def update_div(text_input):
    return f"Wprowadzono: {text_input}"
if __name__ == '__main__':
    app.run_server(debug=True, port=8051, dev_tools_hot_reload=True)
