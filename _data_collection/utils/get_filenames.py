import os

# Cycle Lenght csv file
def get_cl_csv_fnm():
	return os.path.join(os.getcwd(), "_input_data", "cl_data", "kits_cl_data.csv")

# kits-Dynamics data
def get_kits_dynamics_fnm():
	return os.path.join(os.getcwd(), "_input_data", "kits_features", "kits_ver3.csv")

#FIXME:This should be removed (Ramp data)
def get_ramp_csv_fnm():
	return os.path.join(os.getcwd(), "_input_data", "ramps", "df_ramps.csv")

# TRANSIT DATA
# stops
def get_transit_stops_fnm():
	return os.path.join(os.getcwd(), "_input_data", "transit_data", "bus_data", "stops.txt")

# stop times
def get_transit_stop_times_fnm():
	return os.path.join(os.getcwd(), "_input_data", "transit_data", "bus_data", "stop_times.txt")

# trips
def get_transit_trips_fnm():
	return os.path.join(os.getcwd(), "_input_data", "transit_data", "bus_data", "trips.txt")

# KML Filenanmes
# major corridors
def get_major_corridors():
	return os.path.join(os.getcwd(), "_input_data", "kml_files", "major_corridors_v3.kml")

def get_larger_clusters():
	return os.path.join(os.getcwd(), "_input_data", "kml_files", "grouped_signals_v2.kml")

def get_current_pickle_precom_file():
	return os.path.join(os.getcwd(),"_input_data","precomputed_data_v1.pickle")

def get_current_pickle_density_featrs():
	return os.path.join(os.getcwd(),"_input_data","precomputed_density_feat_v1.pickle")


def get_loc_kml_file_loc():
	return os.path.join(os.getcwd(), "_input_data", "kml_files")