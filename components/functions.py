from datetime import datetime as dt
from datetime import date, timedelta
from datetime import datetime
import plotly.graph_objs as go
from plotly import tools
import numpy as np
import pandas as pd

pd.options.mode.chained_assignment = None

df = pd.read_csv("data/performance_analytics_cost_and_ga_metrics.csv")
df["Date"] = pd.to_datetime(df["Date"])

now = datetime.now()
datestamp = now.strftime("%Y%m%d")


# Data Table Update Function
def update_datatable(start_date, end_date):
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)].to_dict("rows")


# Data Table Download Function
def update_download(start_date, end_date):
    return df[(start_date <= df["Date"]) & (df["Date"] <= end_date)]


######################## FOR GRAPHS  ########################


def update_graph(filtered_df, end_date):
    # Sessions Graphs
    sessions_scatter = go.Scatter(
        x=filtered_df["Travel Product"], y=filtered_df["Sessions - This Year"], text="Sessions - This Year"
    )
    sessions_bar = go.Bar(
        x=filtered_df["Travel Product"], y=filtered_df["Sessions - This Year"], text="Sessions - This Year", opacity=0.6
    )

    fig = tools.make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=("Line Chart", "Bar Chart"),  # Be sure to have same number of titles as number of graphs
    )

    fig.append_trace(sessions_scatter, 1, 1)  # 0
    fig.append_trace(sessions_bar, 2, 1)  # 1

    # integer index below is the index of the trace
    # yaxis indices below need to start from the number of total graphs + 1 since they are on right-side
    # overlaing and anchor axes correspond to the graph number

    fig["layout"]["xaxis"].update(title="Travel Product")
    for i in fig["layout"]["annotations"]:
        i["font"] = dict(
            size=12,
            # color='#ff0000'
        )
    fig["layout"].update(
        height=500,
        # width=750,
        showlegend=False,
        xaxis=dict(
            # tickmode='linear',
            # ticks='outside',
            # tick0=1,
            dtick=5,
            ticklen=8,
            tickwidth=2,
            tickcolor="#000",
            showgrid=True,
            zeroline=True,
            # showline=True,
            # mirror='ticks',
            # gridcolor='#bdbdbd',
            gridwidth=2,
        ),
    )
    updated_fig = fig
    return updated_fig
