import dash_html_components as html
import dash_core_components as dcc




def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        #src=app.get_asset_url("https://data.humdata.org/image/2015-11-05-231341.581365REACHlogo_300x125_grey.png"),
                        src="/assets/logo.png",
                        className="logo"
                    ),
                    html.A(
                        html.Button("Download Data", id="learn-more-button"),
                        href='https://www.iadb.org/en',
                    ),
                ],
                className="rowheader",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("General Report Prototype")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header



def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Overview",
                href="/report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Associations",
                href="/report/pageOne",
                className="tab",
            ),
            dcc.Link(
                "Model evaluation",
                href="/report/pageTwo",
                className="tab",
            ),
            dcc.Link(
                "Model interpretation", 
                href="/report/pageThree", 
                className="tab"
            ),
            dcc.Link(
                "Methodology",
                href="/report/pageFour",
                className="tab",
            ),
            dcc.Link(
                "Contact",
                href="/report/pageFive",
                className="tab",
            ),
            dcc.Link(
                "Appendix",
                href="/report/pageSix",
                className="tab",
            )
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table