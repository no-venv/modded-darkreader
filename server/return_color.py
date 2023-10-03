"""

    script to return a single hex color

"""

"""
    function is 4 linux pywal
    idk how to for mac and windows

    i mean, you don't need pywal, as long the script returns a hex 
    colour it's all fine
"""

def linux_pywal():

    from json import loads as load_json
    from os import path

    PYWAL_CONFIG_LOCATION = path.expanduser("~")+"/.cache/wal/colors.json"
        
    PYWAL_COLORS = open(PYWAL_CONFIG_LOCATION,"r")
    PYWAL_COLORS_DICT = load_json(PYWAL_COLORS.read())
    PYWAL_COLORS.close()

    color_dict = {

            "BACKGROUND_COLOR" : PYWAL_COLORS_DICT["special"]["background"],
            "BACKGROUND-ALT_COLOR" : PYWAL_COLORS_DICT["special"]["background"],
            "FOEGROUND_COLOR" : PYWAL_COLORS_DICT["colors"]["color3"],
            "PRIMARY_COLOR" : PYWAL_COLORS_DICT["colors"]["color2"],
            "ALERT_COLOR" : PYWAL_COLORS_DICT["colors"]["color2"],
            "SECONDARY_COLOR" : PYWAL_COLORS_DICT["colors"]["color3"],
            "DISABLED_COLOR" :PYWAL_COLORS_DICT["colors"]["color3"]
    }

    return color_dict["PRIMARY_COLOR"] 

def main():
    # you could edit this to whatever function u want
    return linux_pywal()
    