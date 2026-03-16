from dash import Input, Output

from pages.compare import build_region_figure, default_region_1, default_region_2, df


def register_compare_callbacks(app):
    @app.callback(
        Output("compare-graph-1", "figure"),
        Output("compare-graph-2", "figure"),
        Input("compare-region-1-dropdown", "value"),
        Input("compare-region-2-dropdown", "value"),
    )
    def update_compare_graphs(selected_region_1, selected_region_2):
        region_1 = selected_region_1 or default_region_1
        region_2 = selected_region_2 or default_region_2

        fig_1 = build_region_figure(region_1)
        fig_2 = build_region_figure(region_2)

        compared_prices = df[df["region"].isin([region_1, region_2])]["AveragePrice"]

        if not compared_prices.empty:
            y_min = float(compared_prices.min())
            y_max = float(compared_prices.max())
            padding = (y_max - y_min) * 0.05 if y_max > y_min else 0.1
            shared_range = [y_min - padding, y_max + padding]
            fig_1.update_yaxes(range=shared_range)
            fig_2.update_yaxes(range=shared_range)

        return fig_1, fig_2
