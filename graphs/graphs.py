# External libraries
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
import dash_table
from plotly.subplots import make_subplots


mapbox_token = 'pk.eyJ1IjoiY2F3aWUiLCJhIjoiY2s1cGVsN3U3MHVrYTNsbnNpd3pubGR3ZSJ9.5sgCAI1IM9pOmmk4dZeD4Q'
COLORSCALE = ['#76323f',
                '#7d3c45', 
                '#84464b', 
                '#8a4f51', 
                '#915957', 
                '#97635e', 
                '#9e6c65', 
                '#a4766d', 
                '#ab8075', 
                '#b18a7e', 
                '#b79487', 
                '#bc9e91', 
                '#c2a89c', 
                '#c7b2a8', 
                '#ccbcb4', 
                '#d0c7c3', 
                '#d4d1d3'].reverse()

# Internal modules
from config import config

def barchart(x1,y1, x2=None,y2=None):
    data = [
        go.Bar(
            x = x1,
            y = y1,

            marker = {
                'color': '#76323F',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2,
                }
            },
            name = 'group_1'
        ),

        go.Bar(
            x = x2,
            y = y2,

            marker = {
                'color': '#d4d1d3',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2,
                }
            },
            name = 'group_2'
        )
    ]

    layout = go.Layout(
        template = 'plotly_white',
        autosize = False,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 200,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = True,
        title = '',
        width = 330,

        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure
#barchart(x,y, x, y2)

def density_heat_map(latitude, longitude, quantity, geometry, custom_info=None):
    
    data = [
        {
            'lat':latitude, 
            'lon':longitude, 
            'z':quantity,
            'customdata': custom_info,
            
            'radius': 35,
            'type': 'densitymapbox',
            'showscale': False,
            
            'hovertemplate': 
                "<b>%{customdata}</b><br><br>" + "<extra></extra>" + 
                "population: %{z}<br>" + 
                "longitude: %{lon}<br>" + 
                "latitude: %{lat}<br>"
        }
    ]
    
    layout = {
        'margin': {'l': 10, 'r': 20, 'b': 0, 't': 0},
        'autosize': True,
        'height': 250,
        'width': 350,
        'hovermode': 'closest',
        
        'mapbox': {
            'accesstoken': mapbox_token,
            'style': 'streets',
            'center' : 
            {
                'lon':65.21600, 
                'lat':33.677
            },
            
            'zoom': 4,
            'layers': [
                {
                    'type': 'fill',
                    'below': 'traces',
                    'color': 'rgba(275, 0, 0, 0.1)',
                    'source': {
                        'type': "FeatureCollection",
                        'features': 
                            [
                                {
                                    'type': "Feature",
                                    'geometry': {
                                        'type': "MultiPolygon",
                                        'coordinates': [np.dstack((geometry['geometry'][0].exterior.coords.xy))]
                                    }
                                }
                            ]
                    },
                    'type': "fill",
                    'below': "traces",
                    'color': "rgba(275, 0, 0, 0.1)"
                }
            ]
        }
    }
    
    fig = go.Figure(data=data, layout=layout)
    
    return fig

#density_heat_map(iset_map['lon'], iset_map['lat'], iset_map['total_indiv'], afghanistan_geometry,iset_map['settlement'])


def linechart(x):
    data = [
        go.Scatter(
            x = x.value_counts().sort_index().index,
            y = x.value_counts().sort_index().values,
            line = {'color': '#97151c', 'smoothing':1, 'shape': 'spline'},
            mode = 'lines',
            name = 'set a name for me'
        )
    ]
    
    layout = go.Layout(
        template = 'plotly_white',
        autosize = True,
        title = '',
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 200,
        width = 340,
        hovermode = 'closest',
        legend = {
            'x': -0.0277108433735,
            'y': -0.142606516291,
            'orientation': 'h'
        },
        margin = {
            'r': 20,
            't': 20,
            'b': 20,
            'l': 50
        },
        showlegend = True,
        xaxis = {
            'autorange': True,
            'linecolor': 'rgb(0, 0, 0)',
            'linewidth': 1,
            'showgrid': False,
            'showline': True,
            'title': '',
            'type': 'linear',
        }
    )
    
    yaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        'nticks': 4,
        'showgrid': True,
        'showline': True,
        'ticklen': 5,
        'ticks': 'outside',
        'title': 'Label me!',
        'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    }
    
    fig = go.Figure(data=data, layout=layout)
    
    return fig

def linechart2(x1=None, y1=None, x2=None, y2=None, x3=None, y3=None, x4=None, y4=None):
    fig = go.Figure()
    
    fig.add_trace(
        go.Scatter(
            x = x1,
            y = y1,
            
            line = {'color': '#76323F'},
            mode = 'lines',
            name = 'set a name for me'))
    
    fig.add_trace(
        go.Scatter(
            x = x2,
            y = y2,
            
            line = {'color': '#d4d1d3', 'dash': 'dot', 'width': 1},
            mode = 'lines',
            name = 'set a name for me'))

    fig.add_trace(
        go.Scatter(
            x = x3,
            y = y3,
            
            line = {'color': '#565656', 'dash': 'dot', 'width': 1},
            mode = 'lines',
            name = 'set a name for me'))

    fig.add_trace(
        go.Scatter(
            x = x4,
            y = y4,
            
            line = {'color': '#C09F80', 'dash': 'dot', 'width': 1},
            mode = 'lines',
            name = 'set a name for me'))
    
    fig.update_layout(
        template = 'plotly_white',
        autosize = True,
        title = '',
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 200,
        width = 340,
        hovermode = 'closest',
        legend = {
            'x': -0.0277108433735,
            'y': -0.142606516291,
            'orientation': 'h'
        },
        margin = {
            'r': 20,
            't': 20,
            'b': 20,
            'l': 50
        },
        showlegend = True,
        xaxis = {
            'autorange': True,
            'linecolor': 'rgb(0, 0, 0)',
            'linewidth': 1,
            'showgrid': False,
            'showline': True,
            'title': '',
            'type': 'linear',
        }
    ),
    
    yaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        'nticks': 4,
        'showgrid': True,
        'showline': True,
        'ticklen': 5,
        'ticks': 'outside',
        'title': 'Label me!',
        'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    }
    
    
    return fig

def choropleth(geojson, location_id, variable, label):
    
    data = go.Choroplethmapbox(
        geojson = geojson,
        locations = location_id,
        z = variable,
        text = label,
        colorscale = 'reds',
        #colorbar = {'thickness':20, 'ticklen':3},
        showscale = False,
        marker_line_width=0.5, 
        marker_opacity=0.5
        
    )
    
    layout = go.Layout(
        title_text = '',
        autosize = True,
        height = 250,
        width = 350,
        margin = {'l': 10, 'r': 0, 'b': 0, 't': 0},
        mapbox = {'center': {'lat':33.677, 'lon':65.21600},
                 'accesstoken': mapbox_token,
                 'zoom':4,
                 'style': 'light'}
    )
    
    fig = go.Figure(data=data, layout=layout)

    return fig

# choropleth(geojsdata, gdf['ID_1'], gdf['ID_1'])


def barchart2(x1,y1, x2=None,y2=None, x3=None, y3=None, x4=None, y4=None):
    data = [
        go.Bar(
            x = x1,
            y = y1,

            marker = {
                'color': '#76323F',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_1'
        ),

        go.Bar(
            x = x2,
            y = y2,

            marker = {
                'color': '#d4d1d3',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_2'
        ),
        
        go.Bar(
            x = x3,
            y = y3,

            marker = {
                'color': '#565656',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_3'
        ),
        
        go.Bar(
            x = x4,
            y = y4,

            marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_4'
        ),
    ]

    layout = go.Layout(
        template = 'plotly_white',
        autosize = False,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 200,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = True,
        title = '',
        width = 330,

        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure


#barchart2(x1 = df[df['Target']==1]['instlevel1-sum'].value_counts(normalize=True).index, 
#         y1 = df[df['Target']==1]['instlevel1-sum'].value_counts(normalize=True).values,
#         x2 = df[df['Target']==2]['instlevel1-sum'].value_counts(normalize=True).index, 
#         y2 = df[df['Target']==2]['instlevel1-sum'].value_counts(normalize=True).values,
#         x3 = df[df['Target']==3]['instlevel1-sum'].value_counts(normalize=True).index, 
#         y3 = df[df['Target']==3]['instlevel1-sum'].value_counts(normalize=True).values,
#         x4 = df[df['Target']==4]['instlevel1-sum'].value_counts(normalize=True).index, 
#         y4 = df[df['Target']==4]['instlevel1-sum'].value_counts(normalize=True).values
#        )


def distplot(data, groups=None):
    data = data
    groups = groups
    
    fig = ff.create_distplot(data, 
                             groups, 
                             show_rug=False, 
                             show_hist=False, 
                             colors=config.COLORS)
    
    
    fig.update_layout(
    template = 'plotly_white',
    autosize = True,
    title = '',
    font = {
        'family': 'Raleway',
        'size': 10
    },
    height = 200,
    width = 340,
    hovermode = 'closest',
    legend = {
        'x': -0.0277108433735,
        'y': -0.142606516291,
        'orientation': 'h'
    },
    margin = {
        'r': 20,
        't': 20,
        'b': 20,
        'l': 50
    },
    showlegend = True,
    xaxis = {
        'autorange': True,
        'linecolor': 'rgb(0, 0, 0)',
        'linewidth': 1,
        'showgrid': False,
        'showline': True,
        'title': '',
        'type': 'linear',
    }
)
    
    return fig


#distplot([df[df['Target']==1]['escolari'], 
#          df[df['Target']==2]['escolari'],  
#          df[df['Target']==3]['escolari'],
#          df[df['Target']==4]['escolari']], 
#         ['a', 'b', 'c', 'd'])


def correlation_heatmap(data):
    fig = go.Figure(
        data = go.Heatmap(
            z = data.corr(),
            x = data.corr().columns,
            y = data.corr().index,
            colorscale = ['#76323f',
                '#7d3c45', 
                '#84464b', 
                '#8a4f51', 
                '#915957', 
                '#97635e', 
                '#9e6c65', 
                '#a4766d', 
                '#ab8075', 
                '#b18a7e', 
                '#b79487', 
                '#bc9e91', 
                '#c2a89c', 
                '#c7b2a8', 
                '#ccbcb4', 
                '#d0c7c3', 
                '#d4d1d3'],
            xgap = 0.5,
            ygap = 0.5,
            colorbar = {
                'thickness':15, 
                'ticklen':3, 
                'len': 1.037, 
                'x':0.99, 
                'tickmode': 'auto',
            }
        )
    )
    
    fig.update_layout(
        showlegend = False,
        width = 500, 
        height = 500,
        autosize = True,
        
        margin = {
        'r': 20,
        't': 20,
        'b': 20,
        'l': 20},

        xaxis = {'tickangle': -45},
        yaxis = {'tickangle': -45},
        font = {'family': 'Raleway','size': 10}
        
    )

    
    return fig

#correlation_heatmap(df)


def horizontal_bar(x1,y1, x2=None,y2=None, x3=None, y3=None, x4=None, y4=None):
    data = [
        go.Bar(
            x = x1,
            y = y1,

            marker = {
                'color': '#76323F',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_1',
            orientation='h'
        ),

        go.Bar(
            x = x2,
            y = y2,

            marker = {
                'color': '#d4d1d3',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_2',
            orientation='h'
            
        ),
        
        go.Bar(
            x = x3,
            y = y3,

            marker = {
                'color': '#565656',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_3',
            orientation='h'
        ),
        
        go.Bar(
            x = x4,
            y = y4,

            marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 1,
                }
            },
            name = 'group_4',
            orientation='h'
        ),
    ]

    layout = go.Layout(
        template = 'plotly_white',
        autosize = False,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 530,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = True,
        title = '',
        width = 200,

        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'linear'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'category',
            'zeroline': False,
            'showticklabels': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure

#horizontal_bar(y1 = df.corr()['Target'].index[:-1], x1 = df.corr()['Target'].values[:-1])


def correlation_heatmap(data):
    fig = go.Figure(
        data = go.Heatmap(
            z = data.corr(),
            x = data.corr().columns,
            y = data.corr().index,
            colorscale = ['#76323f',
                        '#7d3c45', 
                        '#84464b', 
                        '#8a4f51', 
                        '#915957', 
                        '#97635e', 
                        '#9e6c65', 
                        '#a4766d', 
                        '#ab8075', 
                        '#b18a7e', 
                        '#b79487', 
                        '#bc9e91', 
                        '#c2a89c', 
                        '#c7b2a8', 
                        '#ccbcb4', 
                        '#d0c7c3', 
                        '#d4d1d3'],
            xgap = 0.5,
            ygap = 0.5,
            colorbar = {
                'thickness':15, 
                'ticklen':3, 
                'len': 1.05, 
                'x':-0.08, 
                'tickmode': 'auto',
                'showticklabels': True,
                'ticks': 'outside'
                
            },
            showscale=False
        )
    )
    
    fig.update_layout(
        showlegend = False,
        width = 500, 
        height = 500,
        autosize = True,
        
        xaxis = {
            'tickangle': -45
        },
        yaxis = {
            'tickangle': 0,
            'side': 'right'
        },
        
        margin = {
        'r': 20,
        't': 20,
        'b': 20,
        'l': 20},
        
        font = {
            'family': 'Raleway',
            'size': 10
        },

        
    )
    
    return fig


colorscale = ['#76323f',
            '#7d3c45', 
            '#84464b', 
            '#8a4f51', 
            '#915957', 
            '#97635e', 
            '#9e6c65', 
            '#a4766d', 
            '#ab8075', 
            '#b18a7e', 
            '#b79487', 
            '#bc9e91', 
            '#c2a89c', 
            '#c7b2a8', 
            '#ccbcb4', 
            '#d0c7c3', 
            '#d4d1d3']




def confusion_matrix(data):
    #x = np.array(data)
    
    font_colors = ['white', 'black']
    fig = ff.create_annotated_heatmap(data,
    								[1,2,3,4],[1,2,3,4],
                                      colorscale=colorscale,
                                      font_colors=font_colors, 
                                      xgap = 0.5,
                                      ygap = 0.5, reversescale=True, transpose=True)
    
    fig.update_layout(
        showlegend = True,
        width = 300, 
        height = 300,
        autosize = True,
        
        xaxis = {
            'tickangle': 0,
            'title':'Predicted values',
            'side':'bottom'
        },
        yaxis = {
            'tickangle': 0,
            'side': 'left',
            'dtick':1,
            'title':'Observed values'
        },
        
        margin = {
        'r': 20,
        't': 20,
        'b': 20,
        'l': 20},
        
        font = {
            'family': 'Raleway',
            'size': 10}




        
    )

    for i in range(len(fig.layout.annotations)):
        fig.layout.annotations[i].font.size = 15
        
        
    return fig

#confusion_matrix(np.array(conf_mat))


def data_table(data):
    return dash_table.DataTable(
        data=data.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in data.columns],

        style_cell_conditional=[
        {
        'if': {'column_id': c},
        'textAlign': 'left'
        } for c in ['Date', 'Region']
        ],
        style_data_conditional=[
        {
        'if': {'row_index': 'odd'},
        'backgroundColor': 'rgb(248, 248, 248)'
        },
        {
        'if': {'column_index': 0},
        'fontWeight': 'bold'
        }
        ],
        style_header={
        'backgroundColor': 'rgb(230, 230, 230)',
        'fontWeight': 'bold'
        }
        )

def box_plot(data):
    data = [
        go.Box(
            y = data[0],
            marker_color = '#76323F',
            boxmean=True,
            name = '1'
    ),

        go.Box(
            y = data[1],
            marker_color = '#D4D1D3',
            boxmean=True,
            name = '2'

    
    ),

        go.Box(
            y = data[2],
            marker_color = '#565656',
            boxmean=True,
            name = '3'

        ),

        go.Box(
            y = data[3],
            marker_color = '#C09F80',
            boxmean=True,
            name = '4'

        )

    ]

    layout = go.Layout(
        template = 'plotly_white',
        autosize = False,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 330,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = False,
        title = '',
        width = 330,

        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
    figure = go.Figure(data=data, layout=layout)
    
    return figure




##########
########### INTERPRETATIONS EXPERIMENT
###########
from processing.data_management import load_excel

df = load_excel(file_name=config.DATA_FILE)

interpretations = {0: [(8, 0.1142757655826782),
                  (11, 0.0419749689507324),
                  (17, -0.040193937766442395),
                  (19, 0.021369448257611598),
                  (6, 0.015126651604110641),
                  (13, -0.012431268283180513),
                  (1, -0.010793721082423855),
                  (4, -0.010474517613815413),
                  (9, 0.007865948084430117),
                  (20, -0.00784333216080914)],
                 1: [(8, 0.16589278177299743),
                  (5, 0.03939243605466441),
                  (20, -0.030085051115543156),
                  (10, -0.028261514208108608),
                  (1, -0.027190389445609843),
                  (19, 0.025664712685355837),
                  (0, -0.023760400993341303),
                  (11, 0.022567941419526394),
                  (14, 0.01985587077530867),
                  (4, -0.013685935897889587)],
                 2: [(5, 0.04397255998896912),
                  (6, -0.033823068009956984),
                  (11, 0.027751176160879708),
                  (19, 0.014277439297171454),
                  (1, -0.012563057599777138),
                  (20, -0.011664355336948014),
                  (14, 0.011502194747900657),
                  (18, 0.010764849714433703),
                  (21, 0.009144088030303251),
                  (4, -0.008883107784215862)],
                 3: [(8, -0.29013624738128746),
                  (11, -0.09336580426681963),
                  (5, -0.07994872028669171),
                  (19, -0.05960366598688584),
                  (1, 0.05116871472907155),
                  (20, 0.04990932267236625),
                  (17, 0.038443167529905745),
                  (14, -0.033492688122290275),
                  (4, 0.032669382426876475),
                  (21, -0.02689251341300879)]}

probabilities = np.array([0.15845577, 0.23450424, 0.20235643, 0.40468356])




def interpret():
    data = make_subplots(rows=3, 
                        cols=2, 
                        shared_xaxes=False, 
                        vertical_spacing=0.13,
                        subplot_titles=(['Outcome: ' + str(i) for i in interpretations.keys()]),
                        specs=[
                            [{}, {}], 
                            [{}, {}], 
                            [{"colspan": 2}, None]],


                       )

    data.add_trace(
        go.Bar(

            x=df.columns[[i[0] for i in interpretations[0]]],
            y=[i[1] for i in interpretations[0]], 
                    marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2}
                }
        ),

        row=1, 
        col=1)

    data.add_trace(
        go.Bar(

            x=df.columns[[i[0] for i in interpretations[1]]],
            y=[i[1] for i in interpretations[1]], 
                    marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2}
                }
        ),

        row=1, 
        col=2)

    data.add_trace(
        go.Bar(

            x=df.columns[[i[0] for i in interpretations[2]]],
            y=[i[1] for i in interpretations[2]], 
                    marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2}
                }
        ),

        row=2, 
        col=1)

    data.add_trace(
        go.Bar(

            x=df.columns[[i[0] for i in interpretations[3]]],
            y=[i[1] for i in interpretations[3]], 
                marker = {
                'color': '#C09F80',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2}
                }),

        row=2, 
        col=2)

    data.add_trace(
        go.Bar(

            y=probabilities,
            orientation='v',
            marker = {
                'color': '#76323F',
                'line': {
                    'color': 'rgb(255, 255, 255)',
                    'width': 2}
                }
        ), 
        row=3, col=1)

    layout = data.update_layout(height=600,
                      width=700,
                      title_text='', 
                      showlegend=False,
                      template = 'plotly_white', 
                      font = {'family': 'Raleway',
                              'size': 10},

                      margin = {'r': 0,
                                't': 20,
                                'b': 10,
                                'l': 10})

    data.update_xaxes(tickangle=-30)
    data.update_xaxes(title_text="Predicted Probabilities", row=3, col=1)


    
    figure = go.Figure(data=data, layout=layout)
    
    return figure

