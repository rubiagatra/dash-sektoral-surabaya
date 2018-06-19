import dash_core_components as dcc   
import plotly.graph_objs as go  
from dash.dependencies import Input, Output
import pandas as pd 

from apps import template
from app import app

APPS_NAME = 'pemerintahan'

dropdown_menu = dcc.Dropdown(id='data-input-' + APPS_NAME) 
pemerintahan_layout = template.template(APPS_NAME, dropdown_menu) 


@app.callback(
    Output('graphs-' + APPS_NAME, 'children'),
    [Input('data-input-' + APPS_NAME, 'value')],
)
def update_graph(data):
    pass