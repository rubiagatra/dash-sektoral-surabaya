import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'pemerintahan'

df = pd.read_csv('data/Bab 2_Pemerintahan dan Keamanan_v1.0_2016.csv')

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Pemerintahan: Produk Hukum Yang Diterbitkan', 'value': 'produk-hukum'},
                                    {'label': 'Pemerintahan: Berkas IPT yang Diproses', 'value': 'berkas-ipt'},
                                    {'label': 'Pemerintahan: Banyaknya Kecelakaan Lalu Lintas', 'value': 'kecelakaan-lalulintas'},
                                    {'label': 'Pemerintahan: Banyaknya Korban Kecelakaan Lalu Lintas', 'value': 'korban-kecelakaan'}], 
                            value=['produk-hukum'],
                            multi=True) 

pemerintahan_layout = template.template(APPS_NAME, dropdown_menu) 

def produk_hukum(value_name: str):
    peraturan_walikota = df["Peraturan Walikota [Produk Hukum]"]
    keputusan_walikota = df["Keputusan Walikota [Produk Hukum]"]
    instruksi_walikotra = df["Instruksi Walikota [Produk Hukum]"]
    peraturan_daerah = df["Peraturan Daerah [Produk Hukum]"]
    data1 = go.Bar(x=df.Bulan, y=peraturan_walikota, name="Peraturan Walikota")
    data2 = go.Bar(x=df.Bulan, y=keputusan_walikota, name="Keputusan Walikota")
    data3 = go.Bar(x=df.Bulan, y=instruksi_walikotra, name="Instruksi Walikota")
    data4 = go.Bar(x=df.Bulan, y=peraturan_daerah, name="Peraturan Daerah") 
        
    data = [data1, data2, data3, data4]
    layout = dict(title='Jumlah Produk Hukum yang Dikeluarkan Tahun 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                barmode='group')
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def berkas_ipt(value_name: str):
    balik_nama = df["Balik Nama/Waktu Penyelesaian (12 hari kerja) [Berkas IPT yang Diproses]"]
    rekom_pengalihan = df["Rekom Pengalihan/Waktu Penyelesaian (10 jam hari kerja) [Berkas IPT yang Diproses]"]
    rekom_imb = df["Rekom IMB/ Waktu Penyelesaian (8 hari kerja) [Berkas IPT yang Diproses]"]
    perpanjangan = df["Perpanjangan/Waktu Penyelesaian (10 hari kerja) [Berkas IPT yang Diproses]"]
    pemutihan = df["Pemutihan/Waktu Penyelesaian (10 hari kerja) [Berkas IPT yang Diproses]"]

    data1 = go.Bar(x=df.Bulan, y=balik_nama, name="Balik Nama")
    data2 = go.Bar(x=df.Bulan, y=rekom_pengalihan, name="Rekom Pengalihan")
    data3 = go.Bar(x=df.Bulan, y=rekom_imb, name="Rekom IMB")
    data4 = go.Bar(x=df.Bulan, y=perpanjangan, name="Perpanjangan") 
    data5 = go.Bar(x=df.Bulan, y=pemutihan, name="Pemutihan") 
        
    data = [data1, data2, data3, data4, data5]
    layout = dict(title='Berkas IPT yang Diproses Tahun 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                barmode='group')
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def kecelakaan_lalulintas(value_name: str):
    kecelakaan = df["Jumlah Kecelakaan"]

    data1 = go.Bar(x=df.Bulan, y=kecelakaan)
    data2 = go.Scatter(x=df.Bulan, y=kecelakaan, mode="lines+markers")
        
    data = [data1, data2]
    layout = dict(title='Banyaknya Kecelakaan Lalu Lintas Tahun 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                barmode='group',
                showlegend=False)
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def kecelakaan_lalulintas(value_name: str):
    kecelakaan = df["Jumlah Kecelakaan"]

    data1 = go.Bar(x=df.Bulan, y=kecelakaan)
    data2 = go.Scatter(x=df.Bulan, y=kecelakaan, mode="lines+markers")
        
    data = [data1, data2]
    layout = dict(title='Banyaknya Kecelakaan Lalu Lintas Tahun 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                barmode='group',
                showlegend=False)
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def korban_kecelakaan(value_name: str):
    meninggal = df["Korban Meninggal"]
    luka_berat = df["Korban Luka Berat"]
    luka_ringan = df["Korban Luka Ringan"]

    data1 = go.Bar(x=df.Bulan, y=meninggal, name="Meninggal")
    data2 = go.Bar(x=df.Bulan, y=luka_berat, name="Luka Berat")
    data3 = go.Bar(x=df.Bulan, y=luka_ringan, name="Luka Ringan")
        
    data = [data1, data2, data3]
    layout = dict(title='Banyaknya Korban Kecelakaan Lalu Lintas Tahun 2016',
                xaxis=dict(title='Bulan'),
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
        if x == 'produk-hukum':
            graphs.append(produk_hukum(x))
        elif x == 'berkas-ipt':
            graphs.append(berkas_ipt(x))
        elif x == 'kecelakaan-lalulintas':
            graphs.append(kecelakaan_lalulintas(x))
        elif x == 'korban-kecelakaan':
            graphs.append(korban_kecelakaan(x))
        
    return graphs
