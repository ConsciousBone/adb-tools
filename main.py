# set up

import PySimpleGUI as sg
import os

layout = [[sg.Text("ADBtools")], [sg.Button("adb devices")], [sg.Button("close")]]

# add explanation

print("This is the output window.")
print("Everything that would normally be printed into a terminal goes here.")
print('')

# create window
window = sg.Window("ADBtools", layout, margins=(100,100))

# create loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "adb devices":
        os.chdir("adb")
        os.system("adb devices")

    elif event == "close":
        break

    elif event == sg.WIN_CLOSED:
        break

window.close()
