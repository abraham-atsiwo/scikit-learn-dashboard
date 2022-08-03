from sklearn_dashboard import app
from sklearn_dashboard.layout import *
from dash.html import Div

from sklearn_dashboard.utils import *
from sklearn_dashboard.callback import initialise_callback

output_datatable = Div(className="output-datatable model-content-item", id="output_datatable")

model_container = Div(
                    children=[Div([estimator_info_items, load_data_items, preprocessing_items, 
                                pipeline_items, output_datatable,  other_processing_items, store_items], 
                        id="model_content", 
                        className="model-content")], 
                    className="model-container", 
                        id="model-container")
app.layout = Div(children=[navbar_items, model_container])

initialise_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True)
