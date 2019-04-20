from dash.dependencies import Input, Output
from app import app
import plotly.graph_objs as go
from plotly import tools

from datetime import datetime as dt
from datetime import date, timedelta
from datetime import datetime

import numpy as np
import pandas as pd

import io
import xlsxwriter
import flask
from flask import send_file

from components import df, update_datatable, update_download


pd.options.mode.chained_assignment = None


now = datetime.now()
datestamp = now.strftime("%Y%m%d")

columns_complete = list(df.columns)
columns_condensed = ["Date", "Travel Product", "Sessions - This Year"]

######################## Datamining Category Callbacks ########################

#### Date Picker Callback
@app.callback(
    Output("output-container-date-picker-range-datamining-category", "children"),
    [
        Input("my-date-picker-range-datamining-category", "start_date"),
        Input("my-date-picker-range-datamining-category", "end_date"),
    ],
)
def update_output(start_date, end_date):
    string_prefix = "You have selected "
    if start_date is not None:
        start_date = dt.strptime(start_date, "%Y-%m-%d")
        start_date_string = start_date.strftime("%B %d, %Y")
        string_prefix = string_prefix + "a Start Date of " + start_date_string + " | "
    if end_date is not None:
        end_date = dt.strptime(end_date, "%Y-%m-%d")
        end_date_string = end_date.strftime("%B %d, %Y")
        days_selected = (end_date - start_date).days
        prior_start_date = start_date - timedelta(days_selected + 1)
        prior_start_date_string = datetime.strftime(prior_start_date, "%B %d, %Y")
        prior_end_date = end_date - timedelta(days_selected + 1)
        prior_end_date_string = datetime.strftime(prior_end_date, "%B %d, %Y")
        string_prefix = (
            string_prefix
            + "End Date of "
            + end_date_string
            + ", for a total of "
            + str(days_selected + 1)
            + " Days. The prior period Start Date was "
            + prior_start_date_string
            + " | End Date: "
            + prior_end_date_string
            + "."
        )
    if len(string_prefix) == len("You have selected: "):
        return "Select a date to see it displayed here"
    else:
        return string_prefix


# Callback and update first data table
@app.callback(
    Output("datatable-datamining-category", "data"),
    [
        Input("my-date-picker-range-datamining-category", "start_date"),
        Input("my-date-picker-range-datamining-category", "end_date"),
    ],
)
def update_data_1(start_date, end_date):
    data_1 = update_datatable(start_date, end_date)
    return data_1


# Callback and update data table columns
@app.callback(Output("datatable-datamining-category", "columns"), [Input("radio-button-datamining-category", "value")])
def update_columns(value):
    if value == "Complete":
        column_set = [{"name": i, "id": i, "deletable": True} for i in columns_complete]
    elif value == "Condensed":
        column_set = [{"name": i, "id": i, "deletable": True} for i in columns_condensed]
    return column_set


# Callback for excel download
@app.callback(
    Output("download-link-datamining-category", "href"),
    [
        Input("my-date-picker-range-datamining-category", "start_date"),
        Input("my-date-picker-range-datamining-category", "end_date"),
    ],
)
def update_link(start_date, end_date):
    return "/cc-travel-report/datamining-category/urlToDownload?value={}/{}".format(
        dt.strptime(start_date, "%Y-%m-%d").strftime("%Y-%m-%d"), dt.strptime(end_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    )


@app.server.route("/cc-travel-report/datamining-category/urlToDownload")
def download_excel_datamining_category():
    value = flask.request.args.get("value")
    # here is where I split the value
    value = value.split("/")
    start_date = value[0]
    end_date = value[1]

    filename = datestamp + "_datamining_category_" + start_date + "_to_" + end_date + ".xlsx"
    # Dummy Dataframe
    d = {"col1": [1, 2], "col2": [3, 4]}
    df = pd.DataFrame(data=d)

    buf = io.BytesIO()
    excel_writer = pd.ExcelWriter(buf, engine="xlsxwriter")
    download_1 = update_download(start_date, end_date)
    download_1.to_excel(excel_writer, sheet_name="sheet1", index=False)
    # df.to_excel(excel_writer, sheet_name="sheet1", index=False)
    excel_writer.save()
    excel_data = buf.getvalue()
    buf.seek(0)

    return send_file(
        buf,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        attachment_filename=filename,
        as_attachment=True,
        cache_timeout=0,
    )
