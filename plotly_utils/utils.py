import plotly.express as px
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
mapbox_access_token = open(os.path.join(APP_ROOT,".mapbox_token")).read()

px.set_mapbox_access_token(mapbox_access_token)

def update_layout(fig, df_all):
	avg_lat = 0.5 * (df_all["new_lat"].max() + df_all["new_lat"].min())
	avglng = 0.5 * (df_all["new_lon"].max() + df_all["new_lon"].min())

	fig.update_layout(
		# mapbox_style="open-street-map",
		# title='Traffic Data',
		autosize=True,
		hovermode='closest',
		showlegend=True,
		mapbox=dict(
			accesstoken=mapbox_access_token,
			bearing=0,
			center=dict(
				lat=avg_lat,
				lon=avglng
			),
			pitch=0,
			zoom=12,
		),
	)
	return fig


def update_layout_multiple_layers(fig):
	fig.update_layout(
		#height=1000,
		showlegend=True,
		margin=dict(l=10, r=0, b=0, t=0),
		paper_bgcolor="white",
		autosize=True,
		hovermode='closest',
		mapbox_style="open-street-map",
		mapbox=dict(
			# bearing=0,
			accesstoken=mapbox_access_token,
			center=dict(
				lat=25.772,
				lon=-80.150
			),
			pitch=0,
			zoom=10,
		),
		legend=dict(
			# traceorder="reversed",
			x=0.72, y=0.98,
			title_font_family="Times New Roman",
			font=dict(
				family="Courier",
				size=18,
				color="black"
			),
			bgcolor="LightSteelBlue",
			bordercolor="Black",
			borderwidth=1.5
		)
	)
	return fig
