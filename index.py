import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import bab1_geografis, bab2_pemerintahan


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return bab1_geografis.geo_layout
    elif pathname == '/geografis':
        return bab1_geografis.geo_layout
    elif pathname == '/pemerintahan':
        return bab2_pemerintahan.pemerintahan_layout
        
    else:
        print(pathname)
        return '404'



if __name__ == '__main__':
    app.run_server(debug=True)