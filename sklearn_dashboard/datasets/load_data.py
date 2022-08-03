import os 
import glob
from pandas import read_csv
from sklearn.datasets import fetch_california_housing, load_breast_cancer, load_diabetes


# default_datasets = {'breast_cancer': load_breast_cancer(), 
#                     'boston': fetch_california_housing(),
#                     'load_diabetes': load_diabetes()
# }

default_datasets = {}


path = os.getcwd()
path_mod = os.path.join(path, "sklearn_dashboard/datasets")
csv_files = glob.glob(os.path.join(path_mod, "*.csv"))
csv_name = glob.glob(os.path.join(path_mod, "*.txt"))
data_counter = 1

for f in csv_files:
      
    # read the csv file
    df = read_csv(f)
    default_datasets["dataset "+str(data_counter)] = df
    data_counter = data_counter + 1



