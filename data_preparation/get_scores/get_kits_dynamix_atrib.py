import pandas as pd
pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"

from _data_collection.utils.get_filenames import get_kits_dynamics_fnm

def _get_int_within_str(list_of_int):
    res = []

    for item in list_of_int:
        try:
            res.append(int(item))
        except:
            pass

    return res

def _convert_columns_to_list(df):
    clmn_names = ["perm_phs","veh_phs","ped_phs", "excls_ped_phs","ped_variant"]
    for clmn in clmn_names:
        df[clmn] = df[clmn].apply(_get_int_within_str)
    return df

def get_kits_dynam_atrib(convert_str_col_to_list=True):

    kits_dyn_df = pd.read_csv(get_kits_dynamics_fnm())
    if convert_str_col_to_list:
        kits_dyn_df = _convert_columns_to_list(kits_dyn_df)


    res = dict()
    for index, row in kits_dyn_df.iterrows():
        asset_dct = dict()
        asset_dct["veh_phs"] = len(row["veh_phs"])
        asset_dct["any_veh_phs"] = 1 if len(row["veh_phs"]) > 0 else 0
        asset_dct["ped_nc_phs"] = len(set(row["ped_phs"]).difference({2,6}))
        asset_dct["spec_ped_treat"] = 1 if (len(row["excls_ped_phs"]) >0 or len(row["ped_variant"])>0) else 0
        asset_dct["preemption"] = 1 if row["prempt_comment"] == "there is RR local preemption." else 0
        asset_dct["ovrlps"] = row["num_ovrlp"]
        asset_dct["lead_lag"] = 1 if row["lead_lag"]=="Yes" else 0
        res[row["asset"]]=asset_dct


    return res

if __name__ == '__main__':
	res = get_kits_dynam_atrib(convert_str_col_to_list=True)