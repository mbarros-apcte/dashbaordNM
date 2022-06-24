import plotly.graph_objects as go

from plotly_utils.add_all_signals import add_empty_layer


def add_cord_sublayer(fig, rel_df, l_name="Num. of weekend plans", clr_col="week_plans", visib="legendonly", clrb_title="colorbar"):

	fig.add_trace(go.Scattermapbox(
		name=l_name,
		lon=rel_df["Longitude"],
		lat=rel_df["Latitude"],
		mode='markers',
		visible=visib,
		marker=go.scattermapbox.Marker(
			size=10,
			color=rel_df[clr_col],
			colorscale="rainbow",
			opacity=1,
			colorbar=dict(
				title=clrb_title
			)
		),
		customdata=rel_df,
		hovertemplate="<br>".join([
			"Asset Id: %{customdata[0]}",
			"Address: %{customdata[1]}",
			"Section: %{customdata[2]}",
			"Siemens MoO: %{customdata[3]}",
			"Num. of week plans: %{customdata[6]}",
			"Num. of weekend plans: %{customdata[7]}",
			"# of weekday TOD break points: %{customdata[8]}",
			"# of weekend TOD break points:%{customdata[9]}",
			"Total time of running free on weekday(h):%{customdata[10]}",
			"Total time of running free on weekend(h):%{customdata[11]}"
		]),
	))
	return fig



def add_coord_based_fctrs_lyr(fig, scr_df):
	rel_df = scr_df[['Asset Id', 'Address','Section','Mode of operation','Latitude','Longitude',
	'week_plans','wknd_plans', 'week_tods', 'wknd_tods', 'week_free', 'wknd_free']]

	fig = add_empty_layer(fig, l_name="SCORERS - Coord Based Factors")
	fig = add_cord_sublayer(fig, rel_df, l_name="  Active Weekday Plans", clr_col="week_plans", visib="legendonly", clrb_title="# of Plans")
	fig = add_cord_sublayer(fig, rel_df, l_name="  Active Weekend Plans", clr_col="wknd_plans", visib="legendonly", clrb_title="# of Plans")
	fig = add_cord_sublayer(fig, rel_df, l_name="  TOD points over Weekday", clr_col="week_tods", visib="legendonly",clrb_title="# of TOD points")
	fig = add_cord_sublayer(fig, rel_df, l_name="  TOD points over Weekend", clr_col="wknd_tods", visib="legendonly",clrb_title="# of TOD points")
	fig = add_cord_sublayer(fig, rel_df, l_name="  Free regime over weekday (h)", clr_col="week_free", visib="legendonly",
							clrb_title="Hours of running")
	fig = add_cord_sublayer(fig, rel_df, l_name="  Free regime over weekend (h)", clr_col="wknd_free",visib="legendonly",
							clrb_title="Hours of running")
	fig = add_empty_layer(fig, l_name=" ")
	return fig