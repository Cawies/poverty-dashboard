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




def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Problem statement", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P("Background"),
                                            html.P("Many social programs have a hard time making sure the right people are given enough aid. It’s especially tricky when a program focuses on the poorest segment of the population. \
                                                The world’s poorest typically can’t provide the necessary income and expense records to prove that they qualify.\
                                                In Latin America, one popular method uses an algorithm to verify income qualification. It’s called the Proxy Means Test (or PMT).\
                                                 With PMT, agencies use a model that considers a family’s observable household attributes like the material of their walls and ceiling,\
                                                or the assets found in the home to classify them and predict their level of need. While this is an improvement,\
                                                 accuracy remains a problem as the region’s population grows and poverty declines. To improve on PMT, the IDB (the largest source of development financing \
                                                  for Latin America and the Caribbean) released household data to the public. They believe that new methods beyond traditional econometrics, based on a dataset of \
                                                   Costa Rican household characteristics, might help improve PMT’s performance. Beyond Costa Rica, many countries face this same problem of inaccurately assessing social need.\
                                                    If a model can can generate an improvement, the new algorithm could be implemented in other countries around the world.")
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.H6("Data preprocessing pipeline", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P("The dataset consists of information on a total of 23.857 individuals grouped into households.\
                                                Each household has one head, which is representative of the household and thus the target for prediction.\
                                                The data preprocessing pipeline cleans to ensure that (1) each household has only one head, (2) poverty levels\
                                                of household members are aligned to the head of the household, (3) ordinal variables are properly coded, \
                                                strings are coded into numerical values, (4) missing values are properly treated by imputation or removal.\
                                                The pipeline then groups the individual household member and aggregates their characteristics to produce a household level observation."),
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),

                            html.Div(
                                [
                                    html.H6("Data dimensionality reduction pipeline", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P("ORIGINAL AGGREGATED DATA DIMENSIONALITY: 143 columns (incl. Target), 2974 rows"),
                                            html.P("1. Constant and quasi-constant variables: remove variables with standard deviation < threshold. "),
                                            html.P("2. Remove duplicated variables: remove identically distributed variables."),
                                            html.P('3. Identify groups of correlated variables: remove least predictive variable from group as evaluated by group specific decision tree model.'),
                                            html.P('4. Identify most informative variables by entropy.'),
                                            html.P('4. Identify most predictive variables as evaluated by decicion tree based Receiver Operating Characteristic (ROC) curve'),
                                            html.P("REDUCED AGGREGATED DATA DIMENSIONALITY: 23 columns (incl. Target), 2974 rows")
                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),

                        ],
                        className="row ",
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
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Model: Multinomial Logistic Regression", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P("The multinomial logistic regression is an extension of the binary logistic regression and serves as a good baseline model for multiclass classification."),
                                            html.P("\
                                                Similarly to One-versus-Rest (OVR) approaches, a series of models are fitted to the data with the difference that one class outcome \
                                                is consistently used as a baseline reference category for the other class outcomes. As such it fits K-1 number of models with their corresponding coefficients. \
                                                While the poverty level outcome is ordinal by nature, the multinomial model treats each class outcome as categorically unrelated."),
                                            html.P("Logistic models are linear models and are therefore subject to the common assumptions of:"),
                                            html.P('1. Additivity and Linearity'),
                                            html.P('2. Normality'),
                                            html.P('3. Homoskedasticity (homogeneity of variance)'),
                                            html.P('4. Independence')

                                        ],
                                        style={"color": "#7a7a7a"},
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ), 
            html.Div(html.P('We could put some information here',style={"color": "#ffffff"}),style= {"background-color": "#565656","border-bottom": "5px solid #76323F", "padding": "20px","margin-bottom": "30px"}),
            html.Br([]),
        ],
        className="page",
    ),