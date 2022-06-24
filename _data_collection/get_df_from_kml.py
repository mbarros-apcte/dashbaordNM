import os
from pykml import parser
import pandas as pd
import time

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from _data_collection.utils.get_filenames import get_loc_kml_file_loc


def _get_lat_longs_from_kml_ccordinates(kml_coordinate):
	res = []
	min_index = kml_coordinate.index("-")
	kml_coordinate = kml_coordinate[min_index::]
	cmpnt = kml_coordinate.split(" ")[:-1]
	# print(cmpnt)
	for coord_pair in cmpnt:
		res.append((float(coord_pair.split(",")[0]), float(coord_pair.split(",")[1])))
	return res


def _updated_pol_name(val):
	try:
		und_ind = val.index("_")
		return val[und_ind + 1::]

	except:
		return val


def get_df_with_polygons_from_kml(kml_fnm="test.kml", update_pol_name=True):
	kml_file_loc = get_loc_kml_file_loc()
	kml_fnm = os.path.join(kml_file_loc, kml_fnm)

	with open(kml_fnm) as fobj:
		folder = parser.parse(fobj).getroot().Document

	df = pd.DataFrame(columns=('pol_name', 'borders'))
	try:
		for pm in folder.Placemark:
			# print(pm.name)
			kml_coordinate = str(pm.Polygon.outerBoundaryIs.LinearRing.coordinates)
			lat_lon_pairs = _get_lat_longs_from_kml_ccordinates(kml_coordinate)
			df = df.append({'pol_name': str(pm.name), 'borders': lat_lon_pairs},
						   ignore_index=True)

	except:
		for pm in folder.Folder.Placemark:
			# print(pm.name)
			kml_coordinate = str(pm.Polygon.outerBoundaryIs.LinearRing.coordinates)
			lat_lon_pairs = _get_lat_longs_from_kml_ccordinates(kml_coordinate)
			df = df.append({'pol_name': str(pm.name), 'borders': lat_lon_pairs},
						   ignore_index=True)

	# remove underscores from pol_name
	if update_pol_name:
		df["pol_name"] = df["pol_name"].apply(_updated_pol_name)
	return df


def get_assets_within_polygon(sig_df, df_pol):
	res = []
	for index, row in df_pol.iterrows():
		polygon = Polygon(row["borders"])
		r = []

		for i, in_row in sig_df.iterrows():
			lon, lat = in_row["Longitude"], in_row["Latitude"],
			point = Point(lon, lat)
			if (polygon.contains(point)):
				r.append(in_row["Asset Id"])
		res.append(r)

	df_pol["assets"] = res
	return df_pol


def add_polygons_clmn(sig_df, df_pol):
	res = []
	for index, row in sig_df.iterrows():
		t_res = []
		asset = row["Asset Id"]

		for ind, r in df_pol.iterrows():
			if asset in r["assets"]:
				t_res.append(r["pol_name"])

		res.append(t_res)

	sig_df["bel_poligons"] = res
	return sig_df


if __name__ == "__main__":
	df_sig = get_signal_data_from_API()


	df_pol = get_df_with_polygons_from_kml("larger_polygons.kml", update_pol_name=True)
	df_pol = get_assets_within_polygon(df_sig, df_pol)

	df_sig = add_polygons_clmn(df_sig, df_pol)
