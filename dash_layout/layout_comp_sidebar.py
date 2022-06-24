from dash import html
import dash_bootstrap_components as dbc

from dash_layout.get_all_controller_compnents import get_cntrl_scorring_factors, get_cntrl_scorring_spat_agg, \
	get_clstr_based_input
from dash_layout.styles import get_sidebar_style, get_input_rb_style


def add_submit_button():
	res = []
	res.extend([

	html.Hr(),
	dbc.Button(
		id='submit_button',
		n_clicks=0,
		children='Submit',
		color='primary',
		block=True
	)
	])
	return dbc.FormGroup(res)

def get_sidebar_layout():
	sidebar = html.Div(
		[
			get_cntrl_scorring_factors(),
			get_cntrl_scorring_spat_agg(),
			get_clstr_based_input(),
			add_submit_button()


		],
		style=get_sidebar_style(),
	)
	return sidebar

