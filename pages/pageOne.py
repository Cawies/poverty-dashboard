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


df = load_excel(file_name=config.DATA_FILE)
#model_coefficients = load_excel(file_name='logistic_model_coefficients.xlsx')
feature_importances = load_excel(file_name='tree_importances.xlsx')
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
                                    html.Div(html.H5("Associations", style={"padding-left": "10px"}), className="inner-product2"),
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
                                        ["Rent by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-one-p1',
                                        figure = graphs.distplot(
                                            [df[(df['Target']==1) & (df['v2a1']>=0) & (df['v2a1']<=300000)]['v2a1'], 
                                            df[(df['Target']==2) & (df['v2a1']>=0) & (df['v2a1']<=300000)]['v2a1'],  
                                            df[(df['Target']==3) & (df['v2a1']>=0) & (df['v2a1']<=300000)]['v2a1'],
                                            df[(df['Target']==4) & (df['v2a1']>=0) & (df['v2a1']<=300000)]['v2a1']], 
                                            ['a', 'b', 'c', 'd'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Number of rooms by poverty level",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id='graph-two-p1',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['rooms'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['rooms'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['rooms'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['rooms'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['rooms'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['rooms'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['rooms'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['rooms'].value_counts(normalize=True).values)
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
                                        ["Over crowding by poverty level"], 
                                        className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-three-p1',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['SQBovercrowding'], 
                                                    df[df['Target']==2]['SQBovercrowding'],  
                                                    df[df['Target']==3]['SQBovercrowding'],
                                                    df[df['Target']==4]['SQBovercrowding']], 
                                                    ['a', 'b', 'c', 'd'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Quality of walls by poverty level",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-four-p1',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['walls'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['walls'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['walls'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['walls'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['walls'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['walls'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['walls'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['walls'].value_counts(normalize=True).values)
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
                                        ["Quality of ceiling by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seventeen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['cielorazo'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['cielorazo'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['cielorazo'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['cielorazo'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['cielorazo'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['cielorazo'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['cielorazo'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['cielorazo'].value_counts(normalize=True).values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Quality of roof by poverty level",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eighteen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['roof'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['roof'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['roof'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['roof'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['roof'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['roof'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['roof'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['roof'].value_counts(normalize=True).values)
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
                                        ["Number of children aged 0-12 by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seventeen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['r4t1'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['r4t1'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['r4t1'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['r4t1'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['r4t1'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['r4t1'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['r4t1'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['r4t1'].value_counts(normalize=True).values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Number of persons aged 0-19 by poverty level",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eighteen',
                                        figure = graphs.barchart2(
                                            x1 = np.sqrt(df[df['Target']==1]['SQBhogar_nin']).value_counts(normalize=True).index, 
                                            y1 = np.sqrt(df[df['Target']==1]['SQBhogar_nin']).value_counts(normalize=True).values,
                                            x2 = np.sqrt(df[df['Target']==2]['SQBhogar_nin']).value_counts(normalize=True).index, 
                                            y2 = np.sqrt(df[df['Target']==2]['SQBhogar_nin']).value_counts(normalize=True).values,
                                            x3 = np.sqrt(df[df['Target']==3]['SQBhogar_nin']).value_counts(normalize=True).index, 
                                            y3 = np.sqrt(df[df['Target']==3]['SQBhogar_nin']).value_counts(normalize=True).values,
                                            x4 = np.sqrt(df[df['Target']==4]['SQBhogar_nin']).value_counts(normalize=True).index, 
                                            y4 = np.sqrt(df[df['Target']==4]['SQBhogar_nin']).value_counts(normalize=True).values)
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
                                        ["Dependency Ratio by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['dependency'], 
                                                    df[df['Target']==2]['dependency'],  
                                                    df[df['Target']==3]['dependency'],
                                                    df[df['Target']==4]['dependency']], 
                                                    ['a', 'b', 'c', 'd'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Minumum age by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['age-min'], 
                                                    df[df['Target']==2]['age-min'],  
                                                    df[df['Target']==3]['age-min'],
                                                    df[df['Target']==4]['age-min']], 
                                                    ['a', 'b', 'c', 'd'])
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
                                        ["Maximum age by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seventeen',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['age-max'], 
                                                    df[df['Target']==2]['age-max'],  
                                                    df[df['Target']==3]['age-max'],
                                                    df[df['Target']==4]['age-max']], 
                                                    ['a', 'b', 'c', 'd'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Male head of household education by poverty level",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eighteen',
                                        figure = graphs.barchart2(
                                            x1 = np.sqrt(df[df['Target']==1]['SQBedjefe']).value_counts(normalize=True).index, 
                                            y1 = np.sqrt(df[df['Target']==1]['SQBedjefe']).value_counts(normalize=True).values,
                                            x2 = np.sqrt(df[df['Target']==2]['SQBedjefe']).value_counts(normalize=True).index, 
                                            y2 = np.sqrt(df[df['Target']==2]['SQBedjefe']).value_counts(normalize=True).values,
                                            x3 = np.sqrt(df[df['Target']==3]['SQBedjefe']).value_counts(normalize=True).index, 
                                            y3 = np.sqrt(df[df['Target']==3]['SQBedjefe']).value_counts(normalize=True).values,
                                            x4 = np.sqrt(df[df['Target']==4]['SQBedjefe']).value_counts(normalize=True).index, 
                                            y4 = np.sqrt(df[df['Target']==4]['SQBedjefe']).value_counts(normalize=True).values)
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
                                        ["Female head of household education by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['edjefa'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['edjefa'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['edjefa'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['edjefa'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['edjefa'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['edjefa'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['edjefa'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['edjefa'].value_counts(normalize=True).values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Lowest education by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['escolari-min'], 
                                                    df[df['Target']==2]['escolari-min'],  
                                                    df[df['Target']==3]['escolari-min'],
                                                    df[df['Target']==4]['escolari-min']], 
                                                    ['a', 'b', 'c', 'd'])
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
                                        ["Higest education by poverty level"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-seventeen',
                                        figure = graphs.distplot(
                                                    [df[df['Target']==1]['escolari-max'], 
                                                    df[df['Target']==2]['escolari-max'],  
                                                    df[df['Target']==3]['escolari-max'],
                                                    df[df['Target']==4]['escolari-max']], 
                                                    ['a', 'b', 'c', 'd'])
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "No completed education",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id = 'graph-eighteen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['instlevel1-sum'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['instlevel1-sum'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['instlevel1-sum'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['instlevel1-sum'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['instlevel1-sum'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['instlevel1-sum'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['instlevel1-sum'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['instlevel1-sum'].value_counts(normalize=True).values)
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
                                        ["Incomplete primary education"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['instlevel2-sum'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['instlevel2-sum'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['instlevel2-sum'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['instlevel2-sum'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['instlevel2-sum'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['instlevel2-sum'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['instlevel2-sum'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['instlevel2-sum'].value_counts(normalize=True).values)
                                        )
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Undergraduate or higher education"], className="subtitle padded"
                                    ),
                                    dcc.Graph(
                                        id = 'graph-nineteen',
                                        figure = graphs.barchart2(
                                            x1 = df[df['Target']==1]['instlevel8-sum'].value_counts(normalize=True).index, 
                                            y1 = df[df['Target']==1]['instlevel8-sum'].value_counts(normalize=True).values,
                                            x2 = df[df['Target']==2]['instlevel8-sum'].value_counts(normalize=True).index, 
                                            y2 = df[df['Target']==2]['instlevel8-sum'].value_counts(normalize=True).values,
                                            x3 = df[df['Target']==3]['instlevel8-sum'].value_counts(normalize=True).index, 
                                            y3 = df[df['Target']==3]['instlevel8-sum'].value_counts(normalize=True).values,
                                            x4 = df[df['Target']==4]['instlevel8-sum'].value_counts(normalize=True).index, 
                                            y4 = df[df['Target']==4]['instlevel8-sum'].value_counts(normalize=True).values)
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
                                    html.Div(html.H5("Associations", style={"padding-left": "10px"}), className="inner-product2"),
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
                                    dcc.Graph(id='ass', figure=graphs.barchart(feature_importances.sort_values(by='importances')['variable'], feature_importances.sort_values(by='importances')['importances'])),
                                ],
                                className="eight columns",
                            ),
#                            html.Div(
#                                [
#                                dcc.Graph(id='goat', figure=graphs.horizontal_bar(y1 = df.corr()['Target'].index[:-1], x1 = df.corr()['Target'].values[:-1]))
#
                            #    ],
                            #    className="four columns",
                            #)
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
                                    html.Div(html.H5("Associations", style={"padding-left": "10px"}), className="inner-product2"),
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