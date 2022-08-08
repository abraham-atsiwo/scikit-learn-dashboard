from ._utils_multi import multi_purpose_callback
from ._load_dataset import load_dataset_callback
from ._navbar import navbar_callback
from ._estimator_info import estimator_info_callback
from ._other_feature_preprocessing import other_feature_processing_callback
from ._model import model_callback


def initialise_callback(app):
    navbar_callback(app)
    load_dataset_callback(app)
    multi_purpose_callback(app)
    estimator_info_callback(app)
    other_feature_processing_callback(app)
    model_callback(app)



__all__ = [ 
            "initialise_callback",
            "multi_purpose_callback", 
            "navbar_callback", 
            "load_dataset_callback",
            "estimator_info_callback",
            "other_feature_processing_callback",
            "model_callback",
        ]