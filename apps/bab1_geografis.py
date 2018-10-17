import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'geografis'

df = pd.read_csv("data/Bab 1-Rata-rata Temperatur Kota Surabaya tahun 2017.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[ {'label': 'Geografis: Temperatur Udara', 'value': 'temperatur-udara'}],
                            value=['temperatur-udara'],
                            multi=True)

geo_layout = template.template(APPS_NAME, dropdown_menu) 

def temperatur_udara(value_name: str):
    perak_1 = df["Rata-rata Temperatur Perak I"]
    perak_2 = df["Rata-rata Temperatur Perak II"]
    juanda = df["Rata-rata Temperatur Juanda Surabaya"] 
    data_1 = go.Scatter(x=df.Bulan, y=perak_1, name="Stasiun Perak I", mode="lines+markers")
    data_2 = go.Scatter(x=df.Bulan, y=perak_2, name="Stasiun Perak II", mode="lines+markers")
    data_3 = go.Scatter(x=df.Bulan, y=juanda, name="Stasiun Juanda", mode="lines+markers")

    data = [data_1, data_2, data_3]
    layout = dict(title='Rata Rata Temperatur Udara di Surabaya Tahun 2017',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Temperatur Udara (Celsius)'),
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
        if x == 'temperatur-udara':
            graphs.append(temperatur_udara(x))
 
    return graphs