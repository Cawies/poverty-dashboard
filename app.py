# External libraries
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json
import dash_table

# Internal modules
from processing.data_management import load_excel, load_geojson
import processing.preprocessors as pp
from config import config
from graphs import graphs
from pages import (overview, pageOne, pageTwo, pageThree, pageFour, pageFive, pageSix)






# Load data
df = load_excel(file_name=config.DATA_FILE)



# Setup dashboard

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)



server = app.server
app.config.suppress_callback_exceptions = True

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)




# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/report/pageOne":
        return pageOne.create_layout(app)
    elif pathname == "/report/pageTwo":
        return pageTwo.create_layout(app)
    elif pathname == "/report/pageThree":
        return pageThree.create_layout(app)
    elif pathname == "/report/pageFour":
        return pageFour.create_layout(app)
    elif pathname == "/report/pageFive":
        return pageFive.create_layout(app)
    elif pathname == "/report/pageSix":
        return pageSix.create_layout(app)
    #elif pathname == "/report/overview":
    #    return overview.create_layout(app)
    else:
        return overview.create_layout(app)


    

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port=8050,debug=False)