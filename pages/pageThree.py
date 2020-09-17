# Internal modules
from processing.data_management import load_excel, load_document
import processing.preprocessors as pp
from config import config
from graphs import graphs

# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
#import geopandas as gpd

from utils import Header, make_dash_table
import pandas as pd
import numpy as np
import pathlib

from dash.dependencies import Input,Output
import json
import docx


df = load_excel(file_name=config.DATA_FILE)
model_coefficients = load_excel(file_name='logistic_model_coefficients.xlsx')
y_pred = load_excel(file_name='predicted_probabilities.xlsx')
########## TEMPORARY MAP DETAILS ######

mapbox_token = 'pk.eyJ1IjoiY2F3aWUiLCJhIjoiY2s1cGVsN3U3MHVrYTNsbnNpd3pubGR3ZSJ9.5sgCAI1IM9pOmmk4dZeD4Q'



def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Global Model Interpretation", style={"padding-left": "10px"}), className="inner-product2"),
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
                                [html.H6(["Model coefficient by outcome class (poverty level)"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(id='ass', figure=graphs.barchart_multi(model_coefficients.T)),
                                ],
                                className="eight columns",
                            ),
                        ],
                        className="row "
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Graph 3", 
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p2',
                                        figure = None)
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Graph 4",
                                        className="subtitle padded",
                                    )
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ), 
        ],
        className="page",
    ), html.Div(
        [
            ##########
            ########## NEW PAGE #########
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Div(html.H5("Local Model Interpretation", style={"padding-left": "10px"}), className="inner-product2"),
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
                                [html.H6(["Instance specific model explanation. (i.e. Why did it predict this poverty level for that household?"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(id='ass', figure=graphs.interpret()),
                                ],
                                className="eight columns",
                            ),
                        ],
                        className="row "
                    ),
                     # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Graph 8"], 
                                        className="subtitle padded"
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Graph 4",
                                        className="subtitle padded",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                ],
                className="sub_page",
            ), 
        ],
        className="page",
    )