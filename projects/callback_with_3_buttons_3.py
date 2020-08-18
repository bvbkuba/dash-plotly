import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from datetime import datetime

app = dash.Dash(__name__)

app.layout = html.Div([    # w layout układamy buttony, które chcemy, odpowiednio je nazywając. Ponadto dajemy div np. na output
    html.Button(id = 'button1', children= 'Button1', n_clicks_timestamp=0,),    #wartość 0 oznacza 1/1/1970
    html.Button(id = 'button2', children= 'Button2', n_clicks_timestamp=0 ),
    html.Button(id = 'button3', children= 'Button3', n_clicks_timestamp=0 ),
    html.Div(style={'margin-top': '8px'}),
    html.Div(id='div_1')      # section to results
])

@app.callback(
    Output('div_1','children'),    #always once time write
    [Input('button1','n_clicks_timestamp'),  # 1st arg
    Input('button2','n_clicks_timestamp'),   #2nd arg
    Input('button3','n_clicks_timestamp')]  # 3 rd arg
    )
def display_click(button1,button2,button3):
    if int(button1)>int(button2) and int(button1)>int(button3):
        msg = 'Button1 został wciśnięty ostatni'
    elif int(button2)>int(button1) and int(button2)>int(button3):
        msg = 'Button2 został wciśnięty ostatni'
    elif int(button3)>int(button1) and int(button3)>int(button2):
        msg = 'Button3 został wciśnięty ostatni'
    else:
        msg = 'Nic nie zostało kliknięte'
    return html.Div([
        html.Div(f"btn1: {datetime.fromtimestamp(button1/1000)}"), # /1000 bo timestamp podaje czas w milisekundach
        html.Div(f"btn2: {datetime.fromtimestamp(button2/1000)}"),
        html.Div(f"btn3: {datetime.fromtimestamp(button3/1000)}"),
        html.Br(),
        html.Div(f"Opis: {msg}")
    ])

if __name__ == '__main__':
    app.run_server(debug=True, port=8051, dev_tools_hot_reload=True)
