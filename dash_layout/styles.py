SIDEBAR_STYLE = {
	'top': 0,
	'left': 0,
	'bottom': 0,
	'max-width': '350px',
	#'width': '19%',
	"height": "100vh",
	'padding': '0 0 0 25px',
	'background-color': '#f8f9fa',
	'overflow': 'scroll'
}

DASHBOARD_STYLE = {
	"align": "left",
	"width": '100%',
	'max-width': '400px',
	"height": "100vh",
	'background-color': '#f8f9fa',
	'overflow': 'scroll',
	'padding': '25px'
}

CONTENT_STYLE = {
    'width': '100%',
	#'height': '100%',
    'margin-right': '3%',
    'padding': '20px 10p'
}

CENTRAL_MAP_STYLE = {
	#'position': 'fixed',
	'top': 0,
	'margin-left': '0%',
	#"align": "left",
	#"width": "100%",
	"height": "100%"
}

TEXT_STYLE = {
	'textAlign': 'center',
	'color': '#191970'
}

CARD_TEXT_STYLE = {
	'textAlign': 'center',
	'color': '#0074D9'
}

INPUT_lab_STYLE = {
    'margin-left': '2%',
    'margin-right': '2%',
    'padding': '20px 10p',
    'width': '72%'
}

INPUT_lab_STYLE_short = {
    'margin-left': '2%',
    'margin-right': '2%',
    'padding': '20px 10p',
    'width': '40%'
}

INPUT_dcc_STYLE = {
    'margin-left': '3%',
    'margin-right': '4%',
    'padding': '20px 10p',
    'width': '50px'
}

INPUT_rb_STYLE = {
    'margin-left': '2%',
    'margin-right': '1%',
    'padding': '20px 10p',
    'width': '100%',
    'textalign': 'justify-all'

}

def get_input_rb_style():
	return INPUT_rb_STYLE

def get_sidebar_style():
	return SIDEBAR_STYLE

def get_content_style():
	return CONTENT_STYLE

def get_text_style():
	return TEXT_STYLE

def get_card_text_style():
	return CARD_TEXT_STYLE

def get_input_lab_style():
	return INPUT_lab_STYLE

def get_input_lab_style_short():
	return INPUT_lab_STYLE_short

def get_input_dcc_style():
	return INPUT_dcc_STYLE

def get_central_map_style():
	return CENTRAL_MAP_STYLE

def get_dashboard_style():
	return DASHBOARD_STYLE