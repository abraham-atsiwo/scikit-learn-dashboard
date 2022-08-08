from collections import OrderedDict
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn_dashboard import preprocessing
from sklearn.compose import ColumnTransformer, make_column_selector

from numpy import number

from sklearn import preprocessing
from sklearn import pipeline
from sklearn.preprocessing import (StandardScaler, 
                                    MinMaxScaler, 
                                    MaxAbsScaler, 
                                    RobustScaler, 
                                    OneHotEncoder, 
                                    OrdinalEncoder)


preprocessing_numeric_options = OrderedDict({
    'MinMaxScaler': MinMaxScaler(),
    'StandardScaler': StandardScaler(),
    'MaxAbsScaler': MaxAbsScaler(),
    'RobustScaler': RobustScaler(),
})

preprocessing_categorical_options = OrderedDict({
    'OneHotEncoder': OneHotEncoder(),
    'OrdinalEncoder': OrdinalEncoder(),
})


def _preprocessing_numeric_pipeline(strategy: str, 
                                   type: preprocessing) -> pipeline:
    if strategy is None:
        strategy = 'mean'
    if type:    
        return Pipeline(
            steps=[
                    ("imputation", SimpleImputer(strategy=strategy)), 
                    ("numeric_features", type)
            ])
    return Pipeline(
        steps=[
                ("imputation", SimpleImputer(strategy=strategy))
        ])

def _preprocessing_categorical_pipeline(type: preprocessing) -> pipeline:
    if type:
        return Pipeline(
            steps=[
                ("categorical_features", type)
            ])
    return None

def preprocessor(numeric_pipeline_kwargs: dict, 
                categorical_pipeline_kwargs: dict):
    numeric_pipeline = _preprocessing_numeric_pipeline(**numeric_pipeline_kwargs)
    categorical_pipeline = _preprocessing_categorical_pipeline(**categorical_pipeline_kwargs)
    #building pipeline
    if categorical_pipeline:
        return ColumnTransformer([
            ("numerical", numeric_pipeline, make_column_selector(dtype_include=number)),
            ("categorical", categorical_pipeline, make_column_selector(dtype_include=object))
        ])
    return ColumnTransformer([
            ("numerical", numeric_pipeline, make_column_selector(dtype_include=number)),
    ])



