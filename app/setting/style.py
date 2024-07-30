from typing import *
# Font for the application
FONT_STYLE = {
    'font_sm': ('Roboto', 11),
    'font_md': ('Roboto', 13),
    'font_lg': ('Roboto', 18),
    'font_xl': ('Roboto', 28),
    'font_sm_bold': ('Roboto', 11, 'bold'),
    'font_md_bold': ('Roboto', 13, 'bold'),
    'font_lg_bold': ('Roboto', 18, 'bold'),
    'font_xl_bold': ('Roboto', 28, 'bold'),
    'font_sm_italic': ('Roboto', 11, 'italic'),
    'font_md_italic': ('Roboto', 13, 'italic'),
    'font_lg_italic': ('Roboto', 18, 'italic'),
    'font_xl_italic': ('Roboto', 28, 'italic'),

                        }   

# Tailwind CSS color palette
COLOR_STYLE = {
    'primary': '#2563EB',
    'secondary': '#10B981',
    'success': '#34D399',
    'danger': '#EF4444',
    'warning': '#F59E0B',
    'info': '#3B82F6',
    'light': '#F9FAFB',
    'dark': '#111827',
    'white': '#FFFFFF',
    'black': '#000000',
    'gray': '#6B7280',
    'gray_light': '#D1D5DB',
    'gray_dark': '#374151',
    'gray_darker': '#1F2937',
    'gray_darkest': '#111827',
    'transparent': 'transparent'
}

KEY_STYLE_TYPE = Literal['font_sm', 'font_md', 'font_lg', 'font_xl', 'font_sm_bold', 'font_md_bold', 'font_lg_bold', 'font_xl_bold', 
'font_sm_italic', 'font_md_italic', 'font_lg_italic', 'font_xl_italic','primary', 'secondary', 'success','danger', 'warning', 'info', 'light', 'dark', 'white', 'black', 'gray', 'gray_light',
 'gray_dark', 'gray_darker', 'gray_darkest','transparent']