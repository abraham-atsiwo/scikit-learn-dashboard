
from collections import OrderedDict
from sklearn.metrics import (mean_squared_error, 
                            mean_absolute_error, 
                            mean_absolute_percentage_error, 
                            r2_score, 
                            explained_variance_score,
                            median_absolute_error)

#classification metrics 
from sklearn.metrics import (accuracy_score, 
                            f1_score, precision_score, 
                            log_loss)
from sklearn.preprocessing import OrdinalEncoder


regression_metrics = OrderedDict({'mean_squared_error': mean_squared_error,
                        'mean_absolute_error': mean_absolute_error,
                        'mean_absolute_percentage_error': mean_absolute_percentage_error, 
                    })
classification_metrics = OrderedDict({'accuracy_score': accuracy_score, 
                            'f1_score': f1_score, 
                            'precision_score': precision_score, 
                            'log_loss': log_loss
                })

scoring_metrics = OrderedDict({
    'regression': regression_metrics,
    'classification': classification_metrics
})

