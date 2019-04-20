import dash_core_components as dcc
import dash_html_components as html
import dash_table
from components import df, Header, print_button
from datetime import datetime as dt
from datetime import date, timedelta
import pandas as pd


df["Date"] = pd.to_datetime(df["Date"])
current_year = df["Date"].apply(lambda x: x.year).max()

dt_columns = list(df.columns)

######################## START Datamining Category Layout ########################
layout_datamining_category = html.Div(
    [
        #    print_button(),
        html.Div(
            [
                # CC Header
                Header(),
                # Date Picker
                html.Div(
                    [
                        dcc.DatePickerRange(
                            id="my-date-picker-range-datamining-category",
                            # with_portal=True,
                            min_date_allowed=dt(2018, 1, 1),
                            max_date_allowed=df["Date"].max().to_pydatetime(),
                            initial_visible_month=dt(current_year, df["Date"].max().to_pydatetime().month, 1),
                            start_date=(df["Date"].max() - timedelta(6)).to_pydatetime(),
                            end_date=df["Date"].max().to_pydatetime(),
                        ),
                        html.Div(id="output-container-date-picker-range-datamining-category"),
                    ],
                    className="row ",
                    style={"marginTop": 30, "marginBottom": 15},
                ),
                # Header Bar
                html.Div(
                    [
                        html.H6(
                            ["Datamining Level Metrics"],
                            className="gs-header gs-text-header padded",
                            style={"marginTop": 15},
                        )
                    ]
                ),
                # Radio Button
                html.Div(
                    [
                        dcc.RadioItems(
                            options=[
                                {"label": "Condensed Data Table", "value": "Condensed"},
                                {"label": "Complete Data Table", "value": "Complete"},
                            ],
                            value="Condensed",
                            labelStyle={
                                "display": "inline-block",
                                "width": "20%",
                                "margin": "auto",
                                "marginTop": 15,
                                "paddingLeft": 15,
                            },
                            id="radio-button-datamining-category",
                        )
                    ]
                ),
                # First Data Table
                html.Div(
                    [
                        dash_table.DataTable(
                            id="datatable-datamining-category",
                            columns=[{"name": i, "id": i, "deletable": True} for i in dt_columns],
                            editable=True,
                            filtering=True,
                            sorting=True,
                            # sorting_type="multi",
                            row_selectable="multi",
                            row_deletable=True,
                            selected_rows=[0],
                            n_fixed_columns=2,
                            style_table={"maxWidth": "1500px"},
                            style_cell={
                                "fontFamily": "Arial",
                                "size": 10,
                                "textAlign": "left",
                                "whiteSpace": "no-wrap",
                                "overflow": "hidden",
                                "textOverflow": "ellipsis",
                                "maxWidth": "500px",
                            },
                            css=[
                                {
                                    "selector": ".dash-cell div.dash-cell-value",
                                    "rule": "display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;",
                                }
                            ],
                            pagination_mode="fe",
                            pagination_settings={"displayed_pages": 1, "current_page": 0, "page_size": 10},
                            navigation="page",
                        )
                    ],
                    className=" twelve columns",
                ),
                # Download Button
                html.Div(
                    [html.A(html.Button("Download Data", id="download-button"), id="download-link-datamining-category")]
                ),
                # GRAPHS
                html.Div(
                    [
                        html.Div(id="update_graph"),
                        html.Div([dcc.Graph(id="datamining-category")], className=" twelve columns"),
                    ],
                    className="row ",
                ),
            ],
            className="subpage",
        )
    ],
    className="page",
)

######################## END Datamining Category Layout ########################

######################## 404 Page ########################
noPage = html.Div(
    [
        # CC Header
        Header(),
        html.P(["404 Page not found"]),
    ],
    className="no-page",
)
