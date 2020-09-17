# Internal modules
from config import config

# External libraries
import pandas as pd
import json
import docx




# Data load during development

def load_excel(*, file_name: str) -> pd.DataFrame:
	_data = pd.read_excel(f"{config.DATASET_DIR}/{file_name}")
	return _data

def load_geojson(*, file_name: str):
    with open(f"{config.DATASET_DIR}/{file_name}") as f:
        geojson = json.load(f)

        return geojson

# Load text document
def load_document(file_name):
    doc = docx.Document(f"{config.DATASET_DIR}/{file_name}")
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)



