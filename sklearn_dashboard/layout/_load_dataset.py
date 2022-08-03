
from dash.html import Div 
from dash.dcc import Dropdown

from sklearn_dashboard import app
from ..utils import dash_component_label
from sklearn_dashboard.callback import load_dataset_callback

from sklearn_dashboard.datasets.load_data import default_datasets
df_options = list(default_datasets.keys())


def load_data_layout(children):
    return Div(children=children, 
                className="load-dataset-wrapper model-content-item", 
                id="load_dataset")

#define components items
header = Div("load dataset", className="model-content-header")

#data options 
data_options = {"options": ["default_dataset", "upload_dataset"], 
                "clearable": False,
                "value": "default_dataset",
            }

data_components = dash_component_label(label = "data_options", 
                                    component_type = "dropdown", 
                                    component_kwargs = data_options)

default_dataset = dash_component_label(label="default_dataset", 
                        component_type="dropdown",
                        component_kwargs={"options": df_options, "value": df_options[0]})

upload_dataset = dash_component_label(label="upload_dataset", 
                                            component_kwargs={
                                                "style": {"color": "white", 
                                                    "cursor": "pointer", "textAlign": "center",
                                                    "padding": "7px",
                                                    "border": "1px dashed"},
                                                "children": Div("click to upload [csv, txt]")},
                                            component_type="upload")

# output_dataframe = Div(className="output-datatable", id="output_datatable")

load_data_items = load_data_layout([header, data_components, default_dataset, 
                                    upload_dataset])


# load_dataset_callback(app)
