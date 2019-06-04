# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)





    dcc.Graph(
                    id="Stay_In_Current_City_Years_Marital_Status", 
                    figure={
                        'data': [
                            {'x': df['Current_City_Years_Marital_Status'].sort_values().unique(), 'y': dff2[0], 'type': 'bar', 'name': '0'},
                            {'x': df['Current_City_Years_Marital_Status'].sort_values().unique(), 'y': dff2[1], 'type': 'bar', 'name': '1'},
                        ],
                        'layout': {
                            'title': 'Stay_In_Current_City_Years_Marital_Status'
                        }
                    },
            )