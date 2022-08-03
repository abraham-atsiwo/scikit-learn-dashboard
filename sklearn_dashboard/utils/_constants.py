
from sklearn_dashboard.utils import dash_component_label

dark_mode_style_yes = {"backgroundColor": "#222", "color": "hsl(212, 33%, 89%)"}
dark_mode_style_no = {"backgroundColor": "hsl(212, 33%, 89%)", "color": "black"}


estimator_type_categories_options = {
    "linear_models": ["ols", "lasso", 'lassocv'],
    "neighbors": ["k_nearest"]
}


#hyper parameters 
hyperparameters = {
    'ols': [],
    'lasso': [dash_component_label(label='alpha', component_type='slider', 
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': 5})],
    'lassocv': [dash_component_label(label='alpha', component_type='range_slider', 
                                    component_kwargs={'min': -20, 'max': 20, 'step': 5, 'value': [-5, 5]})]
}

_regression_metrics = ['mean_squared_error', 'mean_absolute_error']
_classification_metrics = ['mean_deviation']

scoring_metrics = {
    'regression': _regression_metrics,
    'classification': _classification_metrics
}


from sklearn import preprocessing
from sklearn.preprocessing import (StandardScaler, 
                                    MinMaxScaler, 
                                    MaxAbsScaler,
                                    RobustScaler, 
                                    QuantileTransformer, 
                                    PowerTransformer,
                                    OneHotEncoder,
                                    OrdinalEncoder,
                            )
preprocessing_numerical = {
                            "StandardScaler": StandardScaler, 
                            "MinMaxScaler": MinMaxScaler,
                            "MaxAbsScaler": MaxAbsScaler,
                            "RobustScaler": RobustScaler,
                            # "QuantileTransformer": QuantileTransformer,
                            # "PowerTransformer": PowerTransformer,
                        }

preprocessing_categorical = {"OneHotEncoder": OneHotEncoder, "OrdinalEncoder": OrdinalEncoder}