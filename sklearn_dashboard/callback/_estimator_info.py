
from dash import Output, Input 
from dash.html import Div
from dash import callback_context as ctx
from dash.dcc import Dropdown
from typing import List, OrderedDict

from ..utils import (estimator_type_categories_options, 
                    multiple_callback_inputs, 
                    multiple_callback_output,
                    dash_component_label)

from ..hyperparameters import show_hide_hyperparameters

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

    input_id = list(show_hide_hyperparameters.keys()) 
    n_input = len(input_id)
    input_props = ['n_clicks']*len(show_hide_hyperparameters) 
    output_id = ['fit_model', 'hyper_slider_div', 'hyper_range_slider_div', 
            'hyper_dropdown_div', 'cv_type_div'] + input_id
    output_props = ['options'] + ['style']*4 + ['style']*n_input

    @app.callback(multiple_callback_output(output_id, output_props), 
        inputs = multiple_callback_inputs(input_id, input_props)
    )
    def update_hyperparameters(all_inputs):
        styles = [{'backgroundColor': 'green'}]*n_input
        clicked = ctx.triggered_id    
        clicked_index = input_id.index(clicked)
        styles[clicked_index] = {'backgroundColor': 'red'}
        model_hyper_style = show_hide_hyperparameters.get(clicked)
        return [[clicked]] + model_hyper_style + styles


    @app.callback([Output('feature_selection_div', 'children'), 
                Output('feature_selection_hyperparameter_header', 'style'), 
                ], 
                Input("selection_type", "value"))
    def feature_selection(feature_selection):
        score_func = dash_component_label(label="score_func", 
                                    component_type="dropdown")
        def _helper(sel_type, score_func):
            if sel_type is None:
                return [[Dropdown(id="feature_selection_hyperparameter", style={'display':'none'}), 
                            Dropdown(id="score_func", style={'display': 'none'})], {'display': 'none'}]
            sel_type = sel_type.lower()
            if sel_type == 'selectkbest':
                kpars = dash_component_label(label='k',
                                    component_type='slider', 
                                    component_id="feature_selection_hyperparameter",
                                    component_kwargs={'min': 0, 
                                                    'max': 20, 
                                                    'step': 5, 
                                                    'value': 10})
                return [[kpars, score_func], {'display': 'grid'}]

            elif sel_type == "selectpercentile":
                percentile_pars = dash_component_label(label='percentile', 
                                            component_type='slider', 
                                            component_id="feature_selection_hyperparameter",
                                            component_kwargs={'min': 0, 
                                                            'max': 20, 
                                                            'step': 5, 
                                                            'value': 5})
                return [[percentile_pars, score_func], {'display': 'grid'}]
        return _helper(feature_selection, score_func)