import pandas as pd
from dash import dash_table, dcc, html
import dash_bootstrap_components as dbc


DATA_PATH = "datas/avocado.csv"
df = pd.read_csv(DATA_PATH)

region_options = sorted(df["region"].dropna().unique())
type_options = sorted(df["type"].dropna().unique())

hidden_columns = {
    "Unnamed: 0",
    "4046",
    "4225",
    "4770",
    "Small Bags",
    "Large Bags",
    "XLarge Bags",
}

visible_columns = [col for col in df.columns if col not in hidden_columns]

layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Selectionner une region :", style={"marginBottom": "6px"}),
                        dcc.Dropdown(
                            id="region-dropdown",
                            options=[{"label": region, "value": region} for region in region_options],
                            value=region_options[0] if region_options else None,
                            placeholder="Selectionner une region",
                            clearable=False,
                        ),
                    ],
                    style={"flex": "1 1 300px", "minWidth": "240px"},
                ),
                html.Div(
                    [
                        html.Label("Selectionner un type :", style={"marginBottom": "6px"}),
                        dcc.Dropdown(
                            id="type-dropdown",
                            options=[{"label": "Tous", "value": "__all__"}]
                            + [{"label": avocado_type, "value": avocado_type} for avocado_type in type_options],
                            value="__all__",
                            placeholder="Selectionner un type",
                            clearable=False,
                        ),
                    ],
                    style={"flex": "1 1 300px", "minWidth": "240px"},
                ),
            ],
            style={
                "display": "flex",
                "gap": "12px",
                "flexWrap": "wrap",
                "marginBottom": "16px",
            },
        ),
        dash_table.DataTable(
            id="avocado-table",
            columns=[{"name": col, "id": col} for col in visible_columns],
            data=df[visible_columns].to_dict("records"),
            page_size=12,
            style_table={"overflowX": "auto"},
            style_cell={"textAlign": "left", "padding": "8px"},
            style_header={
                "fontWeight": "bold",
                "backgroundColor": "#167ee6",
                "color": "white",
                "border": "1px solid #167ee6",
            },
            style_data_conditional=[
                {
                    "if": {"row_index": "odd"},
                    "backgroundColor": "#efefef",
                }
            ],
        ),
    ],
    fluid=True,
)

