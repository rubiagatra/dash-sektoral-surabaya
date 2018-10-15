import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'pemerintahan'

df = pd.read_csv('data/Bab 2-Banyaknya Surat Ijin Mendirikan Bangunan (IMB) yang dikeluarkan Menurut Jenis Bangunan tahun 2009-2017.csv')

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Pemerintahan: Surat Ijin Mendirikan Bangunan (IMB)', 'value': 'surat-imb'}], 
                            value=['surat-imb'],
                            multi=True) 

pemerintahan_layout = template.template(APPS_NAME, dropdown_menu) 

def surat_imb(value_name: str):
    bangungan_tempat_tinggal = df["Bangunan Tempat Tinggal"]
    bangunan_bukan_tempat_tinggal = df["Bangunan Bukan Tempat Tinggal"]
    realisasi = df["Realisasi"]

    data_1 = go.Bar(x=df.Tahun, y=bangungan_tempat_tinggal, name="Bangunan Tempat Tinggal")
    data_2 = go.Bar(x=df.Tahun, y=bangunan_bukan_tempat_tinggal, name="Bangunan Bukan Tempat Tinggal")
    data_3 = go.Bar(x=df.Tahun, y=realisasi, name="Realisasi")
        
    data = [data_1, data_2, data_3]
    layout = dict(title='Bab 2-Banyaknya Surat Ijin Mendirikan Bangunan (IMB) yang dikeluarkan Menurut Jenis Bangunan tahun 2009-2017',
                xaxis=dict(title='Tahun'),
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
        if x == 'surat-imb':
            graphs.append(surat_imb(x))
        
    return graphs
