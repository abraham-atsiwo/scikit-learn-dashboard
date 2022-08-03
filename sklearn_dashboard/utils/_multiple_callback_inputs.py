from dash import Input, Output, State 
from typing import List, Dict

def multiple_callback_inputs(component_id: List, props: List) -> Dict:
    if isinstance(component_id, list):
        assert len(props) == len(component_id)
        if len(component_id) == 1:
            return Input(component_id, props)
        n_component_id = len(component_id)    
        all_inputs = {component_id[ind]: Input(component_id[ind], props[ind]) 
                            for ind in range(n_component_id)}
                            
        inputs = {"all_inputs": all_inputs}
        return inputs 
    raise TypeError


def multiple_callback_output(component_id: List, props: List) -> Dict:
    if component_id is not None and props is not None:
        assert len(component_id) == len(props)
        if len(component_id) == 1:
            return Output(component_id, props)
        return [Output(id, prop) for id, prop in zip(component_id, props)]
    raise TypeError

def multiple_callback_input_state(input_id: List, 
                        input_props: List, 
                        state_id: List, 
                        state_props: List) -> Dict:
    if input_props and input_id:
        assert len(input_props) == len(input_id) \
            and len(state_props) == len(state_id)
        
        inputs = [Input(id, prop) for id, prop in zip(input_props, input_id)]
        state = [Input(id, prop) for id, prop in zip(state_props, state_id)]
        return inputs + state
    raise ValueError
        

