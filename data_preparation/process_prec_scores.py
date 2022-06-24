import os.path
import pickle
import time

import pandas as pd
pd.set_option("display.max_columns", 40)
pd.set_option('display.width', 2000)
pd.options.plotting.backend = "plotly"


from _data_collection.utils.get_filenames import get_current_pickle_precom_file


def convert_to_df_precomp_data(prec_data):

    scr_df = prec_data["sig_info"]
    for scorer_clstr in ['coord_stp_dict', 'kits_din_featrs', 'dens_featrs', 'ramp_featrs']:
        scor_dct = prec_data[scorer_clstr]
        keys_of_frst_elmnt= list(scor_dct[list(scor_dct.keys())[0]].keys())

        t_df = [list(list(scor_dct.values())[x].values()) for x in range(len(scor_dct))]
        t_df =pd.DataFrame(t_df,columns=keys_of_frst_elmnt)
        t_df["Asset Id"] =scor_dct.keys()

        scr_df = pd.merge(scr_df, t_df, on=['Asset Id'], how='left')
    return scr_df


if __name__ == '__main__':

    pickle_fnm=get_current_pickle_precom_file()
    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)

    scr_df = convert_to_df_precomp_data(prec_data)