from dash.html import Div, Label 
from dash.dcc import Dropdown, Upload, RangeSlider, Slider, RadioItems
from dash import dcc
from typing import Optional, Dict
from dash.html import Div

from ..utils import classname_id_generator


component_options = {
                    "dropdown": Dropdown, 
                    "upload": Upload, 
                    'div': Div,
                    "slider": Slider,
                    "range_slider": RangeSlider,
                    "radio_items": RadioItems,
                }

def get_component(component_type):
    component_keys = list(component_options.keys())
    if isinstance(component_type, str):
        if component_type in component_keys:
            return component_options[component_type]
    else:
        raise TypeError


def dash_component_label(label: str, 
                        component_type: str, 
                        component_classname: str = "component-item", 
                        component_id: str = None,
                        component_id_prefix: str = None,
                        label_kwargs: Dict = {}, 
                        component_kwargs: Dict = {}, 
                        label_classname: str = "component-label", 
                        div_classname: str = "component-label-item-wrapper") -> dcc:

    #verify component type 
    component = get_component(component_type)
    #get auto id 
    if component_id is None: 
        get_id = classname_id_generator(component_id_prefix, label)
    else:
        get_id = component_id

    _label = Label(label, className=label_classname, **label_kwargs)
    _component = Div(component(id=get_id, **component_kwargs, className=component_classname), 
                    className=component_classname+'-div')
    return Div(
                children=[_label, _component], className=div_classname, id=get_id+"_div")