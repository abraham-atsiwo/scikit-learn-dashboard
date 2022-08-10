
from dash import Input, Output, callback_context as ctx
from dash.dcc import Graph
from json import dumps
from pandas import read_json
from plotly.express import line, scatter

from sklearn.model_selection import cross_validate, train_test_split

from ..utils import multiple_callback_inputs, multiple_callback_output
from ..preprocessing import *
from ..linear_models import *
from sklearn_dashboard import preprocessing


def validate_df(df, msg='please select dataset'):
    if df is None:
        return None, msg
    return df, None

def validate_parameters(pars, msg="select model parameters"):
    if pars is None:
        return None, msg
    return pars, None


input_id = ['estimator_type', 'estimator_type_categories', 'numeric_dtypes_features', 
            'categorical_dtypes_features', 'preprocessing_categorical', 'cross_validate',
            'preprocessing_numeric', 'selection_type', 'imputation', 'train_proportion',
            'cv_type', 'metrics', 'select_target', 'n_fold', 'target_regression', 
            'target_classification', 'score_func', 'feature_selection_hyperparameter', 
            'hyper_slider', 'hyper_dropdown', 'hyper_range_slider',
]
input_props = ['value']*len(input_id)
def model_callback(app):
    @app.callback([Output('select_df_range', 'max')], 
                [Input('df', 'data'), Input('train_proportion', 'value')])
    def select_df_range(df, proportion):
        df = read_json(df, orient='split')
        n = len(df)*(1-proportion)
        return [n]


    @app.callback(Output('parameters', 'data'),
        inputs = multiple_callback_inputs(input_id, input_props)
    )
    def get_parameters(all_inputs):
        return all_inputs

    @app.callback(
        multiple_callback_output(['error', 'model_description', 'model_graph_prediction', 'model_graph_others'],
        ['children', 'children', 'figure', 'figure']),
        [Input('fit_model', 'value'), Input('parameters', 'data'), 
        Input('df', 'data'), Input('select_df_range', 'value'), 
        Input('estimator_type_categories_options', 'n_clicks')]
    )
    def fit_model_update_graph(fit_model, parameters, df, df_range, estimator_type_options):
        if df is None:
            return ['please upload dataset', 'Hello', line(), line()]
        if parameters is None:
            return ["click to select model", 'Hello', line(), line()]
    
        for val in ["estimator_type", "estimator_type_categories",
                    "numeric_dtypes_features", "categorical_dtypes_features"]:
            if parameters[val] is None:
                return [val + " cannot be none", 'Hello', line(), line()]
        features_label = parameters["numeric_dtypes_features"] + parameters["categorical_dtypes_features"]
        target_label = parameters['select_target']
        if len(features_label) == 0 or len(target_label) == 0:
            return ['dataset nothj found ', 'Hello', line(), line()]
        dataset = read_json(df, orient='split')
        features = dataset[features_label]
        target = dataset[target_label]
        #train test split
        X_train, X_test, y_train, y_test = train_test_split(features, target, random_state=0,
                                                train_size=parameters['train_proportion'])

        #fit and select model parameters
        numeric = preprocessing_numeric_options.get(parameters['preprocessing_numeric'])
        categorical = preprocessing_categorical_options.get(parameters['preprocessing_categorical'])
        numerical_pipeline_kwargs = {'strategy': parameters['imputation'], 
                                    'type': numeric
                                }
        categorical_pipeline_kwargs = {'type': categorical}
        is_cv = parameters['cross_validate']
        cv_kwargs = {'cv': parameters['n_fold']}
        metrics = parameters['metrics']
        output = ['Hello', 'Amando', line(), line()]
        #required parameters 
        required_pars = {'X_train':X_train, 
                        'y_train': y_train,
                        'X_test': X_test,
                        'y_test': y_test,
                        'df_range': df_range,
                        'metrics': metrics,
                        'numeric_pipeline_kwargs': numerical_pipeline_kwargs,
                        'categorical_pipeline_kwargs': categorical_pipeline_kwargs,
                        'is_cv': is_cv,
                        'cv_kwargs': cv_kwargs,
        }
        if fit_model:
            if fit_model == 'ols':
                model_kwargs = {}
                output = ols_output(**required_pars,
                                    model_kwargs=model_kwargs)
                return ['datasetkkk not found ', output[0], output[1], output[2]]
            if fit_model == 'lasso':
                model_kwargs = {}
                output = lassocv_output(**required_pars, 
                                        model_kwargs=model_kwargs)
                return output
            return ['da not found', 'This world', line(), line()]
        return ['datask not found', 'This world', line(), line()]
        
        

