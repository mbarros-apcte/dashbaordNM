import pandas as pd
pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.mode.chained_assignment = None
import json
import requests

SIGNAL_LOCATION_URL = 'https://assets20210319091453.azurewebsites.net/api/IntersectionsSummary?code=KKdJKG7zOTOT3tdKGZ3lwwSI51FZBQaqvF2Z54YxQKAO8Kapt7konA=='

def get_signal_data_from_API():
	# Get the fata from the web
	response = requests.get(SIGNAL_LOCATION_URL)

	cnt = response.content
	cnt = json.loads(cnt.decode('utf-8'))
	df_sig = pd.DataFrame(cnt['intersections'])

	df_sig.rename(columns={'asset_Id': 'Asset Id', "address": "Address","zone": "Zone", "polygon":"Polygon",
						   "control_Section": "Section", "intersection_Type": "Mode of operation",
						   "signalControlCabinet": "Signal Control Cabinet", "controllerType": "Controller Type",
						   "stateCounty": "State/County", "coordinateY": "Latitude","coordinateX": "Longitude"}, inplace=True)

	df_res = df_sig[["Asset Id" , "Address", "Polygon" ,"Zone" , "Section" ,  "Mode of operation", "Controller Type",
					 "State/County", "systemControl", "constructionStatus", "municipality", "Latitude", "Longitude"]]

	df_res[['Polygon', 'Zone','Section']] = df_res[['Polygon', 'Zone','Section']].fillna(value=0)
	df_res = df_res.astype({"Asset Id": 'int64',"Polygon": 'int64',"Zone": 'int64',"Section": 'int64'})

	return df_res

if __name__ == '__main__':
	df_sig = get_signal_data_from_API()


