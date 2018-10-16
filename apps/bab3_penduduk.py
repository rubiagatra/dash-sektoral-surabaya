import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

kelahiran_df = pd.read_csv("data/Bab 3-Banyak Kelahiran Menurut Jenis Kelamin dan Kecamatan tahun 2017.csv")
kematian_df = pd.read_csv("data/Bab 3-Banyaknya Kematian yang Dilaporkan Menurut Jenis Kelamin dan Kecamatan tahun 2017.csv")
jumlah_penduduk_df = pd.read_csv("data/Bab 3-Jumlah Penduduk Kota Surabaya Hasil Sensus Penduduk 2010.csv")

APPS_NAME = 'penduduk'


dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Penduduk: Kelahiran Menurut Jenis Kelamin', 'value': 'kelahiran'}, 
                                {'label': 'Penduduk: Kematian Menurut Jenis Kelamin', 'value': 'kematian'},
                                {'label': 'Penduduk: Jumlah Penduduk Kota Surabaya Hasil Sensus Penduduk 2010', 'value': 'jumlah-penduduk'}     
                                   ],
                            value=['kelahiran'],
                            multi=True) 
penduduk_layout = template.template(APPS_NAME, dropdown_menu) 

def kelahiran(value_name: str):
    laki_laki = kelahiran_df["Laki-laki"]
    perempuan = kelahiran_df["Perempuan"]

    data_1 = go.Bar(x=kelahiran_df.Kecamatan, y=laki_laki, name="Laki - laki")
    data_2 = go.Bar(x=kelahiran_df.Kecamatan, y=perempuan, name="Perempuan")
        
    data = [data_1, data_2]
    layout = dict(title='Banyak Kelahiran Menurut Jenis Kelamin dan Kecamatan tahun 2017',
                xaxis=dict(title='Kecamatan'),
                yaxis=dict(title='Jumlah'),
                barmode='group')
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def kematian(value_name: str):
    laki_laki = kematian_df["Laki-laki"]
    perempuan = kematian_df["Perempuan"]

    data_1 = go.Bar(x=kematian_df.Kecamatan, y=laki_laki, name="Laki - laki")
    data_2 = go.Bar(x=kematian_df.Kecamatan, y=perempuan, name="Perempuan")
        
    data = [data_1, data_2]
    layout = dict(title='Banyaknya Kematian yang Dilaporkan Menurut Jenis Kelamin dan Kecamatan tahun 2017',
                xaxis=dict(title='Kecamatan'),
                yaxis=dict(title='Jumlah'),
                barmode='group')
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def jumlah_penduduk(value_name: str):
    laki_laki = jumlah_penduduk_df["Laki-laki"]
    perempuan = jumlah_penduduk_df["Perempuan"]

    data_1 = go.Bar(x=jumlah_penduduk_df["Kelompok Umur"], 
                    y=laki_laki, name='Laki - laki',
                    )
    data_2 = go.Bar(x=jumlah_penduduk_df["Kelompok Umur"], 
                    y=perempuan, name="Perempuan",
                    )
        
    data = [data_1, data_2]
    layout = dict(title='Jumlah Penduduk Kota Surabaya Hasil Sensus Penduduk 2010',
                xaxis=dict(title='Kelompok Umur'),
                yaxis=dict(title='Jumlah'),
                barmode='group')
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
        if x == 'kelahiran':
            graphs.append(kelahiran(x))
        elif x == 'kematian':
            graphs.append(kematian(x))
        elif x == 'jumlah-penduduk':
            graphs.append(jumlah_penduduk(x))

    return graphs