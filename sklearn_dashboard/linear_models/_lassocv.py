
from ..preprocessing import preprocessor
from ..utils import (output_df,  
                    predicted_actual_plot, 
                    predicted_residual_plot, 
                    get_dataframe)
from ..metrics import regression_metrics as scoring_metrics

from sklearn.pipeline import Pipeline
from sklearn.linear_model import LassoCV, Lasso
from pandas import DataFrame, melt
import numpy as np
from copy import copy

from plotly.express import line, scatter
from dash.html import Div

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

hyper_search_type = {
    'gridsearchcv': GridSearchCV,
    'randomizedsearchcv': RandomizedSearchCV
}

        
def lassocv_output(X_train: DataFrame, 
            y_train: DataFrame,
            X_test: DataFrame,
            y_test: DataFrame = {},
            df_range: list = [1, 20],
            metrics: str = 'mean_squared_error',
            model_kwargs: dict = {}, 
            numeric_pipeline_kwargs: dict = {}, 
            categorical_pipeline_kwargs: dict = {}, 
            is_cv: str ='false', 
            search_type: str = 'GridSearchCV',
            alphas: list = [-39, 50],
            cv_kwargs : dict = {'cv': 5}):

    processor = preprocessor(numeric_pipeline_kwargs, categorical_pipeline_kwargs)
    pipe = Pipeline(
        steps=[
            ("preprocessor", processor),
            ("classifier", LassoCV(**cv_kwargs))
        ])

    if is_cv == 'true':
        alphas = np.linspace(alphas[0], alphas[1], num=100)
        param_grid = {
            'classifier__alpha': alphas
        }
        if search_type.lower() is None:
            search_method = GridSearchCV
        else:
            search_method = hyper_search_type[search_type.lower()]
        pipe.fit(X_train, y_train)
        df_predict_actual = DataFrame({'observation': range(len(X_test)), 
                    'predicted': np.round(pipe.predict(X_test), 2),
                    'actual': np.array(y_test)})
        df_table = copy(df_predict_actual)
        df_predict_actual_melt = melt(df_predict_actual[df_range[0]:df_range[1]], id_vars='observation', value_vars=['predicted', 'actual'])
        model = pipe[-1]
        mse_path = DataFrame(model.mse_path_)
        mse_path.columns = ['split' + str(j) for j in range(cv_kwargs['cv'])]
        alphas = model.alphas_
        mse_path.insert(0, 'alpha', alphas)
        colnames = list(mse_path.columns)
        #melt
        mse_path_melt = melt(mse_path, id_vars=colnames[0], value_vars=colnames[1:])
        plot_predicted = line(df_predict_actual_melt, x='observation', y='value', color='variable')
        plot_path = line(mse_path_melt, x='alpha', y='value', color='variable')
        #coefficients 
        coefs = model.coef_
        features = pipe.feature_names_in_
        coefs_features = DataFrame({'coef': coefs})
        # print(coefs)
        # print(features)
        predict_header = Div(children=['predicted vs actual target'], className='model-content-header')
        return ['', [predict_header, output_df(df_table), output_df(coefs_features)], plot_path, plot_predicted]
    else:
        model = pipe.fit(X_train, y_train)
    return [None, None, line(), line()]



 # model = search_method(estimator=pipe, param_grid=param_grid, **cv_kwargs)
        # model.fit(X_train, y_train)
        # _keys = ['param_classifier__alpha', 'mean_test_score'] + ['split' + str(j) +'_test_score' for j in range(cv_kwargs['cv'])]
        # df_results = DataFrame(model.cv_results_)[_keys]
        # df_melt = melt(df_results, id_vars=_keys[0], value_vars=_keys[1:])
        # df_melt.columns = ['alpha', 'split_number','test_score']
        # model.fit(X_train, y_train)
        # df_predict_actual = DataFrame({'observation': range(len(X_test)), 
        #             'predicted': model.predict(X_test),
        #             'actual': np.array(y_test)
        # })
        # df_predict_actual = df_predict_actual[df_range[0]:df_range[1]]
        # df_predict_actual_melt = melt(df_predict_actual, id_vars='observation', value_vars=['predicted', 'actual'])
        # plot_predicted = line(df_predict_actual_melt, x='observation', y='value', color='variable')
        # plot_cv = line(df_melt, x='alpha', y='test_score', color = 'split_number')