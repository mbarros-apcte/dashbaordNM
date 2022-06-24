import plotly.graph_objects as go

from data_preparation.precomputes_fig_mltpl_layers import add_comparison_moo_lyrs_clstr
from plotly_utils.add_all_signals import add_all_signals, color_based_on_clr, add_empty_layer


def update_central_map(precmpt_fig, sig_df):
	map_fig = go.Figure(precmpt_fig)
	map_fig = add_empty_layer(map_fig, l_name=" ")
	map_fig = add_empty_layer(map_fig, l_name="EVALUATED SOLUTION")
	map_fig = add_all_signals(map_fig, sig_df, l_name="  Assignd MoO", clr_col="clr_prop_MoO", visib=True,
							  given_clr=True)
	map_fig = color_based_on_clr(map_fig, sig_df, l_name="  Assigned Scores", clr_col="scr_agg",
								 visib="legendonly")
	map_fig = add_comparison_moo_lyrs_clstr(map_fig, sig_df, section_title=False, comprsn_clmn="proposed_MoO",indent="  ")
	return map_fig