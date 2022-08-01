from dash import Input, Output, State, callback_context as ctx

def navbar_callback(app):
    @app.callback([Output("navbar_wrapper", "style"), Output("dark_mode_yes", "style"), Output("dark_mode_no", "style")], 
                [Input("dark_mode_yes", "n_clicks"), 
                    Input("dark_mode_no", "n_clicks")])
    def toggle_dark_mode(dark_mode_yes, dark_mode_no):
        styles = {"backgroundColor": "black", "color": "hsl(212, 33%, 89%)"}
        dark_mode_no_style = {"backgroundColor": "black",}
        dark_mode_yes_style = {"backgroundColor": "black", "color": "hsl(212, 33%, 89%)"}
        dark_mode = ctx.triggered_id
        if dark_mode == "dark_mode_no":
            styles = {"backgroundColor": "hsl(212, 33%, 89%)", "color": "black"}
            dark_mode_no_style = {"backgroundColor": "green", "color": "hsl(212, 33%, 89%)"}
            
        if dark_mode == "dark_mode_yes":
            dark_mode_yes_style = {"backgroundColor": "green", "color": "hsl(212, 33%, 89%)"}
        return [styles, dark_mode_yes_style, dark_mode_no_style]

       



