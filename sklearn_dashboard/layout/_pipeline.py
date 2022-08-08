
from dash.html import Div 
from typing import List


from ..utils import dash_component_label


def _display_dtypes(opt: list):
    output = []
    if not isinstance(opt, list):
        opt = list(opt)
    for val in opt:
        comp = Div(val, className="category-item")
        output.append(comp)
    return Div(output)

def data_types(data):
    cat = list(data.select_dtypes("object").columns)
    num = list(data.select_dtypes("number").columns)
    return {"categorical": cat, "numerical": num}


def pipeline_layout(children: List):
    return Div(children=children, 
            className="pipeline-wrapper model-content-item", 
            id="pipeline")


#build component
header = Div("select features", className="model-content-header")
numeric = dash_component_label(label="numeric dtypes features", 
                                component_type="dropdown", 
                                component_kwargs={"options": [], "value": None, "multi": True, 'clearable': False})

categorical = dash_component_label(label="categorical dtypes features", 
                                component_type="dropdown", 
                                component_kwargs={"options": [], "value": None, "multi": True, 'clearable': False})

pipeline_items = pipeline_layout([header, numeric, categorical])