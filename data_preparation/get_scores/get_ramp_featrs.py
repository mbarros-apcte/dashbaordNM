import time
import pickle
import pandas as pd

from _data_collection.get_signal_location_file_api import get_signal_data_from_API

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"


from _data_collection.utils.ramps import get_ramp_names, get_some_non_ramp_assets, get_some_ramp_asssets
from _data_collection.utils.get_filenames import get_ramp_csv_fnm
from utils.get_distance_between_lat_long_points import get_distance


def _get_ramp_related_assets(sig_df):
    # getting Ramps from address
    df_ramp_1 = sig_df[sig_df["Address"].str.contains(r"SR|95 NB|95 SB|95 EB|95 WB|Gratigny")]

    # dropping some assets from address
    df_ramp_1 = df_ramp_1[~df_ramp_1["Asset Id"].isin(get_some_non_ramp_assets())]

    # adding assets by ID
    df_ramp_2 = sig_df.loc[sig_df["Asset Id"].isin(get_some_ramp_asssets())]
    df_ramp = df_ramp_1.append(df_ramp_2)

    # Adding ramp indicator column to df_sig
    sig_df["Ramp_Indicator"] = sig_df["Asset Id"].apply(lambda x: 1 if x in list(df_ramp["Asset Id"]) else 0)
    return sig_df

def get_ramp_ftrs(sig_df):

    sig_df_ramp = _get_ramp_related_assets(sig_df)
    ramps = sig_df_ramp[sig_df_ramp["Ramp_Indicator"]==1]

    res = dict()
    for index, row in sig_df_ramp.iterrows():
        if row["Asset Id"] in ramps["Asset Id"]: # check if asset is ramp
            asset_sol_dist =0
            assoc_ramp = row["Asset Id"]

        else: # if it is not then find the closest ramp
            point1 = (row["Longitude"], row["Latitude"])

            temp_dst, rmp = [],[]
            for j,rj in ramps.iterrows(): # iterate over all aramps
                point2 = (rj["Longitude"], rj["Latitude"])
                temp_dst.append(round(get_distance(point1, point2),3))
                rmp.append(rj["Asset Id"])

            asset_sol_dist = min(temp_dst)
            assoc_ramp = rmp[temp_dst.index(asset_sol_dist)]

        res[row["Asset Id"]] ={
            "distance_to_ramp":asset_sol_dist,
            "asoc_ramp":assoc_ramp,
            "any_ramp_within_1km": 1 if asset_sol_dist <1  else 0
        }

    return res



if __name__ == '__main__':
    time_st = time.perf_counter()

    sig_df = get_signal_data_from_API()
    res = get_ramp_ftrs(sig_df)
    print(f'Total computation time is {int(time.perf_counter() - time_st)} seconds.')

