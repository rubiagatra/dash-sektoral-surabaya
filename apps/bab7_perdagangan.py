import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'perdagangan'

df = pd.read_csv("data/Bab 7-Banyaknya Persediaan, Pemasukan dan Pengeluaran Beras per Bulan.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Perdagangan: Perdagangan Beras', 'value': 'perdagangan-beras'},],
                            value=['perdagangan-beras'],
                            multi=True)

perdagangan_layout = template.template(APPS_NAME, dropdown_menu) 

def perdagangan_beras(value_name: str):
    persediaan = df["Persediaan"]
    pemasukan = df["Pemasukan"]
    pengeluaran = df["Pengeluaran"]
   
    data_1 = go.Scatter(x=df.Bulan, y=persediaan, name="Persediaan", mode="lines+markers")
    data_2 = go.Scatter(x=df.Bulan, y=pemasukan, name="Pemasukan", mode="lines+markers")
    data_3 = go.Scatter(x=df.Bulan, y=pengeluaran, name="Pengeluaran", mode="lines+markers")

    data = [data_1, data_2, data_3]
    layout = dict(title='Banyaknya Persediaan, Pemasukan dan Pengeluaran Beras per Bulan',
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
        if x == 'perdagangan-beras':
            graphs.append(perdagangan_beras(x))
    return graphs