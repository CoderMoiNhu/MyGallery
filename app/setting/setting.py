
from app.setting.lib import *
from app.setting.style import *

def get_style(name_style: KEY_STYLE_TYPE):
    if name_style in FONT_STYLE:
        return FONT_STYLE[name_style]
    if name_style in COLOR_STYLE:
        return COLOR_STYLE[name_style]
    else:
        return None
    
