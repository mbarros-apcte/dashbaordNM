from dash_layout.styles import get_input_lab_style, get_input_dcc_style
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc

# STP
def get_stp_control_cmpnnts():
    stp_res = [
    html.Label('Number of weekday plans:', style=get_input_lab_style()),
    dcc.Input(id='week_plans', value=0.67, maxLength=5, style=get_input_dcc_style()),

    html.Label('Number of weekend plans:', style=get_input_lab_style()),
    dcc.Input(id='wknd_plans', value=1.1, maxLength=5, style=get_input_dcc_style()),

    html.Label('Number of TOD points over a weekday:', style=get_input_lab_style()),
    dcc.Input(id='week_tods', value=0.7, maxLength=5, style=get_input_dcc_style()),

    html.Label('Number of TOD points over a weekend:', style=get_input_lab_style()),
    dcc.Input(id='wknd_tods', value=0.9, maxLength=5, style=get_input_dcc_style()),

    html.Label('% of time that is running free (weekday):', style=get_input_lab_style()),
    dcc.Input(id='week_free', value=-0.55, maxLength=5, style=get_input_dcc_style()),

    html.Label('% of time that is running free (weekend):', style=get_input_lab_style()),
    dcc.Input(id='wknd_free', value=-0.42, maxLength=5, style=get_input_dcc_style()),
    html.Br(),html.Br()]

    return stp_res

# TIM
def get_tim_cmpnnts():
    tim_res = [
        html.Label('Max cycle length', style=get_input_lab_style()),
        dcc.Input(id='max_cycle', value=0.042, maxLength=5, style=get_input_dcc_style()),

        html.Label('Min cycle length', style=get_input_lab_style()),
        dcc.Input(id='min_cycle', value=0.07, maxLength=5, style=get_input_dcc_style()),

        html.Label('Number of vehicular phases', style=get_input_lab_style()),
        dcc.Input(id='tot_veh_phs', value=1.25, maxLength=5, style=get_input_dcc_style()),

        #html.Label('Number of non-coord phases with ped recall', style=get_input_lab_style()),
        html.Label('Number of (non-coord) ped phases', style=get_input_lab_style()),
        dcc.Input(id='nc_ped_phs', value=3.5, maxLength=5, style=get_input_dcc_style()),

        #html.Label('Number of skipped phases (for a typical day)', style=get_input_lab_style()),
        #dcc.Input(id='inp_tim4', value=0, maxLength=5, style=get_input_dcc_style()),

        #html.Label('% of Green utilization for non coord. phases', style=get_input_lab_style()),
        #dcc.Input(id='inp_tim5', value=0, maxLength=5, style=get_input_dcc_style()),

        #html.Label('Frequency of Pedestrian calls', style=get_input_lab_style()),
        #dcc.Input(id='inp_tim6', value=0, maxLength=5, style=get_input_dcc_style()),
        html.Br(), html.Br()]

    return tim_res

# complex_intersection
def get_compl_int_cmpnnts():
    cmplx_res = [
        html.Label('Presence of special ped treatment', style=get_input_lab_style()),
        dcc.Input(id='c_spec_ped_trtmnt', value=-10, maxLength=5, style=get_input_dcc_style()),

        html.Label('Presence of RR preemption', style=get_input_lab_style()),
        dcc.Input(id='c_rr_preempt', value=10, maxLength=5, style=get_input_dcc_style()),

        html.Label('Presence of overlaps', style=get_input_lab_style()),
        dcc.Input(id='c_ovrlps', value=10, maxLength=5, style=get_input_dcc_style()),

        html.Label('Presence of lead lag', style=get_input_lab_style()),
        dcc.Input(id='c_lead_lag', value=10, maxLength=5, style=get_input_dcc_style()),

        html.Label('Presence of near by ramps', style=get_input_lab_style()),
        dcc.Input(id='c_ramp', value=10, maxLength=5, style=get_input_dcc_style()),
        #html.Label('Major/complex intesetion & bottlneck', style=get_input_lab_style()),
        #dcc.Input(id='inp_cmplx1', value=0, maxLength=5, style=get_input_dcc_style()),

        #html.Label('Major/complex intesetion & bottlneck', style=get_input_lab_style()),
        #dcc.Input(id='inp_cmplx1', value=0, maxLength=5, style=get_input_dcc_style()),

        #html.Label('Coordinated with complex intersection', style=get_input_lab_style()),
        #dcc.Input(id='inp_cmplx2', value=0, maxLength=5, style=get_input_dcc_style()),
        html.Br(), html.Br()]

    return cmplx_res


# complex_intersection
def get_pres_adap_sol_int_cmpnnts():
    adap_sol_res = [
        html.Label('Isolated operations', style=get_input_lab_style()),
        dcc.Input(id='isolated_int', value=-20, maxLength=5, style=get_input_dcc_style()),

        html.Label('Region density', style=get_input_lab_style()),
        dcc.Input(id='region_density', value=0.01, maxLength=5, style=get_input_dcc_style()),

        html.Label('Presence of existing adaptive system', style=get_input_lab_style()),
        dcc.Input(id='exstng_adas', value=0, maxLength=5, style=get_input_dcc_style()),

        html.Label('Importance of State roads', style=get_input_lab_style()),
        dcc.Input(id='county_road', value=0, maxLength=5, style=get_input_dcc_style()),
        #.Label('Presence of railroad preemption', style=get_input_lab_style()),
        #dcc.Input(id='inp_pres2', value=0, maxLength=5, style=get_input_dcc_style()),
        html.Br()]

    return adap_sol_res

# congestion
def get_cngstn_cmpnnts():
    cngstn_sol_res = [
       # html.Label('% of time when the speed is less then 10 mph', style=get_input_lab_style()),
        #dcc.Input(id='inp_cng1', value=0, maxLength=5, style=get_input_dcc_style()),

        #html.Label('% of time when the speed is above 0.85*FFS', style=get_input_lab_style()),
        #dcc.Input(id='inp_cng2', value=0, maxLength=5, style=get_input_dcc_style()),

        html.Label('Bottleneck', style=get_input_lab_style()),
        dcc.Input(id='bottleneck', value=0, maxLength=5, style=get_input_dcc_style()),

        html.Label('Level of Service', style=get_input_lab_style()),
        dcc.Input(id='los', value=0, maxLength=5, style=get_input_dcc_style()),
        html.Br(), html.Br()]

    return cngstn_sol_res