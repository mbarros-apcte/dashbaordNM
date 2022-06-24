import pandas as pd
pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"

from utils.utils import get_dict_from_df
from _data_collection.get_cl_data_from_csv import get_cycle_data_from_csv

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
WEEKEND = ["Saturday", "Sunday"]


def _get_per_of_week_perf(df_filt, period_of_week=WEEKDAYS):
	temp = df_filt[df_filt["DAY"].isin(period_of_week)]
	week_plans = len(set(temp["PLAN"]))
	week_free = round(sum(temp[temp["PLAN"] >= 62]["plan_dur"]) / len(period_of_week), 2)

	week_tods = temp.groupby(['DAY'], as_index=False).agg(plan_counts=('PLAN', 'count'))["plan_counts"].mean() - 1
	return week_plans, week_tods, week_free


def _get_cl_attributes(df_filt):
	week_plans, week_tods, week_free = _get_per_of_week_perf(df_filt, WEEKDAYS)
	wknd_plans, wknd_tods, wknd_free = _get_per_of_week_perf(df_filt, WEEKEND)

	max_cycle = df_filt["CYCLENGTH"].max()
	min_cycle = df_filt["CYCLENGTH"].min()

	return {"week_plans": week_plans, "wknd_plans": wknd_plans, "week_tods": week_tods,
			 "wknd_tods": wknd_tods,  "week_free": week_free, "wknd_free": wknd_free,
			"max_cycle":max_cycle, "min_cycle":min_cycle}


def get_coord_cycle_scorers(output_dict=True):
	# get cycle matrix
	df_cl = get_cycle_data_from_csv()

	# get plan duration
	df_cl['plan_dur'] = (
				pd.to_datetime(df_cl['TIME_END'].astype(str)) - pd.to_datetime(df_cl['TIME_START'].astype(str)))
	df_cl['plan_dur'] = df_cl['plan_dur'].apply(lambda x: x.seconds / 3600)

	# get aggregated data
	df_coord_stp = df_cl.groupby('ASSETNUM').apply(_get_cl_attributes)
	df_coord_stp = df_coord_stp.reset_index()
	df_coord_stp.columns = ['ASSETNUM', 'coord_cl_feat']

	if output_dict:
		df_coord_stp_dict = get_dict_from_df(df=df_coord_stp, key_col='ASSETNUM', val_col='coord_cl_feat')
		return df_coord_stp_dict
	else:
		for clmn in list(df_coord_stp["coord_cl_feat"][0].keys()):
			df_coord_stp[clmn] = df_coord_stp["coord_cl_feat"].apply(lambda x: x[clmn])

		df_coord_stp.drop(['coord_cl_feat'], axis=1, inplace=True)
		return df_coord_stp


if __name__ == '__main__':
	cl_dict = get_coord_cycle_scorers(output_dict=True)
