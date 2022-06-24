import os
import time

import pandas as pd

from _data_collection.utils.get_filenames import get_transit_stop_times_fnm, get_transit_trips_fnm, \
	get_transit_stops_fnm

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"


def get_transit_data():
	# stop times
	stop_times_fnm = get_transit_stop_times_fnm()
	stop_times = pd.read_csv(stop_times_fnm)
	stop_times["arr_time"] = stop_times["arrival_time"].apply(
		lambda x: 100 * int(x.split(":")[0]) + int(x.split(":")[1]))
	stop_times = stop_times[["stop_id", "arr_time", "trip_id"]]

	# trips
	trips_fnm = get_transit_trips_fnm()
	trips = pd.read_csv(trips_fnm)
	trips = trips[["route_id", "service_id", "trip_id", "trip_headsign"]]

	# stops
	stops_fnm = get_transit_stops_fnm()
	stops = pd.read_csv(stops_fnm)
	stops = stops[["stop_id", "stop_name", "stop_lat", "stop_lon"]]

	# aggregate data
	stop_rcrds = pd.merge(stop_times, trips, on=['trip_id'], how='left')

	res = []
	for stop_id in list(stop_rcrds["stop_id"].unique()):
		sing_stop = stop_rcrds[stop_rcrds["stop_id"] == stop_id]
		serv_lanes = list(set(sing_stop["service_id"]))
		num_serv_lane = len(serv_lanes)
		routes = list(set(sing_stop["route_id"]))
		num_routes = len(routes)
		headsign = list(set(sing_stop["trip_headsign"]))
		num_headsign = len(headsign)
		daily_services = len(sing_stop)
		am_peak_ser = len(sing_stop[(sing_stop["arr_time"] >= 700) & (sing_stop["arr_time"] <= 900)])
		pm_peak_ser = len(sing_stop[(sing_stop["arr_time"] >= 1600) & (sing_stop["arr_time"] <= 1800)])
		off_peak_ser = len(sing_stop[(sing_stop["arr_time"] >= 1200) & (sing_stop["arr_time"] <= 1400)])
		res.append([stop_id, serv_lanes, num_serv_lane, routes, num_routes, headsign, num_headsign, daily_services,
					am_peak_ser, pm_peak_ser, off_peak_ser])

	transit_df = pd.DataFrame(data=res,
							  columns=["stop_id", "serv_lane", "num_serv_lanes", "routes", "num_routes", "headsign",
									   "num_headsign", "daily_services", "am_peak_ser", "pm_peak_ser", "off_peak_ser"])

	transit_df = pd.merge(transit_df, stops, on=['stop_id'], how='left')
	return transit_df


if __name__ == '__main__':
	start = time.time()
	df_transit = get_transit_data()
	print(f"total computation time is {int(time.time() - start)} seconds")

