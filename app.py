from dash import Dash
import dash_bootstrap_components as dbc

from pages.table import layout as table_layout


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = table_layout


if __name__ == "__main__":
    app.run(debug=True)