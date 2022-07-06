# Design app layout components
from dash_layout.layout_comp_central_map import get_central_map
from dash_layout.layout_comp_dashboard import get_dashboard_layout
from dash_layout.layout_comp_sidebar import get_sidebar_layout
import dash_bootstrap_components as dbc
from dash import html

def design_layout_components(prec_data):
    # sidebar (left)
    sidebar = get_sidebar_layout()

    # map (central)
    central_map = get_central_map(prec_data)

    # dashboard (right)
    dashboard = get_dashboard_layout(prec_data)


    return sidebar, central_map, dashboard

def design_navbar():
    # return dbc.NavbarSimple(
    #     brand="Scoot Dashboard",
    #     brand_href="#",
    #     color="primary",
    #     dark=True,
    #     style={
    #         "margin-bottom": "2px" 
    #     }
    # )
    navbar = dbc.Navbar(
        [
            html.A(
                        # Use row and col to control vertical alignment of logo / brand
                        dbc.Row(
                            [
                                # dbc.Col(html.Img(src=IMGSSRC, height="30px")),
                                dbc.Col(dbc.NavbarBrand("Scoot Dashboard", className="ms-2")),
                            ],
                            align="center",
                            className="g-0",
                        ),
                        # href="https://plotly.com",
                        style={"textDecoration": "none"},
            ),
            dbc.Container(
                [
                    
                    # dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                ]
            )
        ],
        color="dark",
        dark=True,
    )
    return navbar