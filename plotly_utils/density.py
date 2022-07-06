import pickle

import dash
import dash_core_components as dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from data_preparation.process_prec_scores import convert_to_df_precomp_data

df = px.data.tips()



@app.callback(
    Output("box-plot", "figure"),
    [Input("x-axis", "value"),
     Input("y-axis", "value")])
def generate_chart(x, y):
    print(f"x is {x} type is {type(x)}")
    print(f"y is {y} type is {type(y)}")
    print(f" columns are {df_all.columns}")
    temp = df_all
    temp = temp[temp["scorer_name"].isin(x)]
    fig = px.box(temp, x="scorer_name", y=y, color="cluster")
    return fig

app.run_server(port='8022')