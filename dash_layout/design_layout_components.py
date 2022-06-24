# Design app layout components
from dash_layout.layout_comp_central_map import get_central_map
from dash_layout.layout_comp_dashboard import get_dashboard_layout
from dash_layout.layout_comp_sidebar import get_sidebar_layout


def design_layout_components(prec_data):
    # sidebar (left)
    sidebar = get_sidebar_layout()

    # map (central)
    central_map = get_central_map(prec_data)

    # dashboard (right)
    dashboard = get_dashboard_layout(prec_data)


    return sidebar, central_map, dashboard