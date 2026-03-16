import pandas as pd
import plotly.express as px
from dash import dcc, html
import dash_bootstrap_components as dbc


DATA_PATH = "datas/avocado.csv"
df = pd.read_csv(DATA_PATH)
df["Date"] = pd.to_datetime(df["Date"])

region_options = sorted(df["region"].dropna().unique())

default_region_1 = region_options[0] if region_options else None
default_region_2 = region_options[1] if len(region_options) > 1 else default_region_1


def build_region_figure(selected_region):
    filtered_df = df[df["region"] == selected_region].sort_values("Date")
    figure = px.line(
        filtered_df,
        x="Date",
        y="AveragePrice",
        title=f"Prix moyen dans le temps - {selected_region}",
    )
    figure.update_traces(line={"color": "#6b7cff", "width": 2})
    figure.update_layout(
        margin=dict(l=20, r=20, t=55, b=20),
        paper_bgcolor="#ffffff",
        plot_bgcolor="#ffffff",
        title_font={"size": 14},
        font={"size": 12, "color": "#3d4f67"},
    )
    figure.update_xaxes(gridcolor="#e8edf4")
    figure.update_yaxes(gridcolor="#e8edf4")
    return figure


layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    "Prix moyen dans le temps",
                    style={
                        "backgroundColor": "#167ee6",
                        "color": "white",
                        "fontSize": "30px",
                        "fontWeight": "500",
                        "padding": "8px 14px",
                        "borderRadius": "4px 4px 0 0",
                        "marginBottom": "12px",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Span(
                                    "Region 1 :",
                                    style={
                                        "display": "inline-block",
                                        "backgroundColor": "#12b8dd",
                                        "color": "white",
                                        "fontWeight": "600",
                                        "fontSize": "13px",
                                        "padding": "3px 10px",
                                        "borderRadius": "999px",
                                        "marginBottom": "8px",
                                    },
                                ),
                                dcc.Dropdown(
                                    id="compare-region-1-dropdown",
                                    options=[{"label": region, "value": region} for region in region_options],
                                    value=default_region_1,
                                    clearable=False,
                                ),
                            ],
                            style={"flex": "1 1 360px", "minWidth": "280px"},
                        ),
                        html.Div(
                            [
                                html.Span(
                                    "Region 2 :",
                                    style={
                                        "display": "inline-block",
                                        "backgroundColor": "#12b8dd",
                                        "color": "white",
                                        "fontWeight": "600",
                                        "fontSize": "13px",
                                        "padding": "3px 10px",
                                        "borderRadius": "999px",
                                        "marginBottom": "8px",
                                    },
                                ),
                                dcc.Dropdown(
                                    id="compare-region-2-dropdown",
                                    options=[{"label": region, "value": region} for region in region_options],
                                    value=default_region_2,
                                    clearable=False,
                                ),
                            ],
                            style={"flex": "1 1 360px", "minWidth": "280px"},
                        ),
                    ],
                    style={
                        "display": "flex",
                        "gap": "14px",
                        "flexWrap": "wrap",
                        "marginBottom": "12px",
                    },
                ),
                html.Div(
                    [
                        html.Div(
                            dcc.Graph(
                                id="compare-graph-1",
                                figure=build_region_figure(default_region_1),
                                config={"displayModeBar": False},
                            ),
                            style={
                                "flex": "1 1 420px",
                                "minWidth": "300px",
                                "backgroundColor": "#ffffff",
                                "border": "1px solid #d9e0eb",
                                "borderRadius": "4px",
                                "padding": "6px",
                            },
                        ),
                        html.Div(
                            dcc.Graph(
                                id="compare-graph-2",
                                figure=build_region_figure(default_region_2),
                                config={"displayModeBar": False},
                            ),
                            style={
                                "flex": "1 1 420px",
                                "minWidth": "300px",
                                "backgroundColor": "#ffffff",
                                "border": "1px solid #d9e0eb",
                                "borderRadius": "4px",
                                "padding": "6px",
                            },
                        ),
                    ],
                    style={
                        "display": "flex",
                        "gap": "14px",
                        "flexWrap": "wrap",
                    },
                ),
            ],
            style={
                "backgroundColor": "#f0f2f5",
                "border": "1px solid #d5d9df",
                "borderRadius": "4px",
                "padding": "10px",
            },
        ),
    ],
    fluid=True,
    style={"paddingTop": "10px"},
)
