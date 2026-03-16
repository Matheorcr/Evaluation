from dash import Dash, Input, Output, dcc, html
import dash_bootstrap_components as dbc

from pages.compare_cb import register_compare_callbacks
from pages.markdown import layout as markdown_layout
from pages.compare import layout as compare_layout
from pages.table import layout as table_layout
from pages.table_cb import register_callbacks as register_table_callbacks

app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
server = app.server

app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(
            [
                html.Div("Application des M2 MECEN", className="dashboard-title"),
                html.Div(
                    [
                        dcc.Link("Affichage des données", href="/", id="nav-data", className="dashboard-nav-link"),
                        dcc.Link(
                            "Comparaison entre region",
                            href="/compare",
                            id="nav-compare",
                            className="dashboard-nav-link",
                        ),
                        dcc.Link("Aide en ligne", href="/help", id="nav-help", className="dashboard-nav-link"),
                    ],
                    className="dashboard-nav",
                ),
            ],
            className="dashboard-topbar",
        ),
        html.Div(html.Div(id="page-content", className="dashboard-page-content"), className="dashboard-content"),
    ],
    className="dashboard-shell",
)


@app.callback(
    Output("page-content", "children"),
    Output("nav-data", "className"),
    Output("nav-compare", "className"),
    Output("nav-help", "className"),
    Input("url", "pathname"),
)
def render_page(pathname):
    if pathname == "/compare":
        return compare_layout, "dashboard-nav-link", "dashboard-nav-link active", "dashboard-nav-link"
    if pathname == "/help":
        return markdown_layout, "dashboard-nav-link", "dashboard-nav-link", "dashboard-nav-link active"
    return table_layout, "dashboard-nav-link active", "dashboard-nav-link", "dashboard-nav-link"


register_table_callbacks(app)
register_compare_callbacks(app)


if __name__ == "__main__":
    app.run(debug=True)