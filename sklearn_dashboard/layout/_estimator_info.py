
from dash.html import Div 
from typing import List

from ..utils import dash_component_label, estimator_type_categories_options


def estimator_info_layout(children: List = None):
    return Div(
            children=children, 
            className="estimator-info-wrapper", 
            id="estimator_info")



estimator_type_dropdown_options = ["regression", "classification"]
estimator_type = dash_component_label(label="estimator_type", 
                                    component_type="dropdown", 
                                    component_kwargs={"options" : estimator_type_dropdown_options})

#estimator type categories
estimator_type_categories_dropdown_options = list(estimator_type_categories_options.keys())
estimator_type_categories = dash_component_label(label="estimator_type_categories", 
                                    component_type="dropdown", 
                                    component_kwargs={"options" : estimator_type_categories_dropdown_options, 
                                                    "value": 'linear_models'})

#estimator_type_categories_options
test_children = [Div("Hello World", className="estimator-type-categories-options-item"), 
                Div("Another option", className="estimator-type-categories-options-item")]

estimator_type_categories_options = Div(children=test_children, className="estimator-type-categories-options",
                                        id="estimator_type_categories_options")

estimator_info_items = estimator_info_layout([estimator_type, 
                                                estimator_type_categories, 
                                                estimator_type_categories_options])