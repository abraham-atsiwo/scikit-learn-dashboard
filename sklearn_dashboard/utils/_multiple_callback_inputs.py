from dash import Input, Output, State 
from typing import List, Dict

def multiple_callback_inputs(component_id: List, props: List) -> Dict:
    if isinstance(component_id, list):
        n_component_id = len(component_id)    
        all_inputs = {component_id[ind]: Input(component_id[ind], props[ind]) 
                            for ind in range(n_component_id)}
                            
        inputs = {"all_inputs": all_inputs}
        return inputs 
    raise TypeError