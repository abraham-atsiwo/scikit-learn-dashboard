from dash.dcc import Store
from dash import dcc 
from dash.html import Div
from typing import Dict

def store_layout(component_id_props: Dict) -> dcc:
    store_list = []
    for id, props in component_id_props.items():
        store_list.append(Store(id, props))
    return Div(store_list)


all_store_value = {
    "df" : "memory"
}

store_items = store_layout(all_store_value)