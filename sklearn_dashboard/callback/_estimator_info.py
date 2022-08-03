
from dash import Output, Input 
from dash.html import Div
from dash import callback_context as ctx

from typing import List

from ..utils import (estimator_type_categories_options, 
                    hyperparameters,
                    multiple_callback_inputs, 
                    dash_component_label)




estimator_type_categories_options_keys = list(estimator_type_categories_options.keys())


def _update_children(children: List):
    if isinstance(children, list):
        return [Div(n_child, 
                    className="estimator-type-categories-options-item", 
                    id=n_child.strip().lower().replace(" ", "_")) for n_child in children]
    raise TypeError


def estimator_info_callback(app):
    @app.callback(Output("estimator_type_categories_options", "children"), 
        Input("estimator_type_categories", "value")
    )
    def update_children_categories_options(options_selected):
        if options_selected:
            selected = options_selected.lower().strip()
            if selected in estimator_type_categories_options_keys:
                children = estimator_type_categories_options[selected]
                return _update_children(children)
        return []

    input_id = list(hyperparameters.keys()) + ['estimator_type_categories']
    input_props = ['n_clicks']*len(hyperparameters) + ['value']
    @app.callback(Output("tuning_hyperparametes_div", "children"), 
        inputs = multiple_callback_inputs(input_id, input_props)
    )
    def update_hyperparameters(all_inputs):
        clicked = ctx.triggered_id
        if clicked == "estimator_type_categories":
            return []
        if clicked is not None:
            if clicked in input_id:
                component = hyperparameters[clicked]
                return component
        return []