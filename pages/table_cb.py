from dash import Input, Output

from pages.table import df, visible_columns


def register_callbacks(app):
    @app.callback(
        Output("avocado-table", "data"),
        Input("region-dropdown", "value"),
        Input("type-dropdown", "value"),
    )
    def filter_table(selected_region, selected_type):
        filtered_df = df.copy()

        if selected_region:
            filtered_df = filtered_df[filtered_df["region"] == selected_region]

        if selected_type and selected_type != "__all__":
            filtered_df = filtered_df[filtered_df["type"] == selected_type]

        return filtered_df[visible_columns].to_dict("records")
