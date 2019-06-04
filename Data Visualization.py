import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('datasets\BlackFriday.csv')

Age_sorted = ['0-17', '18-25', '26-35','36-45','46-50','51-55','55+']
df['Age'] = df['Age'].astype('category').cat.set_categories(Age_sorted)

row1 = html.Div([
    html.Div([
        dcc.Graph(
                    id="Gender",
                    figure={
                    'data': [
                        {'lables': df['Gender'].sort_values().unique(),
                         'values': df['Gender'].sort_values().value_counts(),
                         'type': 'pie',
                        },
                    ],
                    'layout': 
                        {'title': 'Gender'},
                    },
        )
    ], style={'width': '32%', 'float': 'left', 'display': 'inline-block'},),
    html.Div([
        dcc.Graph(
                    id="City_Category", 
                    figure={
                    'data': [
                        {'Lables': df['City_Category'].sort_values().unique(),
                         'values': df['City_Category'].sort_values().value_counts(),
                         'type': 'pie',},
                    ],
                    'layout': 
                        {'title': 'City_Category'},
                    },
        )
    ], style={'width': '32%', 'display': 'inline-block'},),
    html.Div([
        dcc.Graph(
                    id="Marital_Status", 
                    figure={
                    'data': [
                        {'Lables': df['Marital_Status'].sort_values().unique(),
                         'values': df['Marital_Status'].sort_values().value_counts(),
                         'type': 'pie',},
                    ],
                    'layout': 
                        {'title': 'Marital_Status'},
                    },
        )
    ], style={'width': '32%', 'float': 'right', 'display': 'inline-block'},),
], className='row')


dff = []
for i in df['City_Category'].sort_values().unique():
    dffff = []
    for j in df['Age'].sort_values().unique():
        dfff = df[df['City_Category']==i]
        value = dfff[dfff['Age']==j]['City_Category'].value_counts()[i]
        dffff.append(value)
    dff.append(dffff)
row2 = html.Div([
    html.Div([
                dcc.RadioItems(
                    id='bar_line',
                    options=[{'label': i, 'value': i} for i in ['bar', 'line']],
                    value='line',
                    labelStyle={'display': 'inline-block'}
                ),
                dcc.Graph(id='Age'),
            ],
            style={'width': '48%', 'display': 'inline-block'}
            ),
    html.Div([
            dcc.Graph(
                    id="Age-City_Category", 
                    figure={
                        'data': [
                            {'x': df['Age'].sort_values().unique(), 'y': dff[0], 'type': 'bar', 'name': 'A'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff[1], 'type': 'bar', 'name': 'B'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff[2], 'type': 'bar', 'name': 'C'},
                        ],
                        'layout': {
                            'title': 'Age-City_Category'
                        }
                    },
            )
        ],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
],className='row')


dff1 = []
for i in df['Stay_In_Current_City_Years'].sort_values().unique():
    dffff = []
    for j in df['Age'].sort_values().unique():
        dfff = df[df['Stay_In_Current_City_Years']==i]
        value = dfff[dfff['Age']==j]['Stay_In_Current_City_Years'].value_counts()[i]
        dffff.append(value)
    dff1.append(dffff)
dff2 = []
for i in df['Marital_Status'].sort_values().unique():
    dffff = []
    for j in df['Stay_In_Current_City_Years'].sort_values().unique():
        dfff = df[df['Marital_Status']==i]
        value = dfff[dfff['Stay_In_Current_City_Years']==j]['Marital_Status'].value_counts()[i]
        dffff.append(value)
    dff2.append(dffff)
row3 = html.Div([
    html.Div([
            dcc.Graph(
                    id="Age-Stay_In_Current_City_Years", 
                    figure={
                        'data': [
                            {'x': df['Age'].sort_values().unique(), 'y': dff1[0], 'type': 'bar', 'name': '0'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff1[1], 'type': 'bar', 'name': '1'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff1[2], 'type': 'bar', 'name': '2'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff1[3], 'type': 'bar', 'name': '3'},
                            {'x': df['Age'].sort_values().unique(), 'y': dff1[4], 'type': 'bar', 'name': '4+'},
                        ],
                        'layout': {
                            'title': 'Age-Stay_In_Current_City_Years'
                        }
                    },
            )
        ],
        style={'width': '48%','display': 'inline-block'}),
    html.Div([
            dcc.Graph(
                     id="Stay_In_Current_City_Years-Marital_Status", 
                    figure={
                        'data': [
                            {'x': ['0-1','1-2','2-3','3-4','4+'], 'y': dff2[0], 'type': 'bar', 'name': '0'},
                            {'x': ['0-1','1-2','2-3','3-4','4+'], 'y': dff2[1], 'type': 'bar', 'name': '1'},
                        ],
                        'layout': {
                            'title': 'Stay_In_Current_City_Years-Marital_Status'
                        }
                    },
            )
        ],
        style={'width': '48%', 'float': 'right', 'display': 'inline-block'}),
],className='row')

app.layout = html.Div([
   row1,
   row2,
   row3,
])


@app.callback(
    Output('Age', 'figure'),
    [Input('bar_line', 'value')])
def update_graph(bar_line):
    if bar_line == 'bar':
        return {
            'data': [go.Bar(
                x=df['Age'].sort_values().unique(),
                y=df['Age'].sort_values().value_counts(),
            )],
            'layout': go.Layout(
                title='Age',
        )
        }
    elif bar_line == 'line':
        return {
            'data': [go.Line(
                x=df['Age'].sort_values().unique(),
                y=df['Age'].sort_values().value_counts(),
            )],
            'layout': go.Layout(
                title='Age',
            )
        }

if __name__ == '__main__':
    app.run_server(debug=True)
