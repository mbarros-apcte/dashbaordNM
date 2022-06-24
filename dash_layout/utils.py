from dash import html
from dash_layout.styles import get_text_style


def get_section_title(section_title='Scoring Factors'):
    res = [
        html.H3(section_title, style=get_text_style()),
        html.Br()]
    return res


def get_subtitle(sbttl='Signal Timing Parameters'):
    return html.H5(sbttl, style={'textAlign': 'left'})


def get_dict_from_list(list_items):
    res = []
    for item in list_items:
        res.append({
            'label': item,
            'value': item
        })
    return res
