
from dash import Input, Output, State, callback_context as ctx
from dash.dcc import Upload
from dash.html import Div

from ..utils import dash_component_label

from sklearn_dashboard import app

def load_dataset_callback(app):
    @app.callback(Output("default_upload", "children"), 
                Input("data_options", "value")
    )
    def data_options_components(data_options):
        if data_options:
            data_val = data_options.lower()
            if data_val == "default_dataset":
                return dash_component_label(label=data_options, 
                        component_type="dropdown",
                        component_kwargs={"options": []})
            elif data_val == "upload_dataset":
                return dash_component_label(label="upload_dataset", 
                                            component_kwargs={
                                                "style": {"color": "white", 
                                                    "cursor": "pointer", "textAlign": "center",
                                                    "padding": "7px",
                                                    "border": "1px dashed"},
                                                "children": Div("click to upload [csv, txt]")},
                                            component_type="upload")
        return []





        