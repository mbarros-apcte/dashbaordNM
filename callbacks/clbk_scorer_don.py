import pickle
import plotly.express as px

from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from data_preparation.get_scorer_distribution import get_scorer_distribution
from utils.user_inputs import get_relevant_user_inputs

def _update_user_inputs_due_to_name_incosistency(updated_user_inputs):
    updated_user_inputs["veh_phs"] =  updated_user_inputs["tot_veh_phs"]
    updated_user_inputs["ped_nc_phs"] = updated_user_inputs["nc_ped_phs"]
    updated_user_inputs["spec_ped_treat"] = updated_user_inputs["c_spec_ped_trtmnt"]
    updated_user_inputs["preemption"] = updated_user_inputs["c_rr_preempt"]
    updated_user_inputs["ovrlps"] = updated_user_inputs["c_ovrlps"]
    updated_user_inputs["lead_lag"] = updated_user_inputs["c_lead_lag"]
    updated_user_inputs["tot_num_nearby_assets"] = updated_user_inputs["region_density"]
    updated_user_inputs['distance_to_ramp'] = 1
    return updated_user_inputs


def  _update_weights(df_filt,updated_user_inputs):
    updated_user_inputs = _update_user_inputs_due_to_name_incosistency(updated_user_inputs)
    df_filt["weigthed_score_val"]=df_filt.apply(lambda x:
        x["scorer_val"] * float(updated_user_inputs[x["scorer_name"].replace(" ","_")]),axis=1)
    return df_filt

def clb_scorer_distribution(x,y,df_scorer_dstrbn,updated_user_inputs):
    df_filt = df_scorer_dstrbn[df_scorer_dstrbn["scorer_name"].isin(x)]

    if y =="scorer_val":
        fig = px.box(df_filt, x="scorer_name", y=y, color="cluster")
        return fig
    elif y == "weigthed_score_val":
        if len(updated_user_inputs) == 0:
            df_filt["weigthed_score_val"] = 0
        else:
            df_filt = _update_weights(df_filt,updated_user_inputs)
        fig = px.box(df_filt, x="scorer_name", y=y, color="cluster")
        return fig


    return {}

if __name__ == "__main__":
    pickle_fnm = get_current_pickle_precom_file()
    with open(pickle_fnm, "rb") as fp:  # Unpickling
        prec_data = pickle.load(fp)

    df_scorer_dstrbn = get_scorer_distribution(prec_data)