def plot_regularization(data):
    
    fig = go.Figure()
    for column in data.columns:
        fig.add_trace(
            go.Scatter(
                x = data.index,
                y = data[column],
                mode = 'lines',
                name=column
            )
        )
    
    fig.update_layout(
        template = 'plotly_white',
        autosize = True,
        title = '',
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 300,
        width = 440,
        hovermode = 'closest',
        #legend = {
        #    'x': -0.0277108433735,
        #    'y': -0.142606516291,
        #    'orientation': 'h'
        #},
        margin = {
            'r': 20,
            't': 20,
            'b': 20,
            'l': 50
        },
        showlegend = False,
        xaxis = {
            'autorange': True,
            'linecolor': 'rgb(0, 0, 0)',
            'linewidth': 1,
            'showgrid': False,
            'showline': True,
            'title': '',
            'type': 'linear',
        }
    ),
    
    yaxis = {
        'autorange': True,
        'gridcolor': 'rgba(127, 127, 127, 0.2)',
        'mirror': False,
        'nticks': 4,
        'showgrid': True,
        'showline': True,
        'ticklen': 5,
        'ticks': 'outside',
        'title': 'Label me!',
        'type': 'linear',
        'zeroline': False,
        'zerolinewidth': 4
    },
    fig.update_layout(xaxis_type="log", yaxis_type="linear")
    
    return fig


