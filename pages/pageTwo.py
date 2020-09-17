# Internal modules
from processing.data_management import load_excel, load_excel, load_document
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
conf_mat = load_excel(file_name='confusion_matrix.xlsx')
#conf_mat.drop(conf_mat.columns[0], axis=1, inplace=True)
classification_report = load_excel(file_name='classification_report.xlsx')
y_pred = load_excel(file_name='predicted_probabilities.xlsx')

print(np.array(conf_mat))
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
                                    html.Div(html.H5("Model Evaluation", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Confusion Matrix"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one-p2',
                                        figure = graphs.confusion_matrix(np.array(conf_mat)))
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Classification Report",
                                        className="subtitle padded",
                                    ),
                                    graphs.data_table(classification_report.round(3).rename(columns={classification_report.columns[0]: ''}))
                                    
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
                                        "Predictions by class", 
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p2',
                                        figure = graphs.box_plot(y_pred))
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
                                    html.Div(html.H5("Model Evaluations", style={"padding-left": "10px"}), className="inner-product2"),
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
                                [html.H6(["Correlations"], className="subtitle padded")],
                                className="twelve columns",
                            )
                        ],
                        className="rows",
                    ),
                    html.Div(
                        [
                            html.Div(
                                [
                                    dcc.Graph(id='ass', figure=graphs.correlation_heatmap(df.drop('Target', axis=1))),
                                ],
                                className="eight columns",
                            ),
                            html.Div(
                                [
                                dcc.Graph(id='goat', figure=graphs.horizontal_bar(y1 = df.corr()['Target'].index[:-1], x1 = df.corr()['Target'].values[:-1]))

                                ],
                                className="four columns",
                            )
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