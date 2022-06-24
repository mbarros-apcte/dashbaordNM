import time

import pandas as pd

from _data_collection.get_df_from_kml import add_polygons_clmn
from _data_collection.get_signal_location_file_api import get_signal_data_from_API


def get_polygons_of_sections(sig_df):
    df_pol = pd.DataFrame(data=sig_df["Section"].unique(),columns=["pol_name"])
    df_pol["assets"] = df_pol["pol_name"].apply(lambda x: list(sig_df[sig_df["Section"]==x]["Asset Id"]))

    return df_pol

if __name__ == '__main__':
    time_st = time.perf_counter()
    sig_df = get_signal_data_from_API()

    df_pol = get_polygons_of_sections(sig_df)

    df_sig = add_polygons_clmn(sig_df, df_pol)
    print(f'Total computation time is {int(time.perf_counter() - time_st)} seconds.')
