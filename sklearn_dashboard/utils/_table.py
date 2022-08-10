from dash.html import Div
from dash.dash_table import DataTable
import numpy as np
from pandas import DataFrame

from plotly.express import line, scatter

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


def predicted_actual_plot(predicted, actual):
    df_predict_actual = get_dataframe(predicted, actual)
    df = unpivot(df_predict_actual)
    plot_predicted_actual = line(df, x='observation', 
                                y='target', 
                                color='type', 
                                line_dash='type')
    return plot_predicted_actual

def predicted_residual_plot(standardized_residuals, predicted):
    plot_residual = scatter(y=standardized_residuals, x=predicted, 
                        labels={'x': 'predicted target',    
                                'y': 'standardized residuals'},
                        title="predicted values vs. standardized residuals")
    plot_residual.add_hline(y=0)
    return plot_residual

def get_dataframe(predicted, actual):
    df_predict_actual = DataFrame({'predicted': predicted, 
                                   'target': np.round(np.array(actual), 2)})
    return df_predict_actual