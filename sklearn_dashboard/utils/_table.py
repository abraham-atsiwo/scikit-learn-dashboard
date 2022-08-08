from dash.html import Div
from dash.dash_table import DataTable
import numpy as np
from pandas import DataFrame

def output_df(df):
    return Div([
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

def unpivot(frame):
    N, K = frame.shape
    data = {
        "target": frame.to_numpy().ravel("F"),
        "type": np.asarray(frame.columns).repeat(N),
        "observation": np.tile(np.asarray([j for j in range(N)]), K),
    }
    return DataFrame(data, columns=["observation", "type", "target"])