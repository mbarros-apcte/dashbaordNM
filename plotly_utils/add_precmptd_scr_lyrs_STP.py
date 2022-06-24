import plotly.graph_objects as go

from plotly_utils.add_all_signals import add_empty_layer


def add_STP_sublayer(fig, rel_df, l_name="Max Cycle Length", clr_col="max_cycle", visib="legendonly",
                      clrb_title="colorbar"):
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
            "Max cycle length: %{customdata[6]}",
            "Min cycle length: %{customdata[7]}",
            "# of Permitted Veh Phases: %{customdata[8]}",
            "Presence of Veh Phases:%{customdata[9]}",
            "# of Ped. Phases (excluding P2&P6): %{customdata[10]}"
        ]),
    ))
    return fig


def add_stp_based_fctrs_lyr(fig, scr_df):
    rel_df = scr_df[['Asset Id', 'Address', 'Section', 'Mode of operation', 'Latitude', 'Longitude',
                     'max_cycle', 'min_cycle', 'veh_phs', 'any_veh_phs', 'ped_nc_phs']]

    fig = add_empty_layer(fig, l_name="SCORERS - STP Based Factors")
    fig = add_STP_sublayer(fig, rel_df, l_name="  Max Cycle Length", clr_col="max_cycle", visib="legendonly",
                            clrb_title="Cycle lenght [s]")
    fig = add_STP_sublayer(fig, rel_df, l_name="  Min Cycle Length", clr_col="min_cycle", visib="legendonly",
                           clrb_title="Cycle lenght [s]")
    fig = add_STP_sublayer(fig, rel_df, l_name="  # of Permitted Veh. Phases", clr_col="veh_phs", visib="legendonly",
                            clrb_title="# of Phases")
    fig = add_STP_sublayer(fig, rel_df, l_name="  Presence of Veh. Phases", clr_col="any_veh_phs", visib="legendonly",
                           clrb_title="Vehicular Activity")

    fig = add_STP_sublayer(fig, rel_df, l_name="  # of Ped. Phases (excluding P2&P6)", clr_col="ped_nc_phs", visib="legendonly",
                           clrb_title="# of Phases")
    fig = add_empty_layer(fig, l_name=" ")
    return fig



