

from dash.html import Div, Hr
from typing import List

from itsdangerous import NoneAlgorithm

from ..utils import dash_component_label

def other_processing_layout(children: List):
    return Div(children=children, 
                className="other-preprocessing-wrapper", 
                id="other_preprocessing")

#add components

def _helper_component(parameters: dict):
        if parameters is None:
                return 
        for _, pars in parameters.items():
                header = pars['header']
                props = pars['props']
                if props['component_type'] == 'div':
                        header_id = header.replace(" ", "_").strip().lower()+"_header"
                else:
                        header_id = props["label"].replace(" ", "_").strip().lower()+"_header"
                _header = Div(header, className="model-content-header", 
                                id=header_id, 
                                style={"marginTop": "5px"})
                if props["component_type"] == 'div':
                        _component = Div(**props["component_kwargs"], style={'marginTop': '5px'})
                else:
                        _component = dash_component_label(**props)
                item = Div([_header, _component])
                yield item
        
        

pars_label_col1 = {
        "selection_type": {
                "header": "Univariate feature selection",
                "props": {
                        "label": "selection type", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": ["SelectKBest", "SelectPercentile"]}
                }
        },
        "imputation": {
                "header": "missing value imputation",
                "props": {
                        "label": "imputation", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": ["mean", "median", "most_frequent"], 
                                                "value": "mean"}
                }
        },
        "target": {
                "header": "select target",
                "props": {
                        "label": "select target", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": [], 'clearable': False}
                }
        },
        "target_preprocessing_reg": {
                "header": "target transformation",
                "props": {
                        "label": "target regression", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": ["QuantileTransformer", "PowerTransformer"], 
                                                "value": None}
                }
        },
        "target_preprocessing_cat": {
                "header": "target transformation",
                "props": {
                        "label": "target classification", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": ["OneHotEncoder","OrdinalEncoder"], 
                                                "value": None}
                }
        },
        "scoring_metrics": {
                "header": "scoring metrics",
                "props": {
                        "label": "metrics", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": [], 'clearable': False,
                                                "value": None}
                }
        }
}


other_processing_col1 = Div(children=list(_helper_component(pars_label_col1)), 
            className="other-preprocessing-col1", 
            id="other_preprocessing_col1")

pars_label_col2 = {
        "train_test_split": {
                "header": "train test split",
                "props": {
                        "label": "train proportion", 
                        "component_type": "slider",
                        "component_kwargs": {"min": 0.5, "max": 0.9, "step": 0.1, "value": 0.6}
                }
        },
        "cross_validation": {
                "header": "cross validation type",
                "props": {
                        "label": "cross validate", 
                        "component_type": "dropdown",
                        "component_kwargs": {"options": ['true', 'false'], 'value': 'false'}
                }
        },
        "n_fold": {
                "header": "select n_fold",
                "props": {
                        "label": "n_fold", 
                        "component_type": "slider",
                       "component_kwargs": {"min": 5, "max": 35, "step": 5, "value": 5},
                }
        },
        #  "hyper_parameters": {
        #         "header": "tuning hyperparameters",
        #         "props": {
        #                 "label": "alpha", 
        #                 "component_type": "div",
        #                "component_kwargs": {"children": [], "id": "tuning_hyperparametes_div"},
        #         }
        # },
        # "cv_type": {
        #         "header": "Search type",
        #         "props": {
        #                 "label": "cv type", 
        #                 "component_type": "dropdown",
        #                "component_kwargs": {"options": ['GridSearchCV', 'RandomSearchCV']},
        #         }
        # },
        "hyper_selectkbest": {
                "header": "feature selection hyperparameter",
                "props": {
                        "label": "feature selection", 
                        "component_type": "div",
                       "component_kwargs": {"children": [], "id": "feature_selection_div"},
                }
        },
        # "hyper_select_percentile": {
        #         "header": "feature selection hyperparameter",
        #         "props": {
        #                 "label": "select_percentile", 
        #                 "component_type": "div",
        #                "component_kwargs": {"children": [], "id": "select_percentile_div"},
        #         }
        # },
        # "hyper_slider": {
        #         "header": "tuning hyperparameter1",
        #         "props": {
        #                 "label": "alpha", 
        #                 "component_type": "slider",
        #                "component_kwargs": {"min": 5, "max": 35, "step": 5, "value": 5},
        #         }
        # },

        # "hyper_dropdown": {
        #         "header": "tuning hyperparameter2",
        #         "props": {
        #                 "label": "k_subset", 
        #                 "component_type": "dropdown",
        #                "component_kwargs":{"options": []},
        #         }
        # },

        # "range_slider": {
        #         "header": "tuning hyperparameter3",
        #         "props": {
        #                 "label": "alpha range", 
        #                 "component_type": "range_slider",
        #                "component_kwargs": {"min": 5, "max": 35, "step": 5, "value": [10, 15]},
        #         }
        # },
               
}

#hyperparameters 
hyper_header = Div(['Tuning hyperparameters'], className="model-content-header", 
                                                id='tuning_hyperparametes_div')
hyper_par1 = dash_component_label(label='hyper_par1', component_type='slider', component_id='hyper_slider',
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': 5})
hyper_par2 = dash_component_label(label='hyper_par2', component_type='range_slider', component_id = 'hyper_range_slider',
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': [5, 10]})
hyper_par3 = dash_component_label(label='hyper_par3', component_type='dropdown', component_id = 'hyper_dropdown',
                                    component_kwargs={})

grid_search = dash_component_label(label='cv_type', component_type='dropdown', 
                                  component_kwargs={'options': ['GridSearchCV', 'RandomSearchCV']})

#hyper contents
hyper_content = [hyper_header, hyper_par1, hyper_par2, hyper_par3, grid_search]
content_from_dict = list(_helper_component(pars_label_col2))
content_from_dict = content_from_dict + hyper_content

other_processing_col2 = Div(content_from_dict, 
                                        className="other-preprocessing-col2", 
                                        id="other_preprocessing_col2")

other_processing_items = other_processing_layout([other_processing_col1, other_processing_col2])


