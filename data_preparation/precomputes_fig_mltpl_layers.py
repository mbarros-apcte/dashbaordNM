import pickle

import pandas as pd

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from data_preparation.process_prec_scores import convert_to_df_precomp_data
from plotly_utils.add_int_complexty_fctrs_lyr import add_int_complexty_fctrs_lyr
from plotly_utils.add_precmptd_scr_lyrs_STP import add_stp_based_fctrs_lyr
from plotly_utils.add_precmptd_scr_lyrs_connectivity import add_int_connectivit_fctrs_lyr
from plotly_utils.add_precmptd_scr_lyrs_coordSTP import add_coord_based_fctrs_lyr

pd.set_option("display.max_columns", 20)
pd.set_option('display.width', 1000)
pd.options.plotting.backend = "plotly"

import plotly
import plotly.graph_objects as go
import plotly.express as px
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
mapbox_access_token = open(os.path.join(APP_ROOT,".mapbox_token")).read()
px.set_mapbox_access_token(mapbox_access_token)

from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from plotly_utils.add_all_signals import add_all_signals, color_based_on_clr, add_empty_layer
from plotly_utils.utils import update_layout_multiple_layers

from plotly_utils.clrs import get_color_proposedMOo

SCOOT_Clr = get_color_proposedMOo()["SCOOT"]
NOSCOOT_clr = get_color_proposedMOo()["NOSCOOT"]
TR_Clr = get_color_proposedMOo()["TR"]
FActuated_Clr = get_color_proposedMOo()["FA"]
SUNRISE_clr = get_color_proposedMOo()["SUNRISE"]
ATSPM_clr = get_color_proposedMOo()["ATSPM"]

def _get_moo_clr(x):
    if x == "SCOOT":
        return SCOOT_Clr
    elif x == "NO SCOOT":
        return NOSCOOT_clr
    elif x == "Traffic Responsive":
        return TR_Clr
    elif x == 'Fully Actuated':
        return FActuated_Clr
    elif x == 'SUNRISE':
        return SUNRISE_clr
    elif x == 'ATSPM':
        return ATSPM_clr
    return "black"




def add_network_characteristics_lyrs_clstr(fig, sig_df):
    # GET THE DATA
    sig_df["siem_moo_clr"] = sig_df["Mode of operation"].apply(_get_moo_clr)

    fig = add_empty_layer(fig, l_name="NETWORK CHARACTERISTICS")
    fig = color_based_on_clr(fig, sig_df, l_name="  MDC Zones", clr_col="Zone", visib="legendonly", clrb_title="Zone")
    fig = color_based_on_clr(fig, sig_df, l_name="  MDC Section", clr_col="Section", visib="legendonly",
                             clrb_title="Section")
    fig = color_based_on_clr(fig, sig_df, l_name="  Siemens Polygons", clr_col="Polygon", visib="legendonly",
                             clrb_title="Polygon")
    fig = add_all_signals(fig, sig_df, l_name="  Jurisdiction", clr_col="State/County", visib="legendonly")
    fig = add_all_signals(fig, sig_df, l_name="  Municipality", clr_col="municipality", visib="legendonly")
    fig = add_all_signals(fig, sig_df, l_name="  Existing System Control", clr_col="systemControl", visib="legendonly")
    fig = add_all_signals(fig, sig_df, l_name="  Existing Controller Type", clr_col="Controller Type",
                          visib="legendonly")
    fig = add_empty_layer(fig, l_name=" ")

    return fig


def add_scores_lyrs_clstr(fig, prec_data):

    scr_df = convert_to_df_precomp_data(prec_data)
    #fig = add_empty_layer(fig, l_name="SCORERS (before weighting)")
    fig = add_coord_based_fctrs_lyr(fig, scr_df)
    fig = add_stp_based_fctrs_lyr(fig, scr_df)
    fig = add_int_complexty_fctrs_lyr(fig, scr_df)
    fig = add_int_connectivit_fctrs_lyr(fig, scr_df)
    return fig


