# Internal modules
from processing.data_management import load_excel, load_document
import processing.preprocessors as pp
from config import config
from graphs import graphs

# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table
import pandas as pd
import numpy as np
import pathlib

from dash.dependencies import Input,Output
import json
import docx


df = load_excel(file_name=config.DATA_FILE)
########## TEMPORARY MAP DETAILS ######

mapbox_token = 'pk.eyJ1IjoiY2F3aWUiLCJhIjoiY2s1cGVsN3U3MHVrYTNsbnNpd3pubGR3ZSJ9.5sgCAI1IM9pOmmk4dZeD4Q'



def create_layout(app):
    # Page layouts
    return html.Div(
        [
            #html.Div([Header(app)]),
            Header(app),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Housing Characteristics", style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one',
                                        figure = graphs.barchart(x1 = df['Target'].value_counts().index, y1 = df['Target'].value_counts().values))
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Rent",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-two',
                                        figure = graphs.linechart(df[(df['v2a1']>0) & (df['v2a1']<500000)]['v2a1']))
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Number of rooms"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-four',
                                        figure = graphs.barchart(x1 = df['rooms'].value_counts().index, y1 = df['rooms'].value_counts().values))
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Level of overcrowding",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='hover-data2',
                                        figure = graphs.linechart(np.sqrt(df['SQBovercrowding'])))
                                ],
                                className="six columns",
                            ),

                        ],
                        className="row",
                        style={"margin-bottom": "0px"},

                    )

                ],
                className="sub_page"
                )
            ],
            className="page"
        ), html.Div(
        [
            #html.Div([Header(app)]), #################### PAGE TWO #######################
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Housing characteristics", style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Quality of walls"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seventeen',
                                        figure = graphs.barchart(
                                            x1 = df['walls'].value_counts().index, 
                                            y1 = df['walls'].value_counts().values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Quality of ceiling",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eighteen',
                                        figure = graphs.barchart(
                                            x1=df['cielorazo'].value_counts().index, 
                                            y1=df['cielorazo'].value_counts().values)

                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Quality of roof"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.barchart(
                                            x1=df['roof'].value_counts().index, 
                                            y1=df['roof'].value_counts().values)
                                        )
                                ],
                                className="six columns",
                            )
                        ],
                        className="row",
                        style={"margin-bottom": "0px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    ),html.Div(
        [
            #html.Div([Header(app)]), #################### PAGE THREE #######################
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Household characteristics", style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Number of children aged 0-12"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-five',
                                        figure = graphs.barchart(
                                            x1 = df['r4t1'].value_counts().index, 
                                            y1 = df['r4t1'].value_counts().values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Number of persons 0-19",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-six',
                                        figure = graphs.barchart(
                                            x1 = np.sqrt(df['SQBhogar_nin']).value_counts().index, 
                                            y1 = np.sqrt(df['SQBhogar_nin']).value_counts().values,
                                            )

                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Dependency Ratio"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seven',
                                        figure = graphs.linechart(df['dependency'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Minimum and Maximum Age",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eight',
                                        figure = graphs.linechart2(
                                            x1 = df['age-min'].value_counts().sort_index().index, 
                                            y1 = df['age-min'].value_counts().sort_index().values,
                                            x2 = df['age-max'].value_counts().sort_index().index, 
                                            y2 = df['age-max'].value_counts().sort_index().values)
                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "0px"},
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    ), html.Div(
        [
            #html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Household characteristics", style={"padding-left": "10px"}), className="inner-product2"),
                                    html.Br([]),
                                    html.P(load_document(config.TEXT_FILE),
                                        style={"color": "#000000"},
                                        className="row",
                                    ),
                                ],
                                className="product2",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Head of household education"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eleven',
                                        figure = graphs.barchart(
                                            x1 = np.sqrt(df['SQBedjefe']).value_counts().index, 
                                            y1 = np.sqrt(df['SQBedjefe']).value_counts().values,
                                            x2 = df['edjefa'].value_counts().index, 
                                            y2 = df['edjefa'].value_counts().values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Minimum and Maximum years of schooling",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-twelve',
                                        figure = graphs.linechart2(
                                            x1 = df['escolari-min'].value_counts().sort_index().index, 
                                            y1 = df['escolari-min'].value_counts().sort_index().values,
                                            x2 = df['escolari-max'].value_counts().sort_index().index, 
                                            y2 = df['escolari-max'].value_counts().sort_index().values)

                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Highest level of completed education",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-fourteen',
                                        figure = graphs.barchart2(
                                            x1 = df['instlevel1-sum'].value_counts().index, 
                                            y1 = df['instlevel1-sum'].value_counts().values,
                                            x2 = df['instlevel2-sum'].value_counts().index, 
                                            y2 = df['instlevel2-sum'].value_counts().values,
                                            x3 = df['instlevel8-sum'].value_counts().index, 
                                            y3 = df['instlevel8-sum'].value_counts().values)
                                        )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "0px"},
                    ),
                    #html.Div(
                    #    [
                    #        html.Div(
                    #            [
                    #                html.H6(
                    #                    ["Graph 15"], className="subtitle padded"
                    #                ),
                    #                dcc.Graph(
                    #                    id = 'graph-fifteen',
                    #                    figure = None
                    #                    )
                    #            ],
                    #            className="six columns",
                    #        ),
                    #        html.Div(
                    #            [
                    #                html.H6(
                    #                    "Graph 16",
                    #                    className="subtitle padded",
                    #                ),
                    #                dcc.Graph(
                    #                    id = 'graph-sixteen',
                    #                    figure = None
                    #                    )
                    #            ],
                    #            className="six columns",
                    #        ),
                    #    ],
                    #    className="row",
                    #    style={"margin-bottom": "0px"},
                    #),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )


