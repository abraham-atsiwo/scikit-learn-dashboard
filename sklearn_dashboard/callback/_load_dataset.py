
from dash import Input, Output, State, callback_context as ctx
from dash.html import Div, Hr
from dash.dash_table import DataTable
from dash.exceptions import PreventUpdate

from operator import itemgetter


import base64
import io 
from pandas import read_csv, read_excel, read_json
from json import dumps, loads

from ..utils import multiple_callback_output, multiple_callback_inputs

from sklearn_dashboard.datasets.load_data import default_datasets
df_options = list(default_datasets.keys())

# print(df_options)


def parse_contents(contents, filename, date, default):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            # Assume that the user uploaded a CSV file
            df = read_csv(
                io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            # Assume that the user uploaded an excel file
            df = read_excel(io.BytesIO(decoded))
    except Exception as e:
        print(e)
        return default
    return df


def output_df(df, date, filename,contents):
    return Div([
        Hr(),
        # Div("Sample data"),
        DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns],
            page_size=10, 
            editable=True,
            id="table",
            style_table={
                'color': 'black',
                'overflowX': 'scroll',
                'width': '100%',
            },
            style_cell={'textAlign': 'left'},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)',
                }
            ],
            style_header={
                'backgroundColor': 'rgb(210, 210, 210)',
                'color': 'black',
                'fontWeight': 'bold'
            }
            ),
    ])

def load_dataset_callback(app):
    @app.callback([Output("default_dataset_div", "style"), Output("upload_dataset_div", "style")], 
                Input("data_options", "value")
    )
    def data_options_components(data_options):
        styles_show = {"display": "grid"}
        styles_hide = {"display": "none"}
        if data_options:
            data_val = data_options.lower()
            if data_val == "default_dataset":
                return [styles_show, styles_hide]
            elif data_val == "upload_dataset":
                return [styles_hide, styles_show]
        return [styles_hide, styles_hide]


    id = ['df', "output_datatable", "numeric_dtypes_features", "categorical_dtypes_features", "df_columns"]
    props = ['data', "children", "options", "options", "data"]
    @app.callback(
            multiple_callback_output(id, props), 
            [
                Input("default_dataset", "value"),
                Input("upload_dataset", "contents"), 
                State("upload_dataset", "filename"),
                State("upload_dataset", "last_modified")
            ])
    def get_dataframe(default, content, file, date):
        if content is not None:
            df = parse_contents(content, file, date, default_datasets[default])
        else:
            df = default_datasets[default]
        dff = df.to_json(date_format='iso', orient='split')
        df_table = output_df(df, date, file, content)
        columns_numeric = list(df.select_dtypes("number").columns)
        columns_categorical = list(df.select_dtypes("object").columns)
        #remove target from list if not none 
        columns = dumps({"numeric": columns_numeric, "categorical": columns_categorical})
        return [dff, df_table, columns_numeric, columns_categorical, columns]

    id = ["select_target", "select_target"]
    props = ["options", "value"]
    @app.callback(multiple_callback_output(id, props),
        [Input("estimator_type", "value"), Input("df_columns", "data")]
    )
    def update_target_options(estimator_type, df_columns):
        col = loads(df_columns)
        columns_numeric = col["numeric"]
        columns_categorical = col["categorical"]

        if estimator_type == "regression":
            return [columns_numeric, columns_numeric[0]]
        elif estimator_type == "classification":
            return [columns_categorical, columns_categorical[0]]
        return [[], ""]

    id = ["numeric_dtypes_features", "categorical_dtypes_features"]
    props = ["value", "value"]
    input_id = ["df_columns", "estimator_type", "select_target", 
                "numeric_dtypes_features", "categorical_dtypes_features"]
    input_props = ["data"] + ["value"]*4
    @app.callback(multiple_callback_output(id, props),
        inputs = multiple_callback_inputs(input_id, input_props)
        
    )
    def update_target_options(all_inputs):
        column_label = (tuple(all_inputs.keys()))
        df_columns, estimator_type, target, numeric, categorical = \
                itemgetter(*column_label)(all_inputs)
        colnames = loads(df_columns)
        if target:
            if estimator_type == "regression":
                if target in numeric:
                    numeric.remove(target)
            elif estimator_type == "classification":
                if target in categorical:
                    categorical.remove(target)
        return [numeric, categorical]
            
    




        