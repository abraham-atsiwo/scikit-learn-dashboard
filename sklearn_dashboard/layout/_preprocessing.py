
from dash.html import Div
from sklearn import preprocessing 
from typing import List

from ..utils import dash_component_label
from ..utils import preprocessing_categorical, preprocessing_numerical

def preprocessing_layout(children: List):
    return Div(children=children, 
                className="preprocessing-wrapper model-content-item", 
                id="preprocessing")


#build components 
header = Div("feature preprocessing", className="model-content-header")
numeric_columns = dash_component_label(label="numeric columns", 
                                    component_type="dropdown", 
                                    component_kwargs={
                                            "options": list(preprocessing_numerical.keys()), 
                                            "value": "",
                                    }, 
                                    component_id="preprocessing_numeric")

categorical_columns = dash_component_label(label="categorical columns", 
                                    component_type="dropdown", 
                                    component_kwargs={
                                            "options": list(preprocessing_categorical.keys()), 
                                            "value": "",
                                    }, 
                                    component_id="preprocessing_categorical")

preprocessing_items = preprocessing_layout([header, numeric_columns, categorical_columns])