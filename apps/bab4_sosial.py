import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'sosial'

donor_darah_df = pd.read_csv("data/Bab 4-Banyaknya Donor Darah yang Datang ke UDD dan Melalui Mobil Unit.csv")
rumah_sakit_df = pd.read_csv("data/Bab 4-Banyaknya Rumah Sakit di Kota Surabaya.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Sosial: Donor Darah', 'value': 'donor-darah'},
                                    {'label': 'Sosial: Rumah Sakit', 'value': 'rumah-sakit'}],
                            value=['donor-darah'],
                            multi=True)

sosial_layout = template.template(APPS_NAME, dropdown_menu) 

def donor_darah(value_name: str):
    gol_darah_a = donor_darah_df["Golongan Darah A"]
    gol_darah_b = donor_darah_df["Golongan Darah B"]
    gol_darah_ab = donor_darah_df["Golongan Darah AB"]
    gol_darah_o = donor_darah_df["Golongan Darah O"]
    data_1 = go.Scatter(x=donor_darah_df.Bulan, y=gol_darah_a, name="Golongan Darah A", mode="lines+markers")
    data_2 = go.Scatter(x=donor_darah_df.Bulan, y=gol_darah_b, name="Golongan Darah B", mode="lines+markers")
    data_3 = go.Scatter(x=donor_darah_df.Bulan, y=gol_darah_ab, name="Golongan Darah AB", mode="lines+markers")
    data_4 = go.Scatter(x=donor_darah_df.Bulan, y=gol_darah_o, name="Golongan Darah O", mode="lines+markers")

    data = [data_1, data_2, data_3, data_4]
    layout = dict(title='Banyaknya Donor Darah yang Datang ke UDD dan Melalui Mobil Unit',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Jumlah'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id=value_name,
        figure=fig,
    )

def rumah_sakit(value_name: str):
    jumlah = rumah_sakit_df["Jumlah"]
    data_1 = go.Pie(labels=rumah_sakit_df['Jenis Rumah Sakit'], values=jumlah)

    data = [data_1]
    layout = dict(title='Banyaknya Rumah Sakit di Kota Surabaya',
                xaxis=dict(title='Jenis Rumah Sakit'),
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
        if x == 'donor-darah':
            graphs.append(donor_darah(x))
        elif x == 'rumah-sakit':
            graphs.append(rumah_sakit(x))
 
    return graphs