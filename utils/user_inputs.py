def get_predefined_user_inputs(week_plans=0.67, wknd_plans =1.1, week_tods =0.7, wknd_tods =0.9, week_free=-0.55, wknd_free=-0.42,
                               max_cycle=0.042, min_cycle=0.07, tot_veh_phs=1.25, nc_ped_phs=3.5,
                               c_spec_ped_trtmnt=-10, c_rr_preempt=10, c_ovrlps=10, c_lead_lag=10, c_ramp=10,
                               isolated_int=-20, region_density=0.01, exstng_adas=0, county_road=0,
                               spat_agg= "int_level", kml_file="smaller_polygons.kml", ex_num_scoots=1064):

    user_inputs = dict()

    crd_bsd_inputs = {
        "week_plans": week_plans,
        "wknd_plans": wknd_plans,
        "week_tods": week_tods,
        "wknd_tods": wknd_tods,
        "week_free": week_free,
        "wknd_free": wknd_free
        }
    user_inputs.update(crd_bsd_inputs)

    stp_inputs ={
        "max_cycle":max_cycle,
        "min_cycle":min_cycle,
        "tot_veh_phs":tot_veh_phs,
        "nc_ped_phs": nc_ped_phs
    }
    user_inputs.update(stp_inputs)

    cmlplx_inputs= {
        "c_spec_ped_trtmnt": c_spec_ped_trtmnt,
        "c_rr_preempt": c_rr_preempt,
        "c_ovrlps": c_ovrlps,
        "c_lead_lag": c_lead_lag,
        "c_ramp": c_ramp
    }
    user_inputs.update(cmlplx_inputs)


    cntctv = {
        "isolated_int": isolated_int,
        "region_density": region_density,
        "exstng_adas": exstng_adas,
        "county_road": county_road,
    }
    user_inputs.update(cntctv)

    spat_and_scoot = {
        "spat_agg": spat_agg,
        "kml_file": kml_file,
        "ex_num_scoots": ex_num_scoots
    }

    user_inputs.update(spat_and_scoot)

    return user_inputs


def get_relevant_user_inputs(mod_num=2, high_num=3, spat_agg="int_level",kml_file="smaller_polygons.kml"):

    week_plans=str(0.1*mod_num)
    wknd_plans = str(0.1*mod_num)
    week_tods = str(0.1*high_num)
    wknd_tods = str(0.1*high_num)
    week_free= str(-0.1*high_num)
    wknd_free= str(-0.1*mod_num)
    max_cycle=str(0.02*high_num)
    min_cycle=str(0.02*high_num)
    tot_veh_phs=(0.5*high_num)
    nc_ped_phs=(0.5*high_num)
    c_spec_ped_trtmnt=str(-1*high_num)
    c_rr_preempt=str(1*high_num)
    c_ovrlps=str(1*mod_num)
    c_lead_lag=str(1*high_num)
    c_ramp=str(2*high_num)
    isolated_int=str(-10*high_num)
    region_density=str(0.005*high_num)
    exstng_adas=str(0.1*mod_num)
    county_road=str(0.1*high_num)
    spat_agg= spat_agg
    kml_file=kml_file
    ex_num_scoots="1450"

    user_inputs = dict()

    crd_bsd_inputs = {
        "week_plans": week_plans,
        "wknd_plans": wknd_plans,
        "week_tods": week_tods,
        "wknd_tods": wknd_tods,
        "week_free": week_free,
        "wknd_free": wknd_free
        }
    user_inputs.update(crd_bsd_inputs)

    stp_inputs ={
        "max_cycle":max_cycle,
        "min_cycle":min_cycle,
        "tot_veh_phs":tot_veh_phs,
        "nc_ped_phs": nc_ped_phs
    }
    user_inputs.update(stp_inputs)

    cmlplx_inputs= {
        "c_spec_ped_trtmnt": c_spec_ped_trtmnt,
        "c_rr_preempt": c_rr_preempt,
        "c_ovrlps": c_ovrlps,
        "c_lead_lag": c_lead_lag,
        "c_ramp": c_ramp
    }
    user_inputs.update(cmlplx_inputs)


    cntctv = {
        "isolated_int": isolated_int,
        "region_density": region_density,
        "exstng_adas": exstng_adas,
        "county_road": county_road,
    }
    user_inputs.update(cntctv)

    spat_and_scoot = {
        "spat_agg": spat_agg,
        "kml_file": kml_file,
        "ex_num_scoots": ex_num_scoots
    }

    user_inputs.update(spat_and_scoot)

    return user_inputs

if __name__ == '__main__':
    user_inputs = get_predefined_user_inputs(week_plans=-1)

    for k, v in user_inputs.items():
        print(f"user input {k} has value {v},")