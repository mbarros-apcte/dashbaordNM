import random
import plotly.express as px

clrs = """aliceblue, antiquewhite, aqua, aquamarine, azure, beige, bisque, black, blanchedalmond, blue, blueviolet, brown, burlywood, cadetblue, 
chartreuse, chocolate, coral, cornflowerblue, cornsilk, crimson, cyan, darkblue, darkcyan, darkgoldenrod, darkgray, darkgrey, darkgreen, darkkhaki, darkmagenta, darkolivegreen, darkorange,
darkorchid, darkred, darksalmon, darkseagreen, darkslateblue, darkslategray, darkslategrey, darkturquoise, darkviolet, deeppink, deepskyblue,
dimgray, dimgrey, dodgerblue, firebrick, floralwhite, forestgreen, fuchsia, gainsboro, ghostwhite, gold, goldenrod, gray, grey, green, greenyellow, honeydew, hotpink, indianred, indigo,
ivory, khaki, lavender, lavenderblush, lawngreen, lemonchiffon, lightblue, lightcoral, lightcyan,
            lightgoldenrodyellow, lightgray, lightgrey,
            lightgreen, lightpink, lightsalmon, lightseagreen,
            lightskyblue, lightslategray, lightslategrey,
            lightsteelblue, lightyellow, lime, limegreen,
            linen, magenta, maroon, mediumaquamarine,
            mediumblue, mediumorchid, mediumpurple,
            mediumseagreen, mediumslateblue, mediumspringgreen,
            mediumturquoise, mediumvioletred, midnightblue,
            mintcream, mistyrose, moccasin, navajowhite, navy,
            oldlace, olive, olivedrab, orange, orangered,
            orchid, palegoldenrod, palegreen, paleturquoise,
            palevioletred, papayawhip, peachpuff, peru, pink,
            plum, powderblue, purple, red, rosybrown,
            royalblue, rebeccapurple, saddlebrown, salmon,
            sandybrown, seagreen, seashell, sienna, silver,
            skyblue, slateblue, slategray, slategrey, snow,
            springgreen, steelblue, tan, teal, thistle, tomato,
            turquoise, violet, wheat, white, whitesmoke,
            yellow, yellowgreen"""


def get_determ_colors():
	return ["red", "green", "blue", "turquoise", "darkorange", "lightpink", "rosybrown",
			"aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond",
			"blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue",
			"cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "orchid", "palegoldenrod", "palegreen",
			"paleturquoise",
			"palevioletred", "papayawhip", "peachpuff", "peru", "pink"]


def get_all_clrs(clrs=clrs):
	cl = clrs.replace("\n", "")
	cl = cl.replace(" ", "")
	return cl.split(",")


def get_color_dist_coord(dist_m):  # used for ss and distance between signals
	if dist_m < 0:
		return "silver"
	if dist_m < 300:
		return "lime"
	if dist_m < 700:
		return "turquoise"
	if dist_m < 1000:
		return "darkorange"
	if dist_m >= 1000:
		return "red"


def get_color_ss(ss):  # used for ss and distance between signals
	if ss < 1:
		return "lime"
	if ss < 2:
		return "turquoise"
	if ss < 4:
		return "darkorange"
	if ss < 5:
		return "crimson"
	if ss >= 5:
		return "red"


def get_random_clr():
	all_clr = get_all_clrs(clrs=clrs)
	return random.choice(all_clr)


def get_color_scoot_proposed_MoO():
	return "darkgreen"


def get_color_non_coot_proposed_MoO():
	return "darkorange"


# color pattern for histgrams refered to final agg scores
def get_color_discrete_seq_dash_hist_fig_top():
	return px.colors.qualitative.Pastel2


def get_color_discrete_seq_dash_hist_fig_bottom():
	return px.colors.qualitative.Pastel2

def get_color_proposedMOo():
	res = {
		"SCOOT": "darkgreen",
		"TR": "darkred",
		"FA": "darkorange",
		"SUNRISE":"darkorange",
		"NOSCOOT": "darkorange",
		"ATSPM":"darkred"

	}
	return res

def get_color_MoO_cmprsn():
	res = {
		"both_scoot": "green",
		"Ap_sct_S_nosct": "darkred",
		"Ap_nosct_S_sct": "lightred"
	}
	return res
