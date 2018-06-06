import dash_core_components as dcc   
import dash_html_components as html 
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from app import app

df = pd.read_csv('data/hujansurabaya.csv')

geo_layout = html.Div([
    html.H2('DATA SEKTORAL SURABAYA', 
                style={'display': 'inline',
                       'float': 'left',
                       'font-size': '3.65em',
                       'margin-left': '7px',
                       'font-weight': 'bolder',
                       'font-family': 'Product Sans',
                       'color': "rgba(117, 117, 117, 0.95)",
                       'margin-top': '20px',
                       'margin-bottom': '0',
                        }),
    html.Img(src="https://i.imgur.com/Glih9lH.png",
                style={
                    'height': '100px',
                    'float': 'right',
                    'margin-bottom': '10px',
                }),
    dcc.Dropdown(
        id='data-input',
        options=[{'label': 'Curah Hujan', 'value': 'curah-hujan'}, {'label': 'Hari Hujan', 'value': 'hari-hujan'}],
        value='curah-hujan',
    ),
    html.Div(id='graphs')   
], className='container')

def curah_hujan():
    perak = df["Curah Hujan (Perak)"]
    juanda = df["Curah Hujan (Juanda)"] 
    data1 = go.Scatter(x=df.index, y=perak, name="Stasiun Perak II", mode="lines+markers")
    data2 = go.Scatter(x=df.index, y=juanda, name="Stasiun Juanda", mode="lines+markers")
    data = [data1, data2]
    layout = dict(title = 'Rata Rata Curah Hujan di Surabaya Tahun 2016',
                xaxis = dict(title = 'Bulan'),
                yaxis = dict(title = 'Curah Hujan (mm)'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id='curah',
        figure=fig,
    )

def hari_hujan():
    perak = df["Hari Hujan (Perak)"]
    juanda = df["Hari Hujan (Juanda)"]
    data1 = go.Scatter(x=df.index, y=perak, name="Stasiun Perak II", mode="lines+markers")
    data2 = go.Scatter(x=df.index, y=juanda, name="Stasiun Juanda", mode="lines+markers")
    data = [data1, data2]
    layout = dict(title = 'Jumlah Hari Hujan di Surabaya Tahun 2016',
                xaxis = dict(title = 'Bulan'),
                yaxis = dict(title = 'Jumlah Hari Hujan'),
                  )
    fig = dict(data=data, layout=layout)
    return dcc.Graph(
        id='curah',
        figure=fig,
    )

@app.callback(
    Output('graphs', 'children'),
    [Input('data-input', 'value')],
)
def update_graph(data):
    if data == 'curah-hujan':
        return curah_hujan()
    elif data == 'hari-hujan':
        return hari_hujan()