import os
import pandas as pd

from _data_collection.utils.get_filenames import get_cl_csv_fnm

pd.set_option("display.max.columns", 20)
import datetime
import pyodbc
import time
from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from _data_collection.utils.tod_utils import get_days_of_week, get_tod_for_each_day

def get_cl_data_from_kits():

    # get signal data
    df_sig = get_signal_data_from_API()

    # make connection
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=SQLSRV17TSSPRD1;DATABASE=MIAMIDADE; Trusted_Connection=yes')

    # import intersection data
    sql_query = 'SELECT * FROM KITS.INTERSECTION'
    df_int = pd.read_sql_query(sql_query, cnxn)
    df_int = df_int[["INTID", "ASSETNUM"]]

    # coordination plans
    sql_query = 'SELECT * FROM KITS.COORDALLPLANS233DA'
    df_coord_plans = pd.read_sql_query(sql_query, cnxn)

    # TOD schedule
    sql_query = 'SELECT * FROM KITS.TODSCHED233'
    df_TOD = pd.read_sql_query(sql_query, cnxn)

    # pre-process the data
    df_TOD = df_TOD[df_TOD["PLAN"] > 0].reset_index(drop="index")
    # remove those rows where the next plan is the identical as running plan
    rows_to_remove = []
    for ii in range(len(df_TOD) - 1):
        if (df_TOD["PLAN"][ii] == df_TOD["PLAN"][ii + 1]) & (df_TOD["INTID"][ii] == df_TOD["INTID"][ii + 1]) & (
                df_TOD["DOW"][ii] == df_TOD["DOW"][ii + 1]):
            rows_to_remove.append(ii + 1)
    df_TOD = df_TOD.drop(rows_to_remove).reset_index(drop="index")
    # get running plans for each day
    df_TOD["present_days"] = df_TOD["DOW"].apply(get_days_of_week)

    # for each day, start and time periods assign a coresponding plan
    start_script_time = time.time()
    df_tod_all = pd.DataFrame(data=[])
    for int_id in list(df_TOD.INTID.unique()):
        df_tod_int = df_TOD[df_TOD["INTID"] == int_id].reset_index(drop="index")

        df_dow_tod = get_tod_for_each_day(df_tod_int)

        if len(df_tod_all) == 0:
            df_tod_all = df_dow_tod
        else:
            df_tod_all = pd.concat([df_tod_all, df_dow_tod])

    end_script_time = time.time()
    print(f"--- {int(end_script_time - start_script_time)} seconds ---")

    # merge the data
    df_merged = pd.merge(df_int, df_tod_all, on="INTID", how="right")

    # add cycle length
    df_coord_plans.rename(columns={'PLANNUM': 'PLAN'}, inplace=True)
    df_merged = pd.merge(df_merged, df_coord_plans[["INTID", "PLAN", "CYCLENGTH"]], on=["INTID", "PLAN"], how="left")
    df_merged['CYCLENGTH'] = df_merged['CYCLENGTH'].fillna(0)  # assign CL of free operations to 0

    # add signal characteristics
    df_sig = df_sig.rename(columns={'Asset Id': 'ASSETNUM'})
    df_merged = pd.merge(df_merged, df_sig, on=["ASSETNUM"], how="inner")
    return df_merged


if __name__ == '__main__':
    save_to_csv = True

    start = time.time()
    df_cl = get_cl_data_from_kits()
    print(f"total computation time is {int(time.time()-start)} seconds")

    if save_to_csv:
        csv_fnm = get_cl_csv_fnm()
        df_cl.to_csv(csv_fnm,index=False)