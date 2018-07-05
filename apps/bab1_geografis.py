import dash_core_components as dcc   
import dash_html_components as html
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'geografis'

df = pd.read_csv("data/Bab 1_Geografis_v2.0_2016.csv")

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME,
                            options=[{'label': 'Geografis: Rata - Rata Curah Hujan', 'value': 'curah-hujan'}, 
                                    {'label': 'Geografis: Jumlah Hari Hujan', 'value': 'hari-hujan'},
                                    {'label': 'Geografis: Kelembapan Udara', 'value': 'kelembapan-udara'},
                                    {'label': 'Geografis: Temperatur Udara', 'value': 'temperatur-udara'},
                                    {'label': 'Geografis: Tekanan Udara', 'value': 'tekanan-udara'},
                                    {'label': 'Geografis: Plot Interaktif', 'value': 'plot-interaktif'}],
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
    juanda_max = df['Maksimal Kelembaban (%) di Juanda']
    juanda_min = df['Minimal Kelembaban (%) di Juanda']
    perak = df["Rata-rata Kelembaban (%) di Tanjung Perak"]
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

def temperatur_udara(value_name: str):
    juanda_max = df['Maksimal Temperatur (Celcius)  di Juanda']
    juanda_min = df['Minimal Temperatur (Celcius)  di Juanda']
    perak = df["Rata-rata Temperatur (Celcius) di Tanjung Perak"]
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
    layout_juanda = dict(title='Temperatur Udara Stasiun Juanda 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Temperatur Udara (Celsius)'),
                )
    layout_perak = dict(title='Rata - rata Temperatur Udara Stasiun Perak 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Kelembapan Udara (Celsius)'),
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

def tekanan_udara(value_name: str):
    juanda_max = df['Maksimal Tekanan Udara (Mbs) di Juanda']
    juanda_min = df['Minimal Tekanan Udara (Mbs) di Juanda']
    perak = df['Rata-rata Tekanan Udara (Mbs) di Tanjung Perak']
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
    layout_juanda = dict(title='Tekanan Udara Stasiun Juanda 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Tekanan Udara (Mbs)'),
                )
    layout_perak = dict(title='Rata - rata Tekanan Udara Stasiun Perak 2016',
                xaxis=dict(title='Bulan'),
                yaxis=dict(title='Tekanan Udara (Celsius)'),
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

def scatter_plot(value_name: str):
    dropdown_options = [{'label': 'Hari Hujan (Juanda)', 'value': 'hari-hujan-juanda'},
                        {'label': 'Hari Hujan (Perak)', 'value': 'hari-hujan-perak'},
                        {'label': "Curah Hujan (Perak)", 'value': 'curah-hujan-perak'},
                        {'label': 'Curah Hujan (Juanda)', 'value': 'curah-hujan-juanda'},
                        ]
    x = dcc.Dropdown(id=value_name + "-x-" + APPS_NAME,
                            options=dropdown_options,
                            value='hari-hujan-juanda',
                            )
    y = dcc.Dropdown(id=value_name + "-y-" + APPS_NAME,
                            options=dropdown_options,
                            value='hari-hujan-perak',
                            )
    return [html.H2("Plot Interaktif"), x, y, dcc.Graph(id=value_name + "-" + APPS_NAME)]


@app.callback(
    Output('plot-interaktif-' + APPS_NAME, 'figure'),
    [Input('plot-interaktif-x-' + APPS_NAME, 'value'),
    Input('plot-interaktif-y-' + APPS_NAME, 'value')],
)
def update_interactive_graph(x_axis, y_axis):
    options = {
        'hari-hujan-perak': "Hari Hujan (Perak)",
        'hari-hujan-juanda': "Hari Hujan (Juanda)",
        'curah-hujan-perak': "Curah Hujan (Perak)" ,
        'curah-hujan-juanda': "Curah Hujan (Juanda)" 
    }
    data = go.Scatter(x=df[options[x_axis]], 
                                    y=df[options[y_axis]], 
                                    name="Plot Interaktif", 
                                    mode="markers",
                                    )
    data = [data]
    layout = dict(title='PLOT INTERAKTIF GEOGRAFIS',
                xaxis=dict(title=options[x_axis]),
                yaxis=dict(title=options[y_axis]),
                  )
    fig = dict(data=data, layout=layout)
    return fig


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
        elif x == 'temperatur-udara':
            graphs.extend(temperatur_udara(x))
        elif x == 'tekanan-udara':
            graphs.extend(tekanan_udara(x))
        elif x == 'plot-interaktif':
            graphs.extend(scatter_plot(x))
    return graphs