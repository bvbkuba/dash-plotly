import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input,Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input_1', value='', type='text'),
    html.Div(id='div_1',children='')

])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051, dev_tools_hot_reload=True)
