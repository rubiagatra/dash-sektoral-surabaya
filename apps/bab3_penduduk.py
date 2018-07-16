import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

df = pd.read_csv("data/Bab 3/Graph ke-1 Bab 3.csv")
APPS_NAME = 'penduduk'


dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Banyaknya Penduduk Berdasarkan Jenis Kelamin', 'value': 'jenis-kelamin'}, 
                                   ],
                            value=['jenis-kelamin'],
                            multi=True) 
penduduk_layout = template.template(APPS_NAME, dropdown_menu) 

def jenis_kelamin(value_name: str):
    laki = df['Laki-laki/ Male']
    perempuan = df['Perempuan/ Female'] 
    data1 = go.Scatter(x=df['Tahun/Year'], y=laki, name="Laki - Laki", mode="lines+markers")
    data2 = go.Scatter(x=df['Tahun/Year'], y=perempuan, name="Perempuan", mode="lines+markers")
    data = [data1, data2]
    layout = dict(title='Banyaknya Penduduk Berdasarkan Jenis Kelamin',
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
        if x == 'jenis-kelamin':
            graphs.append(jenis_kelamin(x))
    return graphs