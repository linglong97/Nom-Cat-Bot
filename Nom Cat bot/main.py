import os
import ImageGrab
import time
import win32api, win32con
import ImageOps
import win32gui
from win32api import keybd_event

global game_over
game_over = 0
right_pos = (1003, 627)
left_pos = (872, 628)


Combs = {
    'A': [
        'SHIFT',
        'a'],
    'B': [
        'SHIFT',
        'b'],
    'C': [
        'SHIFT',
        'c'],
    'D': [
        'SHIFT',
        'd'],
    'E': [
        'SHIFT',
        'e'],
    'F': [
        'SHIFT',
        'f'],
    'G': [
        'SHIFT',
        'g'],
    'H': [
        'SHIFT',
        'h'],
    'I': [
        'SHIFT',
        'i'],
    'J': [
        'SHIFT',
        'j'],
    'K': [
        'SHIFT',
        'k'],
    'L': [
        'SHIFT',
        'l'],
    'M': [
        'SHIFT',
        'm'],
    'N': [
        'SHIFT',
        'n'],
    'O': [
        'SHIFT',
        'o'],
    'P': [
        'SHIFT',
        'p'],
    'R': [
        'SHIFT',
        'r'],
    'S': [
        'SHIFT',
        's'],
    'T': [
        'SHIFT',
        't'],
    'U': [
        'SHIFT',
        'u'],
    'W': [
        'SHIFT',
        'w'],
    'X': [
        'SHIFT',
        'x'],
    'Y': [
        'SHIFT',
        'y'],
    'Z': [
        'SHIFT',
        'z'],
    'V': [
        'SHIFT',
        'v'],
    'Q': [
        'SHIFT',
        'q'],
    '?': [
        'SHIFT',
        '/'],
    '>': [
        'SHIFT',
        '.'],
    '<': [
        'SHIFT',
        ','],
    '"': [
        'SHIFT',
        "'"],
    ':': [
        'SHIFT',
        ';'],
    '|': [
        'SHIFT',
        '\\'],
    '}': [
        'SHIFT',
        ']'],
    '{': [
        'SHIFT',
        '['],
    '+': [
        'SHIFT',
        '='],
    '_': [
        'SHIFT',
        '-'],
    '!': [
        'SHIFT',
        '1'],
    '@': [
        'SHIFT',
        '2'],
    '#': [
        'SHIFT',
        '3'],
    '$': [
        'SHIFT',
        '4'],
    '%': [
        'SHIFT',
        '5'],
    '^': [
        'SHIFT',
        '6'],
    '&': [
        'SHIFT',
        '7'],
    '*': [
        'SHIFT',
        '8'],
    '(': [
        'SHIFT',
        '9'],
    ')': [
        'SHIFT',
        '0'] }
Base = {
    '0': 48,
    '1': 49,
    '2': 50,
    '3': 51,
    '4': 52,
    '5': 53,
    '6': 54,
    '7': 55,
    '8': 56,
    '9': 57,
    'a': 65,
    'b': 66,
    'c': 67,
    'd': 68,
    'e': 69,
    'f': 70,
    'g': 71,
    'h': 72,
    'i': 73,
    'j': 74,
    'k': 75,
    'l': 76,
    'm': 77,
    'n': 78,
    'o': 79,
    'p': 80,
    'q': 81,
    'r': 82,
    's': 83,
    't': 84,
    'u': 85,
    'v': 86,
    'w': 87,
    'x': 88,
    'y': 89,
    'z': 90,
    '.': 190,
    '-': 189,
    ',': 188,
    '=': 187,
    '/': 191,
    ';': 186,
    '[': 219,
    ']': 221,
    '\\': 220,
    "'": 222,
    'ALT': 18,
    'TAB': 9,
    'CAPSLOCK': 20,
    'ENTER': 13,
    'BS': 8,
    'CTRL': 17,
    'ESC': 27,
    ' ': 32,
    'END': 35,
    'DOWN': 40,
    'LEFT': 37,
    'UP': 38,
    'RIGHT': 39,
    'SELECT': 41,
    'PRINTSCR': 44,
    'INS': 45,
    'DEL': 46,
    'LWIN': 91,
    'RWIN': 92,
    'LSHIFT': 160,
    'SHIFT': 161,
    'LCTRL': 162,
    'RCTRL': 163,
    'VOLUP': 175,
    'DOLDOWN': 174,
    'NUMLOCK': 144,
    'SCROLL': 145 }

import ctypes
import time

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
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def get_pos():
    x,y = win32api.GetCursorPos()
    print x, y

def get_rgb():
    temp = screenGrab()
    (x,y) = get_screenshot_pos()
    print x, y
    if 0 <x < 460and 0< y < 754:
        f = temp.getpixel((x,y))
        print f

def get_screenshot_pos():
    x,y = win32api.GetCursorPos()
    x= x-722
    y=y-166
    return ((x,y))
    print ([x,y])
    
def screenGrab():
    b1 = (722, 166, 1179,820)
    im = ImageGrab.grab(b1)
 
    ##im.save(os.getcwd() + '\\Snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def KeyUp(Key):
    keybd_event(Base[Key], 0, 2, 0)

def KeyDown(Key):
    keybd_event(Base[Key], 0, 1, 0)

def get_pixel_colour(i_x, i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def Press(Key):
    rest_time = 0.001
    if Key in Base:
        Key = Base[Key]
        KeyDown(Key)
        time.sleep(rest_time)
        KeyUp(Key)
        return True
    if Key in Combs:
        KeyDown(Base[Combs[Key][0]])
        time.sleep(rest_time)
        KeyDown(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][1]])
        time.sleep(rest_time)
        KeyUp(Base[Combs[Key][0]])
        return True
    return False

def start():
    left_counter = 0
    right_counter = 0
    left_down = False
    right_down = False

    while 1:
    ##    left_color = win32gui.GetPixel(win32gui.getDC((win32gui.GetActiveWindow()), 162 , 463))
    ##    right_color = win32gui.GetPixel(win32gui.getDC((win32gui.GetActiveWindow()), 291 , 463))
        left = get_pixel_colour(882, 630)
        right = get_pixel_colour(1024, 649)
        print 'left is:'+ str(left)
        print 'right is:' +str(right)
        if left[0] >160 and left[1] < 130 and left [2] < 150:
            ReleaseKey(0xCB)
            print 'go up left'
            print left
            time.sleep(2)
            return 0
            left_down = True
        else:
            if left_down == False:
                PressKey(0xCB)
            
        if right[0] > 160 and right[1] < 130 and right[2] < 150:
            ReleaseKey(0xCD)
            print 'go up right'
            print right
            right_down = True
            time.sleep(2)
            return 0
        else:
           if right_down == False:
               PressKey(0xCD)
##            
##        if left[0] >200 and left[1] < 200 and left [2] < 200:
##            while left_counter < 100:
##                KeyUp('LEFT')
##                print 'left up'
4##                left_counter += 1
##        else:
##            if left_down == False:
##                KeyDown('LEFT')
##                left_down = True
##        
##        if right[0] > 200 and right[1] < 200 and right[2] < 200:
##            print 'right ' + str(right)
##            while right_counter < 100:
##                KeyUp('RIGHT')
##                print 'right up'
##                right_counter += 1
##            
##        else:
##            if right_down == False:
##                KeyDown('RIGHT')
##                right_down = True
    ##    print 'left' + str(left[0])
    ##    print 'right' + str(right[0])


