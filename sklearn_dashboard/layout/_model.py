from dash.html import Div, Button, Label
from dash.dcc import Graph, Dropdown

from ..utils import dash_component_label


def model_layout(children):
    return Div(children=children, 
            className="model-wrapper", 
            id="model")

n = 1000
data_range = dash_component_label(label="select_df_range", 
                                    component_type='range_slider', 
                                    component_kwargs={'min': 0, 
                                                     'max': n, 
                                                     'value': [0, min(200, n)],
                                                    #  'step': n//5
                                    })
header_item = Div(dash_component_label(label="FIT MODEL", component_type='dropdown'), style={'minWidth': '300px'})
header = Div(children=[header_item, data_range], className = "model-header", id="model_header")
#error categories 
model_time = Div(children=[], className='error-time error-item')
model_error = Div(className="error-item error-instruction")
model_others = Div(className='error-item error-others')
error = model_graph_prediction = Div(children=[model_time, model_error, model_others], className='error', id='error') 
model_description = Div(children=['hello world'], className="model-description", id="model_description")
model_graph_others = Div(children=[Graph(id="model_graph_others", config={'autosizable': True})], 
                        className="model-graph-others") #Graph(id="model_graph_others")
model_graph_prediction = Div(children=[Graph(id='model_graph_prediction', config={'autosizable': True})], 
                        className='model-graph-prediction') #Graph(id='model_graph_prediction')

#model graph 
model_graph = Div(children=[model_graph_prediction, model_graph_others], className='model-graph', id='model_graph')

model_items = model_layout([
                            header,
                            error,
                            model_description, 
                            model_graph,
                        ])