import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

from dash_layout.get_controller_compnents_scoring_factors import get_stp_control_cmpnnts, get_tim_cmpnnts, \
	get_compl_int_cmpnnts, get_pres_adap_sol_int_cmpnnts, get_cngstn_cmpnnts

from dash_layout.utils import get_subtitle, get_section_title
from dash_layout.styles import get_input_lab_style, get_input_dcc_style, get_input_rb_style, get_input_lab_style_short
from dash_layout.utils import get_dict_from_list
from utils.utils import get_available_kml_files


def get_cntrl_scorring_factors():
	control_scr_fctr_cmpnnts = []

	# title
	control_scr_fctr_cmpnnts.extend(get_section_title(section_title='Scoring Factors'))

	# STP
	control_scr_fctr_cmpnnts.append(get_subtitle(sbttl='Coord-based Signal Timing Parameters'))
	control_scr_fctr_cmpnnts.extend(get_stp_control_cmpnnts())

	# TIM
	control_scr_fctr_cmpnnts.append(get_subtitle(sbttl='Signal Timing Parameters'))
	control_scr_fctr_cmpnnts.extend(get_tim_cmpnnts())

	# Complexity
	control_scr_fctr_cmpnnts.append(get_subtitle(sbttl='Intersection Complexity'))
	control_scr_fctr_cmpnnts.extend(get_compl_int_cmpnnts())

	# Presence of Advance TSS
	control_scr_fctr_cmpnnts.append(get_subtitle(sbttl='Connectivity')) #"Presence of Advance TSS
	control_scr_fctr_cmpnnts.extend(get_pres_adap_sol_int_cmpnnts())

	# Congestion
	#control_scr_fctr_cmpnnts.append(get_subtitle(sbttl='Existing Congestion Indicators* (ong.work)'))
	#control_scr_fctr_cmpnnts.extend(get_cngstn_cmpnnts())

	control_scr_fctr_cmpnnts.append(html.Hr())

	#controls_scor_fctrs = dbc.FormGroup(control_scr_fctr_cmpnnts)

	return dbc.FormGroup(control_scr_fctr_cmpnnts)

def get_cntrl_scorring_spat_agg():

	control_scr_spat_agg_cmpnnts = []
	#control_scr_spat_agg_cmpnnts.extend(get_section_title(section_title='Aggregation of Assigned Scores')) # subtitle

	control_scr_spat_agg_cmpnnts.append(get_subtitle(sbttl='Level of Spatial Aggregation'))
	control_scr_spat_agg_cmpnnts.extend(
		[html.Br(),
		dbc.RadioItems(
			id='spat_agg',
			options=[{
				'label': 'Node',
				'value': 'int_level'
				},
				{
					'label': 'Subsection',
					'value': 'subsection_level'
				},
				{
					'label': 'Section',
					'value': 'section_level'
				},
				{
					'label': 'Polygon',
					'value': 'pol_level'
				}
			],
			value='int_level',
			inline=True,
			style=get_input_rb_style())
	])

	kml_optns = get_available_kml_files()
	kml_optns = get_dict_from_list(kml_optns)

	control_scr_spat_agg_cmpnnts.extend([
		html.Br(),
		#html.Label('kml polygon file:', style=get_input_lab_style_short()),

		dcc.Dropdown(
			id='kml_dropdown',
			options=kml_optns,
			#value=kml_optns[0]["value"],  # default value
			placeholder="Select kml polygon file",
			multi=False,
			style={
				'textAlign': 'left', 'width': '90%'
			})]
	)

	control_scr_spat_agg_cmpnnts.append(html.Hr())
	#control_scr_spat_agg_cmpnnts.append(html.Hr())
	return dbc.FormGroup(control_scr_spat_agg_cmpnnts)


# clustering based input
def get_clstr_based_input():

	control_scr_spat_agg_cmpnnts = []
	#control_scr_spat_agg_cmpnnts.extend(get_section_title(section_title='Aggregation of Assigned Scores')) # subtitle

	control_scr_spat_agg_cmpnnts.append(get_subtitle(sbttl='SCOOT Installation'))

	control_scr_spat_agg_cmpnnts.extend(
		[ html.Label('Total number of installation', style=get_input_lab_style()),
        dcc.Input(id='ex_num_scoots', value=1400, maxLength=5, style=get_input_dcc_style()),
        html.Br()])

	control_scr_spat_agg_cmpnnts.extend(
		[dcc.Checklist(
				options =[
					{'label':'  In comparison interpret ATSPM as SCOOT', 'value':'atspm_as_scoot'}],
				value=["atspm_as_scoot"],
				labelStyle={'float': 'left'}),
        html.Br()])

	# control_scr_spat_agg_cmpnnts.extend(
	# 	[html.Label('Total number of groups', style=get_input_lab_style()),
	# 	 dcc.Input(id='num_clstr', value=0, maxLength=5, style=get_input_dcc_style()),
	# 	 html.Br()])
	#
	# control_scr_spat_agg_cmpnnts.extend(
	# 	[html.Label('Number of top groups assigned to Scoot', style=get_input_lab_style()),
	# 	 dcc.Input(id='scoot_clstr', value=0, maxLength=5, style=get_input_dcc_style()),
	# 	 html.Br()])

	#control_scr_spat_agg_cmpnnts.append(html.Hr())
	return dbc.FormGroup(control_scr_spat_agg_cmpnnts)