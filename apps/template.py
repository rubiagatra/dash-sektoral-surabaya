import dash_html_components as html  
import dash_core_components as dcc    


def template(template_name: str, dropdown_menu):
    return html.Div([
        html.H2('DATA SEKTORAL SURABAYA 2017', 
                    style={"display": "inline",
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
        html.Div([
            dcc.Link('Geografis', href='/geografis', className="tab first"),
            dcc.Link('Pemerintahan', href='/pemerintahan', className="tab"),
            dcc.Link('Penduduk', href='/penduduk', className="tab"),
            dcc.Link('Sosial', href='/sosial', className="tab"),
            dcc.Link('Pertanian', href='/pertanian', className="tab"),
            dcc.Link('Industri', href='/industri', className="tab"),
            dcc.Link('Perdagangan', href='/perdagangan', className="tab"),
            dcc.Link('Transportasi', href='/transportasi', className="tab"),
            dcc.Link('Keuangan', href='/keuangan', className="tab"),
            dcc.Link('Pendapatan', href='/pendaptan', className="tab"),
            ], className="row ", style={"display": "block", "margin-top":"30", "margin-bottom": "10px", "textAlign": "center"}),
        dropdown_menu,
        html.Div(id='graphs-' + template_name)   
    ], className='container')