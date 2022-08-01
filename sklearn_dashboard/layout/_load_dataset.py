
from dash.html import Div 
from dash.dcc import Dropdown

from sklearn_dashboard import app
from ..utils import dash_component_label
from sklearn_dashboard.callback import load_dataset_callback


def load_data_layout(children):
    return Div(children=children, 
                className="load-dataset-wrapper model-content-item", 
                id="load_dataset")

#define components items
header = Div("load_dataset", className="model-content-header")

#data options 
data_options = {"options": ["default_dataset", "upload_dataset"], 
                "clearable": False,
                "value": "default_dataset",
            }

data_components = dash_component_label(label = "data_options", 
                                    component_type = "dropdown", 
                                    component_kwargs = data_options)

default_dataset = Div( id="default_upload")

load_data_items = load_data_layout([header, data_components, default_dataset])


load_dataset_callback(app)
