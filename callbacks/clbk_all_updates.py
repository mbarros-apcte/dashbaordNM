import numpy as np
import pandas as pd
pd.set_option("display.max_columns", 40)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"
import plotly

from callbacks.clbk_add_MoOcomparison import add_comparison_of_MoO
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from callbacks.clbk_add_proposed_MoO import add_proposed_moe
from callbacks.clbk_aggregate_scores import add_spat_agg_scores

from plotly_utils.central_maps import update_central_map
from plotly_utils.dash_histograms import get_top_fig, get_dash_fig2
from utils.user_inputs import get_predefined_user_inputs, get_relevant_user_inputs

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from utils.utils import fetch_precomp_data


def clbk_all_updates(prec_data,user_inputs):

	# Assign all scores per asset
	sig_df = add_all_scores(prec_data, user_inputs)

	#Group the scores update scores based on spat. agg
	sig_df = add_spat_agg_scores(sig_df, user_inputs)

	# Assign proposed MOE
	sig_df = add_proposed_moe(sig_df, user_inputs)

	# add comparison columns and clrs
	sig_df = add_comparison_of_MoO(sig_df)


	# get a top figure for Dashboard
	f1_dash = get_top_fig(sig_df)

	# matching with siemens solution
	f2_dash = get_dash_fig2(sig_df)

	# update map figure
	precmpt_fig = prec_data["multi_layer_fig"]
	map_fig = update_central_map(precmpt_fig,sig_df)

	return map_fig, f1_dash, f2_dash, sig_df



if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm=get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm) # precoumputed in prepare_variables() method

	# get the req inputs
	input_weights = get_predefined_user_inputs(spat_agg="section-level")

	# get all figures
	map_fig, fig1, fig2, sig_df = clbk_all_updates(prec_data,input_weights)

	map_fig.show('browser')

	#plotly.offline.plot(map_fig, filename="_outputs\clasified_map_v1.html")




