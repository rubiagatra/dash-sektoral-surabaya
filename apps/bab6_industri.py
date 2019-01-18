import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'industri'

df = pd.read_csv("data/Bab 6-Produksi Air Minum per Bulan tahun 2017.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Industri: Produksi Air', 'value': 'produksi-air'},],
                            value=['produksi-air'],
                            multi=True)

industri_layout = template.template(APPS_NAME, dropdown_menu) 

def produksi_air(value_name: str):
    sumber_air = df["Sumber Air"]
    ngaggel_1 = df["Ngagel I"]
    ngaggel_2 = df["Ngagel II"]
    ngaggel_3 = df["Ngagel III"]
    krpl_1 = df["KRPL I"]
    krpl_2 = df["KRPL II"]
    krpl_3 = df["KRPL III"]
    data_1 = go.Scatter(x=df.Bulan, y=sumber_air, name="Sumber Air", mode="lines+markers")
    data_2 = go.Scatter(x=df.Bulan, y=ngaggel_1, name="Ngaggel I", mode="lines+markers")
    data_3 = go.Scatter(x=df.Bulan, y=ngaggel_2, name="Ngaggel II", mode="lines+markers")
    data_4 = go.Scatter(x=df.Bulan, y=ngaggel_3, name="Ngaggel III", mode="lines+markers")
    data_5 = go.Scatter(x=df.Bulan, y=krpl_1, name="KRPL I", mode="lines+markers")
    data_6 = go.Scatter(x=df.Bulan, y=krpl_2, name="KRPL II", mode="lines+markers")
    data_7 = go.Scatter(x=df.Bulan, y=krpl_3, name="KRPL III", mode="lines+markers")


    data = [data_1, data_2, data_3, data_4, data_5, data_6, data_7]
    layout = dict(title='Produksi Air Minum per Bulan tahun 2017',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
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
        if x == 'produksi-air':
            graphs.append(produksi_air(x))
    return graphs