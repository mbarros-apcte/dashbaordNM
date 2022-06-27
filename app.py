from flask import Flask
import dash
import os

from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output, State
import logging

from _data_collection.utils.get_filenames import get_current_pickle_precom_file  
from callbacks.clbk_all_updates import clbk_all_updates
from callbacks.clbk_scorer_don import clb_scorer_distribution
from dash_layout.layout_comp_dashboard import get_dashboard_layout

from dash_layout.design_layout_components import design_layout_components
from utils.utils import fetch_precomp_data
from dash_layout.layout_comp_sidebar import get_sidebar_layout


# logging
log_name = "logfile.log"
logging.basicConfig(filename=log_name, format='%(asctime)s  %(levelname)-8s %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    filemode='w')  # ,
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.info("Script is starting...\n")

server = Flask(__name__)
# initiate app
app = dash.Dash(
    __name__,
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    url_base_pathname = '/dash/'
)

# get the precomputed values
pickle_fnm = get_current_pickle_precom_file()
prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method
df_scorer_dstrbn = prec_data["scorer_distribution"]

# preset the values
updated_user_inputs = dict()

# get app layout components
sidebar, central_map, dashboard = design_layout_components(prec_data)
app.layout = html.Div(children=[sidebar, central_map, dashboard])

# app authentication
# auth = dash_auth.BasicAuth(app,{'apcte_dash': "test_dash", "test2": "test2"})


@app.callback(
    [Output('main_fig', 'figure'), Output('dash_fig1', 'figure'), Output('dash_fig2', 'figure')],
    [Input('submit_button', 'n_clicks')],
    [State('week_plans', 'value'), State('wknd_plans', 'value'), State('week_tods', 'value'),
     State('wknd_tods', 'value'), State('week_free', 'value'), State('wknd_free', 'value'),

     State('max_cycle', 'value'), State('min_cycle', 'value'), State('tot_veh_phs', 'value'),
     State('nc_ped_phs', 'value'),

     State('c_spec_ped_trtmnt', 'value'), State('c_rr_preempt', 'value'), State('c_ovrlps', 'value'),
     State('c_lead_lag', 'value'), State('c_ramp', 'value'),

     State('isolated_int', 'value'), State('region_density', 'value'), State('exstng_adas', 'value'),
     State('county_road', 'value'),
     State('spat_agg', 'value'), State('kml_dropdown', 'value'), State('ex_num_scoots', 'value')])
def update_graph_1(n_clicks,
                   week_plans, wknd_plans, week_tods, wknd_tods, week_free, wknd_free,
                   max_cycle, min_cycle, tot_veh_phs, nc_ped_phs,
                   c_spec_ped_trtmnt, c_rr_preempt, c_ovrlps, c_lead_lag, c_ramp,
                   isolated_int, region_density, exstng_adas, county_road,
                   spat_agg, kml_file, ex_num_scoots):
    if n_clicks > 0:
        key = ["week_plans", "wknd_plans", "week_tods", "wknd_tods", "week_free", "wknd_free",
               "max_cycle", "min_cycle", "tot_veh_phs", "nc_ped_phs",
               "c_spec_ped_trtmnt", "c_rr_preempt", "c_ovrlps", "c_lead_lag", "c_ramp",
               "isolated_int", "region_density", "exstng_adas", "county_road",
               "spat_agg", "kml_file", "ex_num_scoots"]
        val = [week_plans, wknd_plans, week_tods, wknd_tods, week_free, wknd_free,
               max_cycle, min_cycle, tot_veh_phs, nc_ped_phs,
               c_spec_ped_trtmnt, c_rr_preempt, c_ovrlps, c_lead_lag, c_ramp,
               isolated_int, region_density, exstng_adas, county_road,
               spat_agg, kml_file, ex_num_scoots]
        user_inputs = {k: v for k, v in zip(key, val)}
        global updated_user_inputs
        updated_user_inputs = user_inputs

        for k, v in user_inputs.items():
            logger.info(f"user input {k} has value {v},")

        map_fig, dshbr_fig1, dshbr_fig2, sig_df = clbk_all_updates(prec_data, user_inputs)

        return map_fig, dshbr_fig1, dshbr_fig2

    return prec_data["multi_layer_fig"], {}, {}


@app.callback(
    Output("box-plot", "figure"),
    [Input("x-axis", "value"),
     Input("y-axis", "value")])
def generate_chart(x, y):
    logger.info(f"keys of updated dicts are {list(updated_user_inputs.keys())}\n "
                f"vals of updated dicts are {list(updated_user_inputs.values())}")
    fig = clb_scorer_distribution(x, y, df_scorer_dstrbn, updated_user_inputs)
    return fig


# Routes (make sure server is routing.)
@server.route("/dash/")
def dash():
    print("MB :: Dash is running")
    return "This will soon be the dash"

@server.route("/")
def index():
    print("MB :: Index is running")
    return "Index Page from web."

if __name__ == '__main__':
    server.run(host="0.0.0.0")  # Please use "0.0.0.0" to work on Azure. 
