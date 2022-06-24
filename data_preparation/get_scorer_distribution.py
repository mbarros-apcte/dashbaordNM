import pickle

import pandas as pd
pd.options.mode.chained_assignment = None # Ignore Warnings
pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from data_preparation.process_prec_scores import convert_to_df_precomp_data

def  _get_cluster_from_clmn(x):
    if x in ["week_plans",  "wknd_plans",  "week_tods",  "wknd_tods",  "week_free", 'wknd_free']:
        return "Coord STP"

    if x in ['max_cycle', 'min_cycle', 'veh_phs', 'ped_nc_phs']:
        return "STP"

    if x in ['spec_ped_treat', 'preemption', 'ovrlps', 'lead_lag', 'distance_to_ramp']:
        return "Complexity"

    if x in ['tot_num_nearby_assets']:
        return "Connectivity"

    return None


def get_scorer_distribution(prec_data):
    scr_df = convert_to_df_precomp_data(prec_data)
    df_res = pd.DataFrame(data=[], columns=["Asset Id", "scorer_name", "scorer_val", "cluster"])
    for clmn in ["week_plans", "wknd_plans", "week_tods", "wknd_tods", "week_free", 'wknd_free',
                 'max_cycle', 'min_cycle', 'veh_phs', 'ped_nc_phs',
                 'spec_ped_treat', 'preemption', 'ovrlps', 'lead_lag', 'distance_to_ramp',
                 "tot_num_nearby_assets"]:
        df_temp = scr_df[["Asset Id", clmn]]
        df_temp["scorer_name"] = clmn.replace("_", " ")
        df_temp["cluster"] = _get_cluster_from_clmn(clmn)
        df_temp.rename(columns={clmn: 'scorer_val'}, inplace=True)

        df_temp = df_temp[["Asset Id", "scorer_name", "scorer_val", "cluster"]]

        if len(df_res) == 0:
            df_res = df_temp
        else:
            df_res = pd.concat([df_res, df_temp])

        # scr_df[f"sc_{clmn}"] = clmn.replace("_"," ")
    return df_res

if __name__ == '__main__':
    pickle_fnm = get_current_pickle_precom_file()
    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)

    df_scorer_dstrbn = get_scorer_distribution(prec_data)