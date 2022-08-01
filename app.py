from sklearn_dashboard import app
from sklearn_dashboard.layout import *
from dash.html import Div

from sklearn_dashboard.utils import *
from sklearn_dashboard.callback import *


model_container = Div(
                    children=[Div([store_items, load_data_items, preprocessing_layout()], 
                        id="model_content", 
                        className="model-content")], 
                    className="model-container", 
                        id="model-container")
app.layout = Div(children=[navbar_items, model_container])

multi_purpose_callback(app)

if __name__ == '__main__':
    app.run_server(debug=True)
