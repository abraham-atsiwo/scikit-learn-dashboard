
from ..utils import dash_component_label
from dash.dcc import Dropdown

order_of_components = ['slider', 'range_slider', 'dropdown', 'cv_type']
number_of_components = len(order_of_components)


hyperparameters = { 
    'ols': None,
    'lasso': dash_component_label(label='alpha', component_type='slider', 
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': 5}),
    'lassocv': dash_component_label(label='alpha', component_type='range_slider', 
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': [-5, 5]})
}

style_show = {'display':'grid'}
style_hide = {'display': 'none'}

show_hide_hyperparameters = {
    'ols': [style_hide]*number_of_components,
    'lasso': [style_show, style_hide, style_hide, style_show],
    'lassocv': [style_show, style_hide, style_hide, style_show]
}