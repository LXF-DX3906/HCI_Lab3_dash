import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import numpy as np

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('E:\github\HCI_Lab3_dash\lab3-datasets\BlackFriday.csv')
#dj = df.sort_values(by='Installs')['Installs'].str.strip('+').unique()
list_sorted = ['0-17', '18-25', '26-35','36-45','46-50','51-55','55+']
#对相关列进行自定义排序
df['Age'] = df['Age'].astype('category').cat.set_categories(list_sorted)

p = df['Age']
q = df['Age'].sort_values()
r = df['Gender'].unique()
m = df[df['Age']=='0-17']['City_Category']
c = df['Stay_In_Current_City_Years'].sort_values().unique()

dff = []
for i in df['City_Category'].sort_values().unique():
    dffff = []
    for j in df['Age'].sort_values().unique():
        dfff = df[df['City_Category']==i]
        value = dfff[dfff['Age']==j]['City_Category'].value_counts()[i]
        dffff.append(value)
    dff.append(dffff)

dage = []
for i in df['Age'].sort_values().unique():
    dage.append(i)

dff2 = []
for i in df['Marital_Status'].sort_values().unique():
    dffff = []
    for j in df['Stay_In_Current_City_Years'].sort_values().unique():
        dfff = df[df['Marital_Status']==i]
        value = dfff[dfff['Stay_In_Current_City_Years']==j]['Marital_Status'].value_counts()[i]
        dffff.append(value)
    dff2.append(dffff)
print(dff[0])
print(dff[1])
print(dff[2])
print(dage)
print(r)
print(df)
