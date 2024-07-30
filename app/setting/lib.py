from customtkinter import (CTk as main_app,CTkToplevel as popup_app)
from customtkinter import *
from typing import *
from PIL import Image,ImageTk,ImageDraw,ImageFont,ImageEnhance
import os,platform,subprocess,webbrowser
from tkinter.filedialog import *
from pathlib import Path
import datetime
import math
import os
from io import BytesIO
import gc
from itertools import product
import numpy as np
BASE_DIR=Path(__file__).resolve().parent.parent
def select_app(name_app:Literal['main','popup']):
    if name_app == 'main':
        return main_app()
    elif name_app == 'popup':
        return popup_app()
    else:
        raise ValueError(f'Unknown  name app : {name_app}')
    
def find_chrome_path():
        system=platform.system()
        if system=='Windows':
            possible_paths = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        ]
            for path in possible_paths:
                if os.path.exists(path):
                    return path
        elif system=='Darwin':
            path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
            if os.path.exists(path):
                return path
        elif system=='Linux':
            try:
                path=subprocess.check_output(['which', 'google-chrome']).decode().strip()
                if path:
                    return path
            except subprocess.CalledProcessError:
                pass
            try:
                path = subprocess.check_output(['which', 'chrome']).decode().strip()
                if path:
                    return path
            except subprocess.CalledProcessError:
                pass