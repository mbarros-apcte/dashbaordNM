from dash import dcc, html
import dash_bootstrap_components as dbc
from dash_layout.styles import get_central_map_style

def get_central_map(prec_data):
    cent_fig = prec_data["multi_layer_fig"]

    # central_map = dcc.Graph(id='main_fig', figure=fig, style={'margin-left':'15%', "align":"left", "width":"58%", "height":"80vh" }) #style=get_content_style())
    central_map = html.Div(
        [
            dcc.Graph(
                id='main_fig',
                figure=cent_fig, # data
                style={
                    "width": "100%",
                    "height": "100%"
                    }
            )
        ],
        style=get_central_map_style()
        )

    return central_map
