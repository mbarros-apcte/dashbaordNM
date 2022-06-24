
import plotly.graph_objects as go

from plotly_utils.add_all_signals import add_empty_layer


def add_connectivity_sublayer(fig, rel_df, l_name="Number of nearby sig. intersections", clr_col="tot_num_nearby_assets", visib="legendonly",
                      clrb_title="# of intersections"):
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
            "Nearby assets.: %{customdata[6]}",
            "Tot # of nearby assets: %{customdata[7]}",
            "Any nearby asset within 1km:%{customdata[8]}",
        ]),
    ))
    return fig


def add_int_connectivit_fctrs_lyr(fig, scr_df):
    rel_df = scr_df[['Asset Id', 'Address', 'Section', 'Mode of operation', 'Latitude', 'Longitude',
                     'nearby_assets', "tot_num_nearby_assets",'any_int_within_thrs']]

    fig = add_empty_layer(fig, l_name="SCORERS - Connectivity")
    fig = add_connectivity_sublayer(fig, rel_df, l_name="  Number of nearby sig. intersections", clr_col="tot_num_nearby_assets", visib="legendonly",
                      clrb_title="# of intersections")
    fig = add_connectivity_sublayer(fig, rel_df, l_name="  Any int. to be coordinated with", clr_col="any_int_within_thrs", visib="legendonly",
                      clrb_title="# of intersections")

    fig = add_empty_layer(fig, l_name=" ")
    return fig