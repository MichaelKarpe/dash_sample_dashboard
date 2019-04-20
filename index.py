import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# see https://community.plot.ly/t/nolayoutexception-on-deployment-of-multi-page-dash-app-example-code/12463/2?u=dcomfort
from app import server
from app import app
from layouts import layout_datamining_category, noPage
import callbacks

import pandas as pd
import io
import xlsxwriter
from flask import send_file

# see https://dash.plot.ly/external-resources to alter header, footer and favicon
app.index_string = """ 
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>Data Mining Report</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>Data Mining Report</div>
    </body>
</html>
"""

app.layout = html.Div([dcc.Location(id="url", refresh=False), html.Div(id="page-content")])

# Update page
# # # # # # # # #
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if (
        pathname == "/cc-travel-report/"
        or pathname == "/cc-travel-report/overview-datamining"
        or pathname == "/cc-travel-report/overview-datamining/"
    ):
        return layout_datamining_category
    else:
        return noPage


# # # # # # # # #
# detail the way that external_css and external_js work and link to alternative method locally hosted
# # # # # # # # #
external_css = [
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
    "//fonts.googleapis.com/css?family=Raleway:400,300,600",
    "https://codepen.io/bcd/pen/KQrXdb.css",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "https://codepen.io/dmcomfort/pen/JzdzEZ.css",
]

for css in external_css:
    app.css.append_css({"external_url": css})

external_js = ["https://code.jquery.com/jquery-3.2.1.min.js", "https://codepen.io/bcd/pen/YaXojL.js"]

for js in external_js:
    app.scripts.append_script({"external_url": js})

if __name__ == "__main__":
    app.run_server(debug=True)
