import os

import eel

import sys
import os




from engine.features import *
from engine.command import *

def start():
    eel.init("www")
    playAssistantSound()
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
