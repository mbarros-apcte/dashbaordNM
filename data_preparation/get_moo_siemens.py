import os
import pandas as pd
pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None

def get_siemens_data():
    df_res = pd.DataFrame(data=[])
    fldr = os.path.join(os.getcwd(),"_input_data","siemens_gis")
    for ii in range(1,13):
        csv_filnme = os.path.join(fldr,f"TG3 SCOOT Priority Map ({ii}).csv")
        df_temp = pd.read_csv(csv_filnme)
        if len(df_res) == 0:
            df_res = df_temp
        else:
            df_res = pd.concat([df_res, df_temp])

    df_res.drop_duplicates(inplace=True)
    df_res.reset_index(inplace=True, drop="index")
    return df_res

if __name__ == '__main__':
	df_res = get_siemens_data()
