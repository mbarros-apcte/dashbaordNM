import pandas as pd

from callbacks.clbk_add_MoOcomparison import add_comparison_of_MoO, _get_all_up_to_moo_comparison
from callbacks.clbk_aggregate_scores import add_spat_agg_scores
from plotly_utils.clrs import get_color_discrete_seq_dash_hist_fig_top, get_color_discrete_seq_dash_hist_fig_bottom
from utils.user_inputs import get_predefined_user_inputs

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"
pd.options.mode.chained_assignment = None  # Ignore Warnings

import plotly.express as px

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from callbacks.clbk_add_proposed_MoO import add_proposed_moe
from utils.utils import fetch_precomp_data


def get_top_fig(sig_df):
	fig1 = px.histogram(sig_df,
						x="scr_agg",
						color="proposed_MoO",
						color_discrete_sequence=get_color_discrete_seq_dash_hist_fig_top(),
						category_orders={"proposed_MoO": ["SCOOT", "NO SCOOT"]}
						)

	fig1.layout.xaxis.title["text"] = 'Total Score'
	fig1.layout.yaxis.title["text"] = 'Number of Assets'
	fig1.layout.legend.title["text"] = 'Type of Control.'

	fig1.update_xaxes(title_font=dict(size=20, family='Courier', color='black'))
	fig1.update_yaxes(title_font=dict(size=20, family='Courier', color='black'))
	fig1.update_layout(legend_font=dict(size=20, family='Courier', color='black'))
	fig1.update_layout(legend = dict(
		orientation="h",
		yanchor="bottom",
		y=1.01,
		xanchor="left",
		x=0.01
	))
	return fig1


def get_dash_fig2(sig_df):
	fig2 = px.histogram(sig_df,
						y="proposed_MoO",
						x="t_all_ones",
						color="proposed_MoO",
						pattern_shape="Siemens sol.",
						color_discrete_sequence = get_color_discrete_seq_dash_hist_fig_bottom(),
						category_orders = {"proposed_MoO": ["SCOOT", "NO SCOOT"]})
						#labels = {'final_score': 'Total Score',
								  #'proposed_MoO': "Proposed sol."})

	fig2.layout.xaxis.title["text"] = 'Total Number of Assigned Assets'
	fig2.layout.yaxis.title["text"] = 'Type of Control'
	fig2.layout.legend.title["text"] = 'Comparison:'# 'Proposed & Siemens sol.'

	fig2.update_xaxes(title_font=dict(size=20, family='Courier', color='black'))
	fig2.update_yaxes(tickangle=-90, title_font=dict(size=20, family='Courier', color='black'))
	fig2.update_layout(legend_font=dict(size=18, family='Courier', color='black'))
	fig2.update_layout(legend=dict(
		orientation="h",
		#itemwidth=80,
		yanchor="bottom",
		y=1.01,
		xanchor="left",
		x=0.01
	))
	return fig2


if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm = get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

	# get the req inputs
	user_inputs = get_predefined_user_inputs(kml_file="smaller_polygons.kml")

	# compute scores per asset; agg. scores; assign proposed MoO; compare_solutions
	sig_df = _get_all_up_to_moo_comparison(prec_data, user_inputs)

	# get figures
	fig1 = get_top_fig(sig_df)
	fig2 = get_dash_fig2(sig_df)
	fig2.show('browser')