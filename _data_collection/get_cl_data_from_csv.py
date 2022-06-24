import pandas as pd

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)

from _data_collection.utils.get_filenames import get_cl_csv_fnm

CSV_FILENAME = get_cl_csv_fnm()


def get_cycle_data_from_csv(csv_fnm=CSV_FILENAME):
	df_cl = pd.read_csv(csv_fnm)
	df_cl["TIME_START"] = pd.to_datetime(df_cl["TIME_START"], format='%H:%M:%S').dt.time
	df_cl["TIME_END"] = pd.to_datetime(df_cl["TIME_END"], format='%H:%M:%S').dt.time

	return df_cl


if __name__ == '__main__':
	df_cl = get_cycle_data_from_csv()
