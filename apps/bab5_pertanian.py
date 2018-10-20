import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'pertanian'

ternak_df = pd.read_csv("data/Bab 5-Populasi Ternak dan Unggas Menurut Jenisnya.csv")
sayur_df = pd.read_csv("data/Bab 5-Produksi Tanaman Sayur Menurut Jenisnya (ton) Tahun 2010-2017.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Peternakan: Ternak dan Unggas', 'value': 'ternak-unggas'},
                                    {'label': 'Peternakan: Sayur Mayur', 'value': 'sayur-mayur'}],
                            value=['ternak-unggas'],
                            multi=True)

pertanian_layout = template.template(APPS_NAME, dropdown_menu) 

def ternak_unggas(value_name: str):
    sapi = ternak_df["Sapi"]
    sapi_perah = ternak_df["Sapi Perah"]
    kerbau = ternak_df["Kerbau"]
    kambing = ternak_df["Kambing"]
    domba = ternak_df["Domba"]
    babi = ternak_df["Babi"]
    itik = ternak_df["Itik"]
    ayam = ternak_df["Ayam"]
    data_1 = go.Scatter(x=ternak_df.Tahun, y=sapi, name="Sapi", mode="lines+markers")
    data_2 = go.Scatter(x=ternak_df.Tahun, y=sapi_perah, name="Sapi Perah", mode="lines+markers")
    data_3 = go.Scatter(x=ternak_df.Tahun, y=kerbau, name="Kerbau", mode="lines+markers")
    data_4 = go.Scatter(x=ternak_df.Tahun, y=kambing, name="Kambing", mode="lines+markers")
    data_5 = go.Scatter(x=ternak_df.Tahun, y=domba, name="Domba", mode="lines+markers")
    data_6 = go.Scatter(x=ternak_df.Tahun, y=babi, name="Babi", mode="lines+markers")
    data_7 = go.Scatter(x=ternak_df.Tahun, y=itik, name="Itik", mode="lines+markers")
    data_8 = go.Scatter(x=ternak_df.Tahun, y=ayam, name="Ayam", mode="lines+markers")


    data = [data_1, data_2, data_3, data_4, data_6, data_7, data_8]
    layout = dict(title='Populasi Ternak dan Unggas Menurut Jenisnya',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def sayur_mayur(value_name: str):
    lombok = sayur_df["Lombok"]
    tomat = sayur_df["Tomat"]
    bayam = sayur_df["Bayam"]
    sawi = sayur_df["Sawi"]
    kangkung = sayur_df["Kangkung"]
    garbis_melon_semangka = sayur_df["Garbis/Melon/Semangka"]
    data_1 = go.Scatter(x=ternak_df.Tahun, y=lombok, name="Lombok", mode="lines+markers")
    data_2 = go.Scatter(x=ternak_df.Tahun, y=tomat, name="Tomat", mode="lines+markers")
    data_3 = go.Scatter(x=ternak_df.Tahun, y=bayam, name="Bayam", mode="lines+markers")
    data_4 = go.Scatter(x=ternak_df.Tahun, y=sawi, name="Sawi", mode="lines+markers")
    data_5 = go.Scatter(x=ternak_df.Tahun, y=kangkung, name="Kangkung", mode="lines+markers")
    data_6 = go.Scatter(x=ternak_df.Tahun, y=garbis_melon_semangka, name="Garbis/Melon/Semangka", mode="lines+markers")


    data = [data_1, data_2, data_3, data_4, data_6]
    layout = dict(title='Produksi Tanaman Sayur Menurut Jenisnya (ton) Tahun 2010-2017',
                xaxis=dict(title='Tahun'),
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
        if x == 'ternak-unggas':
            graphs.append(ternak_unggas(x))
        elif x == 'sayur-mayur':
            graphs.append(sayur_mayur(x)) 
    return graphs