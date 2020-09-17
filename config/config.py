# External libraries
import os
import pathlib
import pandas as pd

# Internal modules
from config import config





PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent.parent
DATASET_DIR = f"{PACKAGE_ROOT}/datasets"


# Specify dataset name for loading data
DATA_FILE = 'reduced_data.xlsx'
GEOJSON_FILE = ''
TEXT_FILE = 'description.docx'


# Specify variable names for preprocessing pipeline
VARIABLES = []
DROP_VARIABLES = []


COLORS = ['#D4D1D3',
          '#565656',
          '#76323F',
          '#C09F80']

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


