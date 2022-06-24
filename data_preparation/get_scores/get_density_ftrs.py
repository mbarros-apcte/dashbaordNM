import time
import pickle
import pandas as pd

from _data_collection.utils.get_filenames import get_current_pickle_density_featrs

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"

from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from utils.get_distance_between_lat_long_points import get_distance


def get_density_ftrs(sig_df, thres_km=1, pickle_fnm=get_current_pickle_density_featrs()):
    res = dict()
    for index, row in sig_df.iterrows():
        point1 = (row["Longitude"], row["Latitude"])
        temp = []
        for j,rj in sig_df.iterrows(): # here you can replace the
            point2 = (rj["Longitude"], rj["Latitude"])

            if 0 < get_distance(point1, point2) < thres_km:
                temp.append(rj["Asset Id"])
        res[row["Asset Id"]] ={
            "nearby_assets":temp,
            "tot_num_nearby_assets":len(temp),
            "any_int_within_thrs": 1 if len(temp) > 0 else 0
        }

    res_var={"density_param":res}
    with open(pickle_fnm, "wb") as fp:  # Pickling
        pickle.dump(res_var, fp)
    pass



if __name__ == '__main__':
    pickle_fnm = get_current_pickle_density_featrs()
    sig_df = get_signal_data_from_API()


    time_st = time.perf_counter()
    get_density_ftrs(sig_df, thres_km=1, pickle_fnm=pickle_fnm)
    print(f'Total computation time is {int(time.perf_counter() - time_st)} seconds.')

    with open(pickle_fnm, "rb") as fp:  # Unpickling
        res_data = pickle.load(fp)

    res = res_data["density_param"]

    # convert to dataframe
    df_res = []
    for k,v in res.items():
        df_res.append([k,v["tot_num_nearby_assets"],v["any_int_within_thrs"]])
    df_res = pd.DataFrame(data=df_res,columns=["asset","num_of_int","any_intersct"])