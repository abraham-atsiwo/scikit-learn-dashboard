
from dash import Output, Input 
from dash.exceptions import PreventUpdate

from ..utils import multiple_callback_output
from ..metrics import scoring_metrics

id = ["target_regression_div", "target_classification_div", 
                "target_regression_header", "target_classification_header", "metrics", "metrics"]
props = ["style"]*(len(id)-2) + ['options', "value"]

#id props for hiding options for cross validation
cv_id = ["n_fold_header", "n_fold_div"] 
cv_props = ["style", "style"] 

def other_feature_processing_callback(app):
    @app.callback(multiple_callback_output(id, props),
            Input("estimator_type", "value"))
    def show_hide_target_preprocessing(estimator_type):
        style_false = {"display": "none"}
        style_true = {"display": "grid"}
        if estimator_type:
            if estimator_type == "regression":
                output = [style_true, style_false]*2 
                metrics = list(scoring_metrics[estimator_type].keys())
                output.extend([metrics] + [metrics[0]])
                return output
            elif estimator_type == "classification":
                output = [style_false, style_true]*2
                metrics = list(scoring_metrics[estimator_type].keys())
                output.extend([metrics] + [metrics[0]])
                return output
        return [style_false, style_false, style_false, style_false, [], None]


    @app.callback(multiple_callback_output(cv_id, cv_props), 
            Input("cross_validate", "value"))
    def hide_cv(cv_type):
        if not cv_type or cv_type == 'false':
            return [{"display": "none"}]*len(cv_id)
        return [{"display": "grid"}]*len(cv_id)

    
    

    
