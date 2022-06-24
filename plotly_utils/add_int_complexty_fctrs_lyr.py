
import plotly.graph_objects as go

from plotly_utils.add_all_signals import add_empty_layer


def add_int_cmplxt_sublayer(fig, rel_df, l_name="Presence of Special Ped. Op.", clr_col="spec_ped_treat", visib="legendonly",
                      clrb_title="Spec. Ped. Op"):
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
            "Presence of Special Ped. Op.: %{customdata[6]}",
            "Presence of Preemption: %{customdata[7]}",
            "Number of Overlaps:%{customdata[8]}",
            "Presence of Lagging phs.: %{customdata[9]}",
            "Distance to nearby ramp (km).: %{customdata[10]}",
            "Asset id of nearby ramp: %{customdata[11]}",
            "Any ramps within threshold (1km): %{customdata[12]}"
        ]),
    ))
    return fig


def add_int_complexty_fctrs_lyr(fig, scr_df):
    rel_df = scr_df[['Asset Id', 'Address', 'Section', 'Mode of operation', 'Latitude', 'Longitude',
                     'spec_ped_treat', "preemption",'ovrlps', 'lead_lag',
                     'distance_to_ramp', 'asoc_ramp', 'any_ramp_within_1km']]

    fig = add_empty_layer(fig, l_name="SCORERS - Intersection Complexity")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Presence of Special Ped. Op.", clr_col="spec_ped_treat", visib="legendonly",
                      clrb_title="Spec. Ped. Op")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Presence of RR Preemption", clr_col="preemption",
                                  visib="legendonly", clrb_title="RR Preemption")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Number of Overlaps", clr_col="ovrlps",
                                  visib="legendonly", clrb_title="# of Overlaps")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Presence of Lagging LT phs", clr_col="lead_lag",
                                  visib="legendonly", clrb_title="any Lag LT Phase")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Distance to nearest ramp (km)", clr_col="distance_to_ramp",
                                  visib="legendonly", clrb_title="Distance (km)")
    fig = add_int_cmplxt_sublayer(fig, rel_df, l_name="  Any ramp witin 1km radius", clr_col="any_ramp_within_1km",
                                  visib="legendonly", clrb_title="Any Nearby Ramp?")
    fig = add_empty_layer(fig, l_name=" ")
    return fig