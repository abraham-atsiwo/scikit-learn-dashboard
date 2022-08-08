
from dash import Input, Output, callback_context as ctx

from sklearn_dashboard.utils import multiple_callback_inputs, dark_mode_style_yes, dark_mode_style_no

output_model_content_item_id = ["load_dataset", "preprocessing", "pipeline", "other_preprocessing_col1", 'model',
                            "estimator_info", "output_datatable", "other_preprocessing", "other_preprocessing_col2"]
input_dark_mode_id = ["dark_mode_yes", "dark_mode_no"]
input_dark_mode_props = ["n_clicks"]*len(input_dark_mode_id)

input_dark_mode = multiple_callback_inputs(input_dark_mode_id, input_dark_mode_props)


def multi_purpose_callback(app):
    @app.callback([Output(id, "style") for id in output_model_content_item_id], 
       inputs = {
            "all_inputs": input_dark_mode
       }
    )
    def toggle_model_content_background(all_inputs):
        clicked = ctx.triggered_id
        n_output = len(output_model_content_item_id)
        if clicked == "dark_mode_no":
            return [dark_mode_style_no for j in range(n_output)]
        return [dark_mode_style_yes for j in range(n_output)]
