import numpy as np
import plotly.express as px
import pandas as pd

from callbacks.clbk_aggregate_scores import add_spat_agg_scores, _get_all_up_to_spat_agg_scores

pd.set_option("display.max_columns", 40)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"
pd.options.mode.chained_assignment = None # Ignore Warnings

from plotly_utils.clrs import get_color_scoot_proposed_MoO, get_color_non_coot_proposed_MoO
from utils.user_inputs import get_predefined_user_inputs

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from utils.utils import fetch_precomp_data


def add_proposed_moe(sig_df, user_inputs):
	clr_scoot = get_color_scoot_proposed_MoO()
	clr_non_scoot = get_color_non_coot_proposed_MoO()

	# Exact number
	if int(user_inputs["ex_num_scoots"]) > 0:

		thrshld = list(sig_df["scr_agg"].sort_values(ascending=False))[int(user_inputs["ex_num_scoots"])]
		sig_df["proposed_MoO"] = sig_df["scr_agg"].apply(lambda x: "SCOOT" if x >= thrshld else "NO SCOOT")
		sig_df["clr_prop_MoO"] = sig_df["proposed_MoO"].apply(lambda x: clr_scoot
										if x =="SCOOT" else clr_non_scoot)

	return sig_df


def _get_all_up_to_est_prop_moe(prec_data, user_inputs):
	sig_df = _get_all_up_to_spat_agg_scores(prec_data, user_inputs)
	sig_df = add_proposed_moe(sig_df, user_inputs)
	return sig_df

if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm = get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

	# get the req inputs (dummy)
	user_inputs = get_predefined_user_inputs(spat_agg= "subsection_level", kml_file="smaller_polygons.kml", ex_num_scoots=1064)

	sig_df = _get_all_up_to_est_prop_moe(prec_data, user_inputs) # assign proposed MoO