def barchart_multi(dataframe):
    data = []
    
    for variable in dataframe.columns:
        data.append(
            go.Bar(
                x = dataframe[variable].index,
                y = dataframe[variable].values,
                
                marker = {
                    #'color': '#76323F',
                    'line': {
                        'color': 'rgb(255, 255, 255)',
                        'width': 0}
                },
                name = variable,
                orientation='v'
            )
        )
        
        layout = go.Layout(
        template = 'plotly_white',
        autosize = True,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 300,
        width = 700,
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = True,
        title = '',


        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
        
    figure = go.Figure(data=data, layout=layout)
    figure.update_traces(marker_color=['#D4D1D3', '#565656', '#76323F','#C09F80'], showlegend=False)
    
    return figure

def barchart_multi(dataframe):
    data = []
    colors = ['#D4D1D3', '#565656', '#76323F','#C09F80']
    
    for variable in range(len(dataframe.columns)):
        data.append(
            go.Bar(
                x = dataframe[variable].index,
                y = dataframe[variable].values,
                
                
                marker = {
                    'color': colors[variable],
                    'line': {
                        'color': 'rgb(255, 255, 255)',
                        'width': 0}
                },
                name = dataframe.columns[variable],
                orientation='v'
            )
        )
        
        layout = go.Layout(
        template = 'plotly_white',
        autosize = True,
        bargap = 0.35,
        font = {
            'family': 'Raleway',
            'size': 10
        },
        height = 300,
        width = 700,
        barmode='group',
        legend = {
            'x': -0.0228945952895,
            'y': -0.189563896463,
            'orientation': 'h',
            'yanchor': 'top'
        },
        margin = {
            'r': 0,
            't': 20,
            'b': 10,
            'l': 10
        },
        showlegend = True,
        title = '',


        xaxis = {
            'autorange': True,
            'showline': True,
            'title': '',
            'type': 'category'
        },
        yaxis = {
            'autorange': True,
            'showgrid': True,
            'showline': True,
            'title': '',
            'type': 'linear',
            'zeroline': False
        },
        transition = {
                'duration': 500,
                'easing': 'cubic-in-out'
            }
    )
    
        
    figure = go.Figure(data=data, layout=layout)
    
    return figure



