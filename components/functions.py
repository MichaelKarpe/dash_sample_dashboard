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
