import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import bab1_geografis, bab2_pemerintahan, bab3_penduduk, bab4_sosial, bab5_pertanian
from apps import bab6_industri, bab7_perdagangan 


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
    elif pathname == '/penduduk':
        return bab3_penduduk.penduduk_layout
    elif pathname == '/sosial':
        return bab4_sosial.sosial_layout
    elif pathname == '/pertanian': 
        return bab5_pertanian.pertanian_layout
    elif pathname == '/industri': 
        return bab6_industri.industri_layout
    elif pathname == '/perdagangan': 
        return bab7_perdagangan.perdagangan_layout
    else:
        print(pathname)
        return '404'



if __name__ == '__main__':
    app.run_server(debug=True, port=8051)

