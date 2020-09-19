#_____________________________
#
#    Roblox Anti Afk Script
#           v1.0
#_____________________________
#
#
# How To Use:
#  1. make sure that the file "RobloxAFK.py" is located in the same location as your AFK script.
#  2. add "from RobloxAFK import *" to the top of your AFK script.
#
# Functions:
#   1. PressKey(LETTER)        LETTER = a-z, ENTER, SPACE, SLASH.
#   2. ReleaseKey(LETTER)      LETTER = a-z, ENTER, SPACE, SLASH.














# Don't Edit Any Of This Code!!!

from pynput.mouse import Button, Controller
import ctypes
import time
import random

mouse = Controller()

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))



a = 0x1e
b = 0x30
c = 0x2e
d = 0x20
e = 0x12
f = 0x21
g = 0x22
h = 0x23
i = 0x17
j = 0x24
k = 0x25
l = 0x26
m = 0x32
n = 0x31
o = 0x18
p = 0x19
q = 0x10
r = 0x13
s = 0x1f
t = 0x14
u = 0x16
v = 0x2f
w = 0x11
x = 0x2d
y = 0x15
z = 0x2c
SPACE = 0x39
SLASH = 0x35
ENTER = 0x1c
Space = 0x39
Slash = 0x35
Enter = 0x1c













