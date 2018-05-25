import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 


df = pd.read_csv("../data/hujansurabaya.csv", index_col="Bulan")
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
pyo.plot(fig, filename="1_curah_hujan.html")