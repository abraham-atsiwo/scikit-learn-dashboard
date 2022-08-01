
from dash.html import Nav, Div, Label, Button
from sklearn_dashboard import app
from sklearn_dashboard.callback import navbar_callback



def navbar_layout(children: list):
    items = []
    for val in children:
        if isinstance(val, str):
            nav = Div(val, className="navbar-item")
        else:
            nav = val
        items.append(nav)
    return Nav(items, className="navbar", id="navbar")

dark_mode = Div([Label("Yes", className="dark-mode-item", id="dark_mode_yes"), 
                Label("No", className="dark-mode-item", id="dark_mode_no")], 
                className="dark-mode", id="dark_mode")
dark_mode_label = Div([Div("Dark Mode"), dark_mode], className="dark-mode-wrapper")

navbar_items = Div(children = navbar_layout(["sklearn dashboard", dark_mode_label, "sklearn | dash"]), 
                    className="navbar-wrapper", id="navbar_wrapper")


navbar_callback(app)
