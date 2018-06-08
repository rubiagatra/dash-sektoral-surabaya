import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'geografis'

df_geo = pd.read_csv("data/Bab 1_Geografis_v2.0_2016.csv")
df = pd.read_csv("data/hujansurabaya.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Geografis: Rata - Rata Curah Hujan', 'value': 'curah-hujan'}, 
                                    {'label': 'Geografis: Jumlah Hari Hujan', 'value': 'hari-hujan'},
                                    {'label': 'Geografis: Kelembapan Udara', 'value': 'kelembapan-udara'}],
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
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Curah Hujan (mm)'),
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
    layout = dict(title='Jumlah Hari Hujan di Surabaya Tahun 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah Hari Hujan'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def kelembapan_udara(value_name: str):
    juanda_max = df_geo['Maksimal Kelembaban (%) di Juanda']
    juanda_min = df_geo['Minimal Kelembaban (%) di Juanda']
    perak = df_geo["Rata-rata Kelembaban (%) di Tanjung Perak"]
    data_juanda_max = go.Scatter(x=df.Bulan, 
                                y=juanda_max, 
                                name="Max", 
                                line=dict(color=('rgb(205, 12, 24)'),
                                    width=4,
                                ))
    data_juanda_min = go.Scatter(x=df.Bulan, 
                                y=juanda_min, 
                                name="Min", 
                                line=dict(color=('rgb(205, 12, 24)'),
                                    width=4,
                                ))
    data_juanda_mean = go.Scatter(x=df.Bulan, 
                                y=(juanda_max + juanda_min) / 2, 
                                name="Rata-rata", 
                                line=dict(color=('rgb(205, 12, 24)'),
                                    width=4,
                                    dash='dot',
                                ))
    data_perak_mean = go.Scatter(x=df.Bulan, 
                            y=perak, 
                            name="Rata-rata", 
                            mode="lines+markers",
                            )
    data_juanda = [data_juanda_max, data_juanda_min, data_juanda_mean]
    data_perak = [data_perak_mean]
    layout_juanda = dict(title='Kelembapan Udara Stasiun Juanda 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Kelembapan Udara (%)'),
                )
    layout_perak = dict(title='Rata - rata Kelembapan Udara Stasiun Perak 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Kelembapan Udara (%)'),
                )
    fig_juanda = dict(data=data_juanda, layout=layout_juanda)
    fig_perak = dict(data=data_perak, layout=layout_perak)
    
    return [dcc.Graph(
        id=value_name + "-juanda",
        figure=fig_juanda,
        style={"width": "50%", "display": "inline-block"}
    ),
    dcc.Graph(
        id=value_name + "-perak",
        figure=fig_perak,
        style={"width": "50%", "display": "inline-block"}
    )]


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
        elif x == 'kelembapan-udara':
            graphs.extend(kelembapan_udara(x))
    return graphs