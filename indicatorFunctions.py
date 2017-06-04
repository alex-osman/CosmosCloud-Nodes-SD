#!/usr/bin/python

import os

isPi = os.getenv('IS_PI', False) is not False

if isPi:
    import SmartHome
PORT_NUMBER = 8081
style = "off"
colors = [0, 0, 0]


def changeColor(colors_):
    global colors
    colors = colors_
    if isPi:
        result = SmartHome.rgb.changeColor(colors)
    else:
        print("rgb::color ", colors)
        result = colors
    return result


def changeStyle(style_):
    global style
    global colors
    print("style: ", style_)
    style = style_
    if isPi:
        if style == 'off':
            print("Turning off!")
            result = SmartHome.rgb.off()
        elif style == 'on':
            result = SmartHome.rgb.changeColor(colors)
    else:
        print("rgb::style", style)
        result = style
    return result
