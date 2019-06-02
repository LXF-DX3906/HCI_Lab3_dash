import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('E:\github\HCI_Lab3_dash\lab3-datasets\BlackFriday.csv')
#dj = df.sort_values(by='Installs')['Installs'].str.strip('+').unique()
list_sorted = ['0-17', '18-25', '26-35','36-45','46-50','51-55','55+']
#对相关列进行自定义排序
df['Age'] = df['Age'].astype('category').cat.set_categories(list_sorted)

p = df[df['User_ID']]['Age']
q = df['Age'].sort_values()
r = df['Gender'].unique()
print(df)
