
from sklearn import linear_model
from ..preprocessing import preprocessor
from ..utils import output_df
from ..metrics import regression_metrics as scoring_metrics

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from pandas import DataFrame
import numpy as np

from plotly.express import line, scatter
from dash.dash_table import DataTable
from dash.html import Div

from sklearn.preprocessing import StandardScaler

from ..utils import predicted_actual_plot, predicted_residual_plot, get_dataframe

        
def ols_output(X_train: DataFrame, 
            y_train: DataFrame,
            X_test: DataFrame,
            y_test: DataFrame = {},
            df_range: list = [0, 200],
            metrics: str = 'mean_squared_error',
            model_kwargs: dict = {}, 
            numeric_pipeline_kwargs: dict = {}, 
            categorical_pipeline_kwargs: dict = {}, 
            is_cv: str ='false', 
            cv_kwargs : dict = {'cv': 5}):

    processor = preprocessor(numeric_pipeline_kwargs, categorical_pipeline_kwargs)
    pipe = Pipeline(
        steps=[
            ("preprocessor", processor),
            ("classifier", LinearRegression(**model_kwargs))
        ])
    pipe.fit(X_train, y_train)
    predicted = np.round(pipe.predict(X_test), 2)
    plot_predicted_actual = predicted_actual_plot(predicted[df_range[0]:df_range[1]], 
                                                    y_test[df_range[0]:df_range[1]])
    # plot_predicted_actual = predicted_actual_plot(predicted, 
    #                                                 y_test)
    error = predicted - np.array(y_test)
    scaler = StandardScaler()
    standardized_residuals= scaler.fit_transform(error.reshape(-1, 1)).flatten()
    plot_residual = predicted_residual_plot(standardized_residuals, predicted)

    #model description area

    #metrics
    metrics_selected = scoring_metrics.get(metrics)
    train_metrics = metrics_selected(pipe.predict(X_train), np.array(y_train))
    test_metrics = metrics_selected(pipe.predict(X_test), np.array(y_test))
    # print(test_metrics)
    metrics_df = DataFrame({'train': [np.round(train_metrics, 2)], 
                            'test': [np.round(test_metrics, 2)]})
    # print(metrics_df)
    metrics_df = output_df(metrics_df)

    data_header = Div("prediction on test set", className="model-content-header")
    data_style = output_df(get_dataframe(predicted, y_test))
    scoring_header = Div(metrics, className="model-content-header")
    model_description = [data_header, data_style, scoring_header, metrics_df]
    n = len(y_test)
    if is_cv == 'false' or is_cv is None:
        return [model_description, plot_residual, plot_predicted_actual]
    else:
        cross_validation = cross_val_score(pipe, X_train, y_train, **cv_kwargs)
        n = range(1, len(cross_validation) + 1)
        cv_plot = line(x=n, y=cross_validation, labels={'x': 'n_fold', 'y': 'cross validation error'})
        # print(cross_validation)
        return [model_description, cv_plot, plot_predicted_actual]


