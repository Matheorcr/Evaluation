from pathlib import Path

from dash import dcc, html
import dash_bootstrap_components as dbc


def read_markdown_file(file_path):
    path = Path(file_path)
    return path.read_text(encoding="utf-8") if path.exists() else f"Fichier introuvable: {file_path}"


layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(
                    html.H1("Présentation de Dash", className="markdown-hero-title"),
                    className="markdown-hero",
                ),
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            dcc.Markdown(read_markdown_file("expli1.md"), className="markdown-content"),
                            title="Accueil",
                            item_id="accueil",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_markdown_file("expli2.md"), className="markdown-content"),
                            title="Layout",
                            item_id="layout",
                        ),
                        dbc.AccordionItem(
                            dcc.Markdown(read_markdown_file("expli3.md"), className="markdown-content"),
                            title="CallBack",
                            item_id="callback",
                        ),
                    ],
                    active_item="layout",
                    start_collapsed=True,
                    always_open=False,
                    className="markdown-accordion",
                ),
            ],
            className="markdown-shell",
        ),
    ],
    fluid=True,
    className="markdown-page",
)
