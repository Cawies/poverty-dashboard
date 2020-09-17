# Internal modules
from processing.data_management import load_excel, load_excel, load_document
import processing.preprocessors as pp
from config import config
from graphs import graphs

# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
#import geopandas as gpd

from utils import Header, make_dash_table
import pandas as pd
import numpy as np
import pathlib

from dash.dependencies import Input,Output
import json
import docx


#data = load_excel(file_name=config.DATA_FILE)
#gdf = load_geometry(file_name=config.GEO_DATA_FILE)
#geojsdata = pp.shapefile_to_geojson(gdf, list(gdf.index),tolerance=0)
#afghanistan_geometry = load_geometry(file_name=config.GEO_DATA_FILE)



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
                                    html.Div(html.H5("Appendix", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
                                        className="subtitle padded",
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
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
            html.Div(html.P('We could put some information here',style={"color": "#ffffff"}),style= {"background-color": "#565656","border-bottom": "5px solid #76323F", "padding": "20px","margin-bottom": "30px"}),
            html.Br([]),
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
                                    html.Div(html.H5("Appendix cont.", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
                                        className="subtitle padded",
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
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
            html.Div(html.P('We could put some information here',style={"color": "#ffffff"}),style= {"background-color": "#565656","border-bottom": "5px solid #76323F", "padding": "20px","margin-bottom": "30px"}),
            html.Br([]),
        ],
        className="page",
    ), 
    html.Div(
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
                                    html.Div(html.H5("Appendix cont.", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
                                        className="subtitle padded",
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
                                        ["Header"], className="subtitle padded"
                                    )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Header",
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
            html.Div(html.P('We could put some information here',style={"color": "#ffffff"}),style= {"background-color": "#565656","border-bottom": "5px solid #76323F", "padding": "20px","margin-bottom": "30px"}),
            html.Br([]),
        ],
        className="pagetwo",
    )