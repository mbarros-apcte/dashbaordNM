import os.path
import pickle
import time

import plotly

from _data_collection.get_signal_location_file_api import get_signal_data_from_API
from _data_collection.utils.get_filenames import get_current_pickle_precom_file, get_current_pickle_density_featrs
from data_preparation.add_classific_solutions import add_classific_solutns
from data_preparation.get_polygons_of_sections import get_polygons_of_sections
from data_preparation.get_scorer_distribution import get_scorer_distribution
from data_preparation.precomputes_fig_mltpl_layers import get_all_precomputed_figures
from data_preparation.get_scores.coord_cl_atributes import get_coord_cycle_scorers
from data_preparation.get_scores.get_density_ftrs import get_density_ftrs
from data_preparation.get_scores.get_kits_dynamix_atrib import get_kits_dynam_atrib
from data_preparation.get_scores.get_ramp_featrs import get_ramp_ftrs
from plotly_utils.static_fig.correlation import get_correlation_fig


def prepare_variables(pickle_fnm=get_current_pickle_precom_file()):
    prec_data = dict()

    # get the sig_info
    sig_df = get_signal_data_from_API()
    sig_df = add_classific_solutns(sig_df)
    prec_data["sig_info"] = sig_df

    # get the cl data
    coord_stp_dict = get_coord_cycle_scorers(output_dict=True)
    prec_data["coord_stp_dict"] = coord_stp_dict

    # get_the kits features
    kits_din_featrs = get_kits_dynam_atrib(convert_str_col_to_list=True)
    prec_data["kits_din_featrs"] = kits_din_featrs

    # density features
    with open(get_current_pickle_density_featrs(), "rb") as fp:  # Unpickling
        dens_featrs = pickle.load(fp)
    prec_data["dens_featrs"] = dens_featrs["density_param"]

    # ramp features
    ramp_featrs = get_ramp_ftrs(sig_df)
    prec_data["ramp_featrs"] = ramp_featrs

    # precompute the distribution of the get_coord_cycle_scorers
    scor_don = get_scorer_distribution(prec_data)
    prec_data["scorer_distribution"] = scor_don

    #correl_fig = get_correlation_fig(prec_data)
    #prec_data["corr_fig"] = correl_fig

    # Fixme This should be added to pre-computed values
    # spatial aggregation:
    #poygons_of_sect = get_polygons_of_sections(sig_df)
    #prec_data["poygons_of_sect"] = poygons_of_sect

    # precompute the figures
    fig = get_all_precomputed_figures(sig_df, prec_data)

    prec_data["multi_layer_fig"] = fig

    with open(pickle_fnm, "wb") as fp:  # Pickling
        pickle.dump(prec_data, fp)
    pass


if __name__ == '__main__':
    time_st = time.perf_counter()
    pickle_fnm = get_current_pickle_precom_file()
    prepare_variables(pickle_fnm=pickle_fnm)

    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)
    print(f'Total computation time is {int(time.perf_counter() - time_st)} seconds.')

    fig_a = prec_data["multi_layer_fig"]
    fig_a.show("browser")
    plotly.offline.plot(fig_a, filename="_outputs\\fig_mltpl_feat_v3.html")