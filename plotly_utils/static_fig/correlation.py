import pickle
import plotly
import plotly.figure_factory as ff

import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from data_preparation.process_prec_scores import convert_to_df_precomp_data


def make_figure_sns(data):
    corr = data.corr()
    ax = sns.heatmap(
        corr,
        vmin=-1, vmax=1, center=0,
        cmap=sns.diverging_palette(20, 220, n=200),
        square=True
    )
    ax.set_xticklabels(
        ax.get_xticklabels(),
        rotation=45,
        horizontalalignment='right'
    );
    return ax

def make_figure_plotly(data):
    df_corr = data.corr()
    x = list(df_corr.columns)
    y = list(df_corr.index)
    z = np.array(df_corr)

    fig = go.Figure()
    fig.add_trace(
        go.Heatmap(
            x=df_corr.columns,
            y=df_corr.index,
            z=np.array(df_corr),
            #annotation_text=np.around(z, decimals=2),
            colorscale='Viridis'
        )
    )
    return fig

def get_correlation_fig(prec_data):
    col_of_int = ['week_plans', 'wknd_plans', 'week_tods', 'wknd_tods', 'week_free', 'wknd_free', 'max_cycle', 'min_cycle', 'veh_phs', 'any_veh_phs', 'ped_nc_phs', 'spec_ped_treat', 'preemption', 'ovrlps', 'lead_lag', 'tot_num_nearby_assets', 'any_int_within_thrs', 'distance_to_ramp']

    scr_df = convert_to_df_precomp_data(prec_data)
    scr_df = scr_df[col_of_int]

    fig = make_figure_plotly(scr_df)
    return fig



if __name__ == '__main__':
    pickle_fnm = get_current_pickle_precom_file()
    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)

    fig = get_correlation_fig(prec_data)
    plotly.offline.plot(fig, filename="_outputs\\corr.html")