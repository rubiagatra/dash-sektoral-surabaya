import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'geografis'

df = pd.read_csv('data/hujansurabaya.csv')
dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Geografis: Rata - Rata Curah Hujan', 'value': 'curah-hujan'}, {'label': 'Geografis: Jumlah Hari Hujan', 'value': 'hari-hujan'}],
                            value=['curah-hujan'],
                            multi=True)

geo_layout = template.template(APPS_NAME, dropdown_menu) 

def curah_hujan(value_name: str):
    perak = df["Curah Hujan (Perak)"]
    juanda = df["Curah Hujan (Juanda)"] 
    data1 = go.Scatter(x=df.Bulan, y=perak, name="Stasiun Perak II", mode="lines+markers")
    data2 = go.Scatter(x=df.Bulan, y=juanda, name="Stasiun Juanda", mode="lines+markers")
    data = [data1, data2]
    layout = dict(title='Rata Rata Curah Hujan di Surabaya Tahun 2016',
                xaxis=dict(title = 'Bulan'),
                yaxis=dict(title = 'Curah Hujan (mm)'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def hari_hujan(value_name: str):
    perak = df["Hari Hujan (Perak)"]
    juanda = df["Hari Hujan (Juanda)"]
    data1 = go.Scatter(x=df.Bulan, y=perak, name="Stasiun Perak II", mode="lines+markers")
    data2 = go.Scatter(x=df.Bulan, y=juanda, name="Stasiun Juanda", mode="lines+markers")
    data = [data1, data2]
    layout = dict(title = 'Jumlah Hari Hujan di Surabaya Tahun 2016',
                xaxis=dict(title = 'Bulan'),
                yaxis=dict(title = 'Jumlah Hari Hujan'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

@app.callback(
    Output('graphs-' + APPS_NAME, 'children'),
    [Input('data-input-' + APPS_NAME, 'value')],
)
def update_graph(data):
    graphs = []
    for x in data:
        if x == 'curah-hujan':
            graphs.append(curah_hujan(x))
        elif x == 'hari-hujan':
            graphs.append(hari_hujan(x))
    return graphs