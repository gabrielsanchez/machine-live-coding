from patterns import *
from random import *

import clipboard
import re
import time
import pyautogui as robot


def auto_move(direction='down',times=1):
    for i in range(times):
        robot.press(direction)

def auto_goto(line):
    robot.hotkey('ctrl','g')
    robot.typewrite(str(line+1))
    robot.hotkey('enter')

def auto_select(start, end):
    for i in range(end-start):
        robot.hotkey('shift', 'right',interval=0.0001)

def auto_select_line():
    robot.hotkey('shift', 'end')

def auto_focus(position=500):
    robot.moveTo(None, 500)
    robot.click()

def auto_eval():
    robot.hotkey('ctrl', 'alt', ',')
    robot.hotkey('shift', 'return')

def auto_copy():
    robot.hotkey('ctrl', 'a')
    robot.hotkey('ctrl', 'c')

def auto_paste():
    return clipboard.paste()

def auto_search(pattern, text):
    return list(re.finditer(pattern,text))

def auto_first():
    robot.hotkey('ctrl', 'home')

def auto_count(text,start,pattern):
    return text[:start].count(pattern)

def auto_write(text,interval=0.1):
    robot.typewrite(text,interval)

def auto_change_pattern(regex_pattern, markov_chain):
    auto_focus()
    auto_copy()
    #auto_eval()

    code = auto_paste()
    expr = auto_search(regex_pattern, code)
    auto_focus()
    auto_first()

    pattern = expr[randint(0,len(expr)-1)]
    new_pattern = markov_chain[pattern.group(3)][randint(0,1)]
    print('changing ' + pattern.group(3) + 'to   =>  ' + new_pattern)

    times = auto_count(code, pattern.start(3), '\n')
    #auto_move('down', times)
    auto_goto(times)
    auto_select_line()
    auto_write(new_pattern)
    auto_move('down',5)
    auto_eval()

def sleep(seconds):
    time.sleep(seconds)