def add_proposed_moo_lyrs_clstr(fig, sig_df):
    # 3"All signals" layer where color is defined by MoO (Scoot, Actuated)
    sig_df["siem_moo_v1_clr"] = sig_df["Mode of operation"].apply(_get_moo_clr)
    sig_df["siem_moo_v2_clr"] = sig_df["siem_sol_v1"].apply(_get_moo_clr)
    sig_df["apcte_v1_clr"] = sig_df["apcte_sol1"].apply(_get_moo_clr)
    sig_df["apcte_v1_int_lvl_clr"] = sig_df["apcte_sol1_intlevel"].apply(_get_moo_clr)

    fig = add_empty_layer(fig, l_name="PROPOSED MODE OF OPERATIONS (MoO)")
    fig = add_all_signals(fig, sig_df, l_name="  Siemens Sol v1", clr_col="siem_moo_v1_clr", visib="legendonly",
                          given_clr=True)
    fig = add_all_signals(fig, sig_df, l_name="  Siemens Sol v2", clr_col="siem_moo_v2_clr", visib="legendonly",
                          given_clr=True)
    fig = add_all_signals(fig, sig_df, l_name="  APCTE Solution v1", clr_col="apcte_v1_clr",
                          visib="legendonly",
                          given_clr=True)
    fig = add_all_signals(fig, sig_df, l_name="  APCTE Solution v1-int level", clr_col="apcte_v1_int_lvl_clr",
                          visib="legendonly",
                          given_clr=True)
    fig = add_empty_layer(fig, l_name=" ")
    # fig = add_all_signals(fig, sig_df, l_name="  Proposed Siemens MoO", clr_col="Mode of operation", visib="legendonly")

    return fig

def add_comparison_moo_lyrs_clstr(fig, sig_df,section_title=True,comprsn_clmn="apcte_sol1_intlevel",indent=""):
    if section_title:
        fig = add_empty_layer(fig, l_name="COMPARISON OF INITIAL SOLUTIONS")
    else:
        fig = add_empty_layer(fig, l_name="  Initial & evaluated solutions")


    # both scoot
    df_scoot = sig_df[(sig_df["siem_sol_v1"] == "SCOOT") & (sig_df[comprsn_clmn] == "SCOOT")]
    df_scoot["temp_clr"] = SCOOT_Clr
    fig = add_all_signals(fig, df_scoot, l_name=f"{indent}  Scoot & Scoot ({len(df_scoot)} assets)", clr_col="temp_clr",
                          visib="legendonly", given_clr=True)

    # no scoot
    df_nscoot = sig_df[(sig_df["siem_sol_v1"] != "SCOOT") & (sig_df[comprsn_clmn] == "NO SCOOT")]
    df_nscoot["temp_clr"] = NOSCOOT_clr
    fig = add_all_signals(fig, df_nscoot, l_name=f"{indent}  NO Scoot & NO Scoot ({len(df_nscoot)} assets)", clr_col="temp_clr",
                          visib="legendonly", given_clr=True)

    # diff
    ovrlp_assets = list(set(df_scoot["Asset Id"]).union(set(df_nscoot["Asset Id"])))
    df_different = sig_df[~sig_df["Asset Id"].isin(ovrlp_assets)]
    df_different["temp_clr"] = "red"
    fig = add_all_signals(fig, df_different, l_name=f"{indent}  Different Solutions ({len(df_different)} assets)", clr_col="temp_clr",
                          visib="legendonly", given_clr=True)
    return fig


def get_all_precomputed_figures(sig_df, prec_data):
    fig = go.Figure()

    # Network Charactersitics
    fig = add_network_characteristics_lyrs_clstr(fig, sig_df)

    # Scorers
    fig = add_scores_lyrs_clstr(fig, prec_data)

    # Mode of Operations
    fig = add_proposed_moo_lyrs_clstr(fig, sig_df)

    # Comparison
    fig = add_comparison_moo_lyrs_clstr(fig, sig_df,section_title=True,comprsn_clmn="apcte_sol1_intlevel")

    # update the layout
    fig = update_layout_multiple_layers(fig)

    return fig


if __name__ == '__main__':
    pickle_fnm = get_current_pickle_precom_file()
    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)

    sig_df = prec_data["sig_info"]
    fig = get_all_precomputed_figures(sig_df, prec_data)
    fig.show("browser")
    plotly.offline.plot(fig, filename="_outputs\\tmp_fig_mltpl_feat_v2.html")
