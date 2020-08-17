import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from _datetime import datetime as dt


app = dash.Dash(__name__)

app.layout = html.Div(
    [
    html.A(html.Button('Refresh Data'), href='/'),
    html.H1('Witaj w EasyM'),
    html.Label("Wybierz pakiet dla Ciebie"),
    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        placeholder='Wybierz z listy'
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        value =  'py'
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        value= 'Java',
        multi=True,
        # disabled=True
    ),
    html.Br()
        ,
    dcc.Slider(
        min = 0,
        max = 10,
        step = 1
    ),
    dcc.Slider(
        min=0,
        max=3,
        step=1,
        marks={k:f'Label: {k*5}' for k in range(4)}
        # marks = {k:'Label' + ':' + str(k) for k in range(4)}  #trening z dict comprahensions

        ),
    html.Br()
        ,
    dcc.Input(
        type = 'text',
        placeholder='Wpisz swoje imie'
    ),
    dcc.Input(
        type = 'number'
    ),
    dcc.Input(
        type='password'),
    dcc.Input(
        type='email'
    ),
    dcc.Textarea(
        placeholder='Wprowadź tekst',
        style={'width': '30%'},
        maxLength=10,
    ),
    dcc.Checklist(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        value= ['py']

    ),
    dcc.RadioItems(
        options=[
            {'label': 'Python', 'value': 'py'},
            {'label': 'SQL', 'value': 'sql'},
            {'label': 'JavaScript', 'value': 'js'}
        ],
        value = 'js',
        labelStyle = {'display': 'inline-block'}
    ),
    html.Button("Kup teraz!"),
    html.Button("Kup potem!", disabled=True,),
    html.Button("Kup wszystko!", type='submit'),
    dcc.DatePickerSingle(
        date= dt(2020,8,17),
        display_format='YYYY-MM-DD'
),
    dcc.DatePickerRange(
        start_date=dt(2020,10,10),
        end_date=dt(2020,11,11),
        min_date_allowed=dt(2020,10,10),
        max_date_allowed=dt(2020,11,11)
    ),
    dcc.Markdown(
'''
1. Kup już
2. Kup potem
3. Kup wszystko

* 1
* 2
* 3

[udemy.com](http://www.udemy.com)

Kod:
```
import numpy as np
print("Witajcie kochani")
for i in range(8):
    print(f"Dziś okazja numer {i})
```


Tabela:

|imie    |nazwisko   |wynik  |
|--------|-----------|-------|
|Marek   |Konrad     | 78    |
|Marek   |Konrad     | 44    |
|Marek   |Konrad     | 42    |
|Marek   |Konrad     | 38    |
|Marek   |Konrad     | 38    |
|Marek   |Konrad     | 34    |


abc

abc

bcd
> To najlepszy kurs na świecie
'''
    ),
    dcc.Tabs(
        children=[
            dcc.Tab(label='Matura',
                    children=[
                        dcc.Markdown("""
                        ```
                        import numpy as numpy
                        print("Welcome in python course")
                        ```
                        """)
                    ]
            ),
            dcc.Tab(label= 'Kurs',
                    children=[
                        dcc.Markdown("""
                        Na kursie nauczysz się m.in.:
                        * Matematyka
                        * Excel
                        * Python
                        
                        Do zobaczenia!
                        """)
                    ]
            )
        ]
    )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8051, dev_tools_hot_reload=True)
