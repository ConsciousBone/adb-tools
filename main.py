# hello_psg.py

import PySimpleGUI as sg
import os

layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("adb devices")]]

# Create the window
window = sg.Window("Demo", layout, margins=(100,100))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "adb devices":
        os.system("cd C:\adb\")
        os.system("adb devices")

    elif event == sg.WIN_CLOSED:
        break

window.close()
