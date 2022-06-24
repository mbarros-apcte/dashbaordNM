from _data_collection.get_df_from_kml import get_df_with_polygons_from_kml, get_assets_within_polygon, add_polygons_clmn
from _data_collection.utils.get_filenames import get_current_pickle_precom_file
from callbacks.clbk_subsection_clusters import make_homog_subsections
from callbacks.clbk_compute_asset_scores_ import add_all_scores
from data_preparation.get_polygons_of_sections import get_polygons_of_sections
from utils.user_inputs import get_predefined_user_inputs
from utils.utils import fetch_precomp_data


def _get_max_score(row, df_pol_dct):
	if len(row["bel_poligons"]) == 0:
		return row["scr_fin_asset"]
	else:
		res = []
		for pol in row["bel_poligons"]:
			res.append(df_pol_dct[pol])
		return max(res)


def add_spat_agg_scores(sig_df, user_inputs):
	if user_inputs["spat_agg"] in ["pol_level", "section_level"]:
		if user_inputs["spat_agg"] == "pol_level": # case 1 pol_level
			df_pol = get_df_with_polygons_from_kml(user_inputs["kml_file"], update_pol_name=True)
			df_pol = get_assets_within_polygon(sig_df, df_pol)
			sig_df = add_polygons_clmn(sig_df, df_pol)

		if user_inputs["spat_agg"] == "section_level": # case 3 section level
			df_pol = get_polygons_of_sections(sig_df)
			sig_df = add_polygons_clmn(sig_df, df_pol)

		df_pol["tot_score"] = df_pol["assets"].apply(
			lambda x: sig_df[sig_df["Asset Id"].isin(x)]["scr_fin_asset"].sum())
		df_pol["avg_score"] = df_pol.apply(lambda x: x["tot_score"] / len(x["assets"]), axis=1)

		df_pol_dct = dict()
		for index, row in df_pol.iterrows():
			df_pol_dct[row["pol_name"]] = round(row["avg_score"], 2)

		sig_df["scr_agg"] = sig_df.apply(_get_max_score, df_pol_dct=df_pol_dct, axis=1)

	elif user_inputs["spat_agg"]=="subsection_level": # case subsection level
		sig_df = make_homog_subsections(sig_df)
		sig_df["scr_agg"] = sig_df["clstr_cen"]

	else: # i.e. user input = intersection level (remaining case)
		sig_df["scr_agg"] = sig_df["scr_fin_asset"]

	return sig_df


def _get_all_up_to_spat_agg_scores(prec_data, user_inputs):
	sig_df = add_all_scores(prec_data, user_inputs)
	sig_df = add_spat_agg_scores(sig_df, user_inputs)
	return sig_df


if __name__ == '__main__':
	# fetch the precomputed data
	pickle_fnm = get_current_pickle_precom_file()
	prec_data = fetch_precomp_data(pickle_fnm)  # precoumputed in prepare_variables() method

	# get the req inputs (dummy)
	user_inputs = get_predefined_user_inputs(kml_file="smaller_polygons.kml")

	sig_df = _get_all_up_to_spat_agg_scores(prec_data, user_inputs)
