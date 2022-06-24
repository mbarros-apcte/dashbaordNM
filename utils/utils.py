import os
import pickle

from _data_collection.utils.get_filenames import get_current_pickle_precom_file, get_loc_kml_file_loc


def get_dict_from_df(df,key_col,val_col):
	res_dict = dict()
	for index, row in df.iterrows():
		res_dict[row[key_col]]= row[val_col]
	return res_dict


def fetch_precomp_data(pickle_fnm=get_current_pickle_precom_file()):
	with open(pickle_fnm, "rb") as fp:  # Unpickling
		res_data = pickle.load(fp)
	return res_data


def get_available_kml_files():
	loc_kml_files = get_loc_kml_file_loc()
	all_kml_files= [f for f in os.listdir(loc_kml_files) if
					  (os.path.isfile(os.path.join(loc_kml_files, f)) & (".kml" in f))]
	return all_kml_files


if __name__ == '__main__':
	test = get_available_kml_files()