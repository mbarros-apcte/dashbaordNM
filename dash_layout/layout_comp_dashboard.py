from dash import html
from dash import dcc

from plotly_utils._test_figures import get_test_fig_hor_bar, test_figure_conf_matr, test_fig_scatterbox

def get_placeholder_for_precomputed_score_fig():
	res = html.Div([
		html.P("Attributes (x-axis):"),
		dcc.Checklist(
			id='x-axis',
			options=[{'value': x.replace("_"," "), 'label': f' {x.replace("_"," ")}'}
					 for x in ["week_plans",  "wknd_plans",  "week_tods",  "wknd_tods",  "week_free", 'wknd_free',
					 'max_cycle', 'min_cycle', 'veh_phs', 'ped_nc_phs',
					 'spec_ped_treat', 'preemption', 'ovrlps', 'lead_lag', 'distance_to_ramp',
					 "tot_num_nearby_assets"]],
			value=['week plans'],
			style={"margin-left": "15px"}
			#labelStyle={'float': 'left'}
		),
		html.P("Distribution of scorers (y-axis):"),
		dcc.RadioItems(
			id='y-axis',
			options=[{'value': x, 'label': y}
					 for x,y in zip(["scorer_val", "weigthed_score_val"],[" scorer   ", " weighted scorer   "])],
			value='scorer_val',
			labelStyle={'display': 'inline-block'}
		),
		dcc.Graph(id="box-plot"),
	])
	return res

def get_dashboard_layout(prec_data):
	a,b, c,d = 0, 100, "26%", "100%"
	test_fig2 = test_figure_conf_matr()
	#test_fig3 = test_fig_scatterbox()
	dashboard = html.Div([
			get_placeholder_for_precomputed_score_fig(),
			html.Br(), html.Br(),
		dcc.Graph(id='dash_fig1', figure={}, style={'margin-left':f'{a}%', "align":"left", "width":f'{b}%','background-color': '#f8f9fa'}, ),
		html.Br(), html.Br(),
		dcc.Graph(id='dash_fig2', figure={}, style={'margin-left':f'{a}%', "align":"left", "width":f'{b}%','background-color': '#f8f9fa'}),
		html.Br(), html.Br(),
			#dcc.Graph(id='dash_fig3', figure=test_fig3, style={'margin-left':f'{a}%', "align":"left", "width":f'{b}%', 'background-color': '#f8f9fa'}),
			#dcc.Graph(id='dash_fig4', figure=test_fig1, style={'margin-left': f'{a}%', "align": "left", "width": f'{b}%','background-color': '#f8f9fa'}),
		],
		# style={'margin-left':'73%', "align": "left", "width": c, "height": d, 'background-color': '#f8f9fa'} #'position': 'fixed'
		className="col",
		style={
			"padding-left": "0px",
			"height": '100%',
			'overflow-y': 'scroll'
		}
	)
	return dashboard