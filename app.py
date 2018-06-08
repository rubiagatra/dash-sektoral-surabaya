import dash

app = dash.Dash("Data Sektoral Surabaya")
server = app.server
app.config.suppress_callback_exceptions = True

external_css = ["https://fonts.googleapis.com/css?family=Product+Sans:400,400i,700,700i",
                "https://cdn.rawgit.com/plotly/dash-app-stylesheets/2cc54b8c03f4126569a3440aae611bbef1d7a5dd/stylesheet.css",
                "https://codepen.io/bcd/pen/KQrXdb.css"]

for css in external_css:
    app.css.append_css({"external_url": css})
