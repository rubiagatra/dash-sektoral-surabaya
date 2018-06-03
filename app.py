import dash
import dash_core_components as dcc   
import dash_html_components as html 
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

app = dash.Dash()
df = pd.read_csv('data/hujansurabaya.csv')

app.layout = html.Div([
    html.H2('Data Sektoral Surabaya', 
                style={'display': 'inline',
                       'float': 'left',
                       'font-size': '2.65em',
                       'margin-left': '7px',
                       'font-weight': 'bolder',
                       'font-family': 'Product Sans',
                       'color': "rgba(117, 117, 117, 0.95)",
                       'margin-top': '20px',
                       'margin-bottom': '0',
                        }),
    html.Img(src="https://pbs.twimg.com/profile_images/915741980814041088/eyoxOz9v_400x400.jpg",
                style={
                    'height': '100px',
                    'float': 'right'
                }),
    dcc.Dropdown(
        id='data-input',
        options=[{'label': 'Curah Hujan', 'value': 'curah-hujan'}, {'label': 'Jumlah Hujan', 'value': 'jumlah-hujan'}],
        value=['curah-hujan'],
        multi=True
    ),
    html.Div(id='graphs')   
], className='container')

external_css = ["https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2cc54b8c03f4126569a3440aae611bbef1d7a5dd/stylesheet.css"]

for css in external_css:
    app.css.append_css({"external_url": css})


if __name__ == "__main__":
    app.run_server(debug=True)