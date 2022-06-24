import os
import pandas as pd

from data_preparation.get_moo_apcte import get_apcte_v1_classification

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None

from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from data_preparation.get_moo_siemens import get_siemens_data




def add_classific_solutns(sig_df):
    df_siem = get_siemens_data()
    df_siem.rename(columns={'ASSET ID': 'Asset Id', "Intersection Type": "siem_sol_v1"}, inplace=True)
    sig_df = pd.merge(sig_df, df_siem[['Asset Id', 'siem_sol_v1']], on=['Asset Id'], how='left')

    df_apcte = get_apcte_v1_classification(fnm="clasified_assets_v1.csv")
    df_apcte.rename(columns={'proposed_MoO': 'apcte_sol1'}, inplace=True)
    sig_df = pd.merge(sig_df, df_apcte[['Asset Id', 'apcte_sol1']], on=['Asset Id'], how='left')

    df_apcte = get_apcte_v1_classification(fnm='clasified_assets_v1-int_level.csv')
    df_apcte.rename(columns={'proposed_MoO': 'apcte_sol1_intlevel'}, inplace=True)
    sig_df = pd.merge(sig_df, df_apcte[['Asset Id', 'apcte_sol1_intlevel']], on=['Asset Id'], how='left')

    return sig_df



if __name__ == '__main__':
    sig_df = get_signal_data_from_API()
    sig_df = add_classific_solutns(sig_df)