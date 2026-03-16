from dash import Dash
import dash_bootstrap_components as dbc

from pages.compare_cb import register_compare_callbacks
from pages.markdown import layout as markdown_layout




app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server


app.layout = markdown_layout
# register_compare_callbacks(app)


if __name__ == "__main__":
    app.run(debug=True)