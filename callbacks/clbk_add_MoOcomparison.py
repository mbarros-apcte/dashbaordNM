from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from callbacks.clbk_add_proposed_MoO import add_proposed_moe, _get_all_up_to_est_prop_moe
from plotly_utils.clrs import get_color_MoO_cmprsn
from utils.user_inputs import get_predefined_user_inputs
from utils.utils import fetch_precomp_data


def add_comparison_of_MoO(sig_df):
	# sig_df["matching_sltns"] = sig_df.apply(
	# 	lambda x: "Yes" if (x["Mode of operation"] == "SCOOT") == (x["proposed_MoO"] == "SCOOT")
	# 	else "No", axis=1)
	clr_comprs = get_color_MoO_cmprsn()

	sig_df["Siemens sol."] = sig_df.apply(
		lambda x: "SCOOT" if x["siem_sol_v1"] == "SCOOT" else "NO SCOOT", axis=1)
	sig_df["t_all_ones"] = 1
	sig_df["clr_sol_compasn"] = sig_df.apply(
		lambda x: clr_comprs["both_scoot"] if (x["siem_sol_v1"] == "SCOOT") and (x["proposed_MoO"] == "SCOOT")
		else (clr_comprs["Ap_sct_S_nosct"] if x["proposed_MoO"] == "SCOOT" else clr_comprs["Ap_nosct_S_sct"]), axis=1)

	return sig_df

def _get_all_up_to_moo_comparison(prec_data, user_inputs):
	sig_df = _get_all_up_to_est_prop_moe(prec_data, user_inputs)
	sig_df = add_comparison_of_MoO(sig_df)
	return sig_df


if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm = get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

	# get the req inputs (dummy)
	user_inputs = get_predefined_user_inputs(kml_file="smaller_polygons.kml")

	sig_df = _get_all_up_to_moo_comparison(prec_data, user_inputs)  # assign proposed MoO