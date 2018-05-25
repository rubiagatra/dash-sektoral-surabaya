import pandas as pd 
import plotly.offline as pyo 
import plotly.graph_objs as go 


df = pd.read_csv("../data/hujansurabaya.csv", index_col="Bulan")
perak = df["Hari Hujan (Perak)"]
juanda = df["Hari Hujan (Juanda)"]
data1 = go.Scatter(x=df.index, y=perak, name="Stasiun Perak II", mode="lines+markers")
data2 = go.Scatter(x=df.index, y=juanda, name="Stasiun Juanda", mode="lines+markers")

data = [data1, data2]
layout = dict(title = "Jumlah Hari Hujan di Surabaya Tahun 2016",
              xaxis = dict(title = 'Bulan'),
              yaxis = dict(title = 'Hari Hujan'),
              )

fig = dict(data=data, layout=layout)
pyo.plot(fig, filename="2_hari_hujan.html")