import plotly.graph_objects as go
import random

from plotly_utils.clrs import get_all_clrs, get_determ_colors


def _get_unique_clr_det(n):
	deter_colors = get_determ_colors()
	return deter_colors[0:n]

def _get_unique_clr_random(n):
	res = []
	while len(res) < n:
		t_clr = random.choice(get_all_clrs())
		if t_clr not in res:
			res.append(t_clr)
	return res


def _get_color_based_on_columns(df, clr_col):
	uniq_val = list(df[clr_col].unique())
	color_list = _get_unique_clr_det(len(uniq_val))
	df["clr_set"] = df[clr_col].apply(lambda x: color_list[uniq_val.index(x)])
	return df

def add_empty_layer(fig,l_name="Empty Layer"):
	fig.add_trace(go.Scattermapbox(
		name=l_name,
		lon=[0],
		lat=[0],
		mode='markers',
		marker=go.scattermapbox.Marker(size=0, opacity=.000001, color = "LightSteelBlue"),
		visible="legendonly")
	)
	return fig

def add_all_signals(fig, df, l_name="All signals", clr_col="Mode of operation", visib="legendonly", given_clr=False):
	if not given_clr:
		df = _get_color_based_on_columns(df, clr_col)
	else:
		df["clr_set"]= df[clr_col]

	fig.add_trace(go.Scattermapbox(
		name=l_name,
		lon=df["Longitude"],
		lat=df["Latitude"],
		mode='markers',
		visible=visib,
		marker=go.scattermapbox.Marker(
			size=10,
			color=df["clr_set"],

			opacity=1
		),
		customdata=df,
		hovertemplate="<br>".join([
			"Asset Id: %{customdata[0]}",
			"Address: %{customdata[1]}",
			"Polygon: %{customdata[2]}",
			"Zone: %{customdata[3]}",
			"Section: %{customdata[4]}",
			"Proposed MoO (Siemens v1): %{customdata[5]}",
			"Proposed MoO (Siemens v2): %{customdata[13]}",
			"Proposed MoO (Apcte): %{customdata[14]}",
			"Construction Status: %{customdata[9]}",
			"Controller Type: %{customdata[6]}",
			"System Control: %{customdata[8]}",
			"Jurisdiction:%{customdata[7]}",
			"Municipality:%{customdata[10]}"
		]),
	))
	return fig

def color_based_on_clr(fig, df, l_name="Assigned Weights", clr_col="coord_score", visib=True, clrb_title="colorbar"):

	fig.add_trace(go.Scattermapbox(
		name=l_name,
		lon=df["Longitude"],
		lat=df["Latitude"],
		mode='markers',
		visible=visib,
		marker=go.scattermapbox.Marker(
			size=10,
			color=df[clr_col],
			colorscale="rainbow",
			opacity=1,
			colorbar=dict(
				title=clrb_title
			)
		),
		customdata=df,
		hovertemplate="<br>".join([
			"Asset Id: %{customdata[0]}",
			"Address: %{customdata[1]}",
			"Polygon: %{customdata[2]}",
			"Zone: %{customdata[3]}",
			"Section: %{customdata[4]}",
			"Proposed MoO: %{customdata[5]}",
			"Construction Status: %{customdata[9]}",
			"Controller Type: %{customdata[6]}",
			"System Control: %{customdata[8]}",
			"Jurisdiction:%{customdata[7]}",
			"Municipality:%{customdata[10]}"
		]),
	))
	return fig

