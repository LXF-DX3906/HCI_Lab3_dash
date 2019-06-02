import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('E:\github\HCI_Lab3_dash\lab3-datasets\BlackFriday.csv')
Age_sorted = ['0-17', '18-25', '26-35','36-45','46-50','51-55','55+']
#对相关列进行自定义排序
df['Age'] = df['Age'].astype('category').cat.set_categories(Age_sorted)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Graph(
                id='example-graph-1',
                figure={
                    'data': [
                        {'x': df[df['User_ID']]['Age'].sort_values().unique(),
                         'y': df['Age'].sort_values().value_counts(),
                         'type': 'bar', 'name': 'SF'},
                    ],
                    'layout': {
                        'title': 'Age '
                    }
                }
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='example-graph-2',
                figure={
                    'data': [
                        {'Lables': df['City_Category'].sort_values().unique(),
                         'values': df['City_Category'].sort_values().value_counts(),
                         'type': 'pie',},
                    ],
                    'layout': {
                        'title': 'City_Category '
                    }
                }
            ),
        ], style={'width': '48%', 'float': 'right','display': 'inline-block'}),
        html.Div([
            dcc.Graph(
                id='example-graph-3',
                figure={
                    'data': [
                        {'lables': df['Gender'].sort_values().unique(),
                         'values': df['Gender'].sort_values().value_counts(),
                         'type': 'pie',
                         },
                    ],
                }
            ),
        ], style={'width': '48%', 'display': 'inline-block'}),
         html.Div([
            dcc.Graph(
                id='example-graph-4',
                figure={
                    'data': [
                        {'x': df['Age'].sort_values().unique(),
                         'y': df['Age'].sort_values().value_counts(),
                         'type': 'line'},
                    ],
                    'layout': {
                        'title': 'City_Category '
                    }
                }
            ),
        ], style={'width': '48%', 'float': 'right','display': 'inline-block'}),
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True)
