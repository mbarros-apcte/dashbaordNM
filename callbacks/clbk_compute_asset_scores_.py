import numpy as np
import pandas as pd

from utils.user_inputs import get_predefined_user_inputs

pd.set_option("display.max_columns", 40)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"
pd.options.mode.chained_assignment = None # Ignore Warnings

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from utils.utils import fetch_precomp_data



def _assign_coord_based_scores(sig_df, prec_data, user_inputs):

	#input weights
	input_cmpnts = ['week_plans', "wknd_plans", 'week_tods', 'wknd_tods', 'week_free', "wknd_free"]
	coord_weights = [float(user_inputs[x]) for x in input_cmpnts]

	# precomputed factors
	coord_stp_fctr = prec_data["coord_stp_dict"]

	res = []
	for asset in list(sig_df["Asset Id"]):

		if asset in coord_stp_fctr.keys():
			comp_attrib = [float(coord_stp_fctr[asset][x]) for x in input_cmpnts]
			t_sum = round(np.multiply(coord_weights, comp_attrib).sum(),2)
			res.append(t_sum)

		else:
			res.append(0)
	return res


def _assign_stp_based_scores(sig_df, prec_data, user_inputs,corr_fcr_non_veh_phs=-10):

	# #input weights
	input_cmpnts_stp = ['max_cycle',"min_cycle"]
	coord_weights_stp = [float(user_inputs[x]) for x in input_cmpnts_stp]

	input_cmpnts_dyn = ['tot_veh_phs', "nc_ped_phs"]
	coord_weights_dyn = [float(user_inputs[x]) for x in input_cmpnts_dyn]

	# factors
	coord_stp_fctr = prec_data["coord_stp_dict"]
	kits_din_fctrs = prec_data["kits_din_featrs"]

	res = []

	cmn_keys = set(coord_stp_fctr.keys()).intersection(kits_din_fctrs.keys())
	for asset in list(sig_df["Asset Id"]):

		if asset in cmn_keys:
			coord_attrib = [float(coord_stp_fctr[asset][x]) for x in input_cmpnts_stp]
			t_sum_cord = round(np.multiply(coord_weights_stp, coord_attrib).sum(), 2)

			kits_dyn_attrib = [float(kits_din_fctrs[asset][x]) for x in ["veh_phs","ped_nc_phs"]]
			t_sum_kdyn = round(np.multiply(coord_weights_dyn, kits_dyn_attrib).sum(), 2)

			t_sum = t_sum_cord + t_sum_kdyn

			if kits_din_fctrs[asset]['any_veh_phs'] == 0:
				t_sum += corr_fcr_non_veh_phs

			res.append(t_sum)

		else:
			res.append(0)
	return res


def _assign_cmplx_based_scores(sig_df, prec_data, user_inputs,corr_ramp_fctr=1):

	# #input weights
	input_cmpnts_dyn = ['c_spec_ped_trtmnt', "c_rr_preempt", "c_ovrlps", "c_lead_lag"]
	coord_weights_dyn = [float(user_inputs[x]) for x in input_cmpnts_dyn]

	input_cmpnts_ramp = ['c_ramp']
	coord_weights_ramp = [float(user_inputs[x]) for x in input_cmpnts_ramp]

	# factors
	kits_din_fctrs = prec_data["kits_din_featrs"]
	ramp_fctr = prec_data["ramp_featrs"]


	res = []

	cmn_keys = set(ramp_fctr.keys()).intersection(kits_din_fctrs.keys())
	for asset in list(sig_df["Asset Id"]):

		if asset in cmn_keys:
			kits_dyn_attrib = [float(kits_din_fctrs[asset][x]) for x in ["spec_ped_treat", "preemption","ovrlps","lead_lag"]]
			t_sum_kdyn = round(np.multiply(coord_weights_dyn, kits_dyn_attrib).sum(), 2)

			ramp_attrib = [float(ramp_fctr[asset][x]) for x in ["any_ramp_within_1km"]]
			t_sum_cord = round(np.multiply(coord_weights_ramp, ramp_attrib).sum(), 2)

			t_sum = t_sum_cord + t_sum_kdyn

			if kits_din_fctrs[asset]['any_veh_phs'] == 0:
				t_sum += corr_ramp_fctr

			res.append(t_sum)

		else:
			res.append(0)
	return res




def _assign_cnctvty_based_scores(sig_df, prec_data, user_inputs):


	# #input weights density
	input_cmpnts_density = ["region_density"]
	density_weights = [float(user_inputs[x]) for x in input_cmpnts_density]

	# scores
	density_fctrs = prec_data["dens_featrs"]

	res = []

	for index, row in sig_df.iterrows():

		asset = row["Asset Id"]

		if asset in density_fctrs.keys():

			# density
			dens_attrib = [float(density_fctrs[asset][x]) for x in ["tot_num_nearby_assets"]]
			t_sum_density = round(np.multiply(density_weights, dens_attrib).sum(), 2)

			# sum isolated
			t_sum_isolated= float(user_inputs['isolated_int'])*(1-density_fctrs[asset]["any_int_within_thrs"])

			# county_roads
			t_sum_county = 0
			if sig_df["State/County"][0]=="State":
				t_sum_county = float(user_inputs['county_road'])

			t_sum = t_sum_density + t_sum_isolated + t_sum_county

			res.append(t_sum)

		else:
			res.append(0)
	return res


def add_all_scores(prec_data, user_inputs, corr_fcr_non_veh_phs=-0.01,corr_ramp_fctr=0.01):
	sig_df = prec_data["sig_info"]

	# COORD BASED SCORES
	sig_df["scr_coord"] = _assign_coord_based_scores(sig_df, prec_data, user_inputs)

	# STP BASED SCORES
	sig_df["scr_stp"] = _assign_stp_based_scores(sig_df, prec_data, user_inputs, corr_fcr_non_veh_phs=corr_fcr_non_veh_phs)

	# complexity BASED SCORES
	sig_df["scr_cmplxt"] = _assign_cmplx_based_scores(sig_df, prec_data, user_inputs, corr_ramp_fctr=corr_ramp_fctr)

	# connectivity BASED SCORES
	sig_df["cnctvty"] = _assign_cnctvty_based_scores(sig_df, prec_data, user_inputs)

	# sum all scores
	sig_df["scr_fin_asset"] = sig_df.apply(lambda x: round((x["scr_coord"] + x["scr_stp"] + x["scr_cmplxt"] + x["cnctvty"]),2), axis=1)

	return sig_df

if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm = get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

	# get the req inputs (dummy)
	user_inputs = get_predefined_user_inputs()
	sig_df = add_all_scores(prec_data, user_inputs)


