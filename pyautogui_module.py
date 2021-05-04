from tkinter.constants import X
import pyautogui as pg
import datetime

# General Function------------------------------------------------->

# # Want to know the size of your screen
# print(pg.size())

# # Want to know the position of your mouse cursor
# print(pg.position())

# # Want to check that x and y coordinates are present on screen or not
# print(pg.onScreen(1365,767))


# Mouse Movement-------------------------------------------------------->

# # Want to move cursor at specific coordinates instantly or with duration(consider as absolute position)
# pg.moveTo(100,200)
# pg.moveTo(300,100,3)

# # Want to move cursor at specific coordinates instantly(consider as relative position)
# pg.move(100,200)
# pg.move(100,200,3)

# # Want to drag cursor while holding a button(consider as absolute position)
# pg.dragTo(374,174,2,button='left')  # default left
# pg.dragTo(374+100,174,2,button='right')
# pg.dragTo(374,174+100,2,button='middle')


# # Want to drag cursor while holding a button(consider as relative position)
# pg.drag(100,200,3)
# pg.drag(100,700,3,button='right')
# pg.drag(100,700,3,button='middle')
# pg.dragRel(50,60,5)
# pg.dragRel(50,60,5,button='right')
# pg.dragRel(50,60,5,button='middle')

# # Drag cursor then click(consider as absolute position)
# pg.click()
# pg.click(338,55)
# pg.click(165,51,duration=2)

# # Drag cursor then hold button(consider as absolute position)
# pg.mouseDown(button='left')
# pg.mouseDown(338,125,'left')
# pg.mouseUp(338,185,'right')

# # Scroll up and down
# pg.scroll(500)
# pg.scroll(-500)
# pg.hscroll(500)
# pg.vscroll(500)


# Keyboard Control Function-------------------------------------------------------------->

# # Want to write a text
# pg.write("Hello sir")
# pg.write("Hello sir",2)

# # Want to press key
# pg.press("enter")
# pg.press(['enter', 'c', 'enter'])

# # Want to press key at same time
# pg.hotkey("ctrl","c")

# # These are keyboard keys
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']


# Message Box Function------------------------------------------------------------->

# # Alert box
# pg.alert("This is python alert box.",title="python",button="Ok")

# # Confirm Box
# pg.confirm(text="Do you want to save this file.", title="JR" , buttons=['Yes','No'])

# # Prompt Box
# pg.prompt("Enter your name-","JR","name")

# # Password Box
# pg.password("Enter your password - ","JR", 'password' , '*')


# Screenshot Function------------------------------------------------------->

# # Take screenshot
# a = pg.screenshot(datetime.datetime.now().strftime('%Y_%m_%d_%I_%M_%S.png'))