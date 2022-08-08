from dash.dcc import Store
from dash import dcc 
from dash.html import Div, Span
from typing import Dict

def store_layout(component_id_props: Dict) -> dcc:
    store_list = []
    for id, props in component_id_props.items():
        store_list.append(Store(id))
    return Span(store_list, style={"display": "hidden"}, className="store")


all_store_value = {
    "df" : "session",
    "df_columns": "session",
    'parameters': 'session',
    'hidden': 'session',
}

store_items = store_layout(all_store_value)