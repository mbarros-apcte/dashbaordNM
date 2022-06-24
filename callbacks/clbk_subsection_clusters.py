import time
import numpy as np
import pandas as pd
pd.set_option("display.max_columns", 40)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"
import plotly

import plotly.express as px

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from utils.user_inputs import get_predefined_user_inputs
from utils.utils import fetch_precomp_data

from sklearn.cluster import KMeans

def _get_num_clst(x):
    if 2 <= x <= 7:
        return 2
    elif x <= 17:
        return 3
    elif x <= 28:
        return 4
    elif x <= 39:
        return 5
    else:
        return 6


def _integrate_clstr_data(sec,sec_df,kmeans):
    sec_df["clstr"] = list(kmeans.labels_)
    sec_df["clstr_sec"] = sec_df["clstr"].apply(lambda x: f"{sec}-{x+1}")
    sec_df["clstr_cen"] = sec_df["clstr"].apply(lambda x: kmeans.cluster_centers_[x][0])
    return sec_df


def _add_columns_for_non_clstrd_data(sec,sec_df):
    sec_df["clstr"] = -1
    sec_df["clstr_sec"] = sec_df["clstr"].apply(lambda x: f"{sec}-{x+1}")
    sec_df["clstr_cen"] = sec_df["scr_fin_asset"]
    return sec_df



def make_homog_subsections(sig_df):
    df_all = pd.DataFrame(data=[])
    for sec in sig_df["Section"].unique():
        sec_df = sig_df[sig_df["Section"] == sec]
        sec_df.reset_index(inplace=True, drop="index")

        if sec > 0 and len(sec_df) > 2:
            df_clstr = pd.DataFrame(sec_df, columns=['scr_fin_asset'])
            num_clstr = _get_num_clst(len(sec_df))
            kmeans = KMeans(n_clusters=num_clstr).fit(df_clstr)

            sec_df = _integrate_clstr_data(sec,sec_df,kmeans)

        else:
            sec_df = _add_columns_for_non_clstrd_data(sec, sec_df)

        if len(df_all) == 0:
            df_all = sec_df
        else:
            df_all = pd.concat([df_all, sec_df])

    return df_all




if __name__ == '__main__':
    pickle_fnm = get_current_pickle_precom_file()
    prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

    # get the req inputs
    user_inputs = get_predefined_user_inputs(spat_agg="section-level")

    # get all figures
    sig_df = add_all_scores(prec_data, user_inputs)

    time_st = time.perf_counter()
    df_all = make_homog_subsections(sig_df)
    print(f'Total computation time is {int(time.perf_counter() - time_st)} seconds.')


    # test
    sec = sig_df.groupby(['Section'], as_index=False).agg(section_counts=('Section', 'count'))  # !!!
    fig = px.histogram(sec, x="section_counts")
    fig.show()