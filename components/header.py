import dash_html_components as html
import dash_core_components as dcc


def Header():
    return html.Div([get_logo(), get_header(), html.Br([]), get_menu()])


def get_logo():
    logo = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src="https://i.pinimg.com/564x/4a/bc/38/4abc38758eba60d6712bd86dd1542697.jpg",
                        height="101",
                        width="141",
                    )
                ],
                className="ten columns padded",
            ),
            # html.Div([
            #     dcc.Link('Full View   ', href='/cc-travel-report/full-view')
            # ], className="two columns page-view no-print")
        ],
        className="row gs-header",
    )
    return logo


def get_header():
    header = html.Div(
        [html.Div([html.H5("Data Mining Report")], className="twelve columns padded")],
        className="row gs-header gs-text-header",
    )
    return header


def get_menu():
    menu = html.Div(
        [dcc.Link("Overview", href="/cc-travel-report/overview-datamining/", className="tab first")], className="row "
    )
    return menu
