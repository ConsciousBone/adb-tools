# set up

import PySimpleGUI as sg
import os

sg.theme("DarkGrey6")

layout = [ [sg.Text("ADBtools")],
           [sg.Text('')],
           [sg.Text("Run commands:"), sg.Button("adb devices"), ],
           [sg.Text("Custom ADB command:"), sg.Text("adb"), sg.InputText(), sg.Button("Send")],
           [sg.Button("Close ADBtools")] ]

# add explanation

print("This is the output window.")
print("Everything that would normally be printed into a terminal goes here.")
print('')

# create window
window = sg.Window("ADBtools", layout, element_justification='c', margins=(25,25))

# move into adb directory so python doesnt shit itself
os.chdir("adb")

# create loop
while True:
    event, values = window.read()

    if event == "adb devices":
        os.system("adb.exe devices")

    elif event == "close ADBtools":
        print("ADBtools closed")
        break

    elif event == "Send":
        os.system("adb.exe " + values[0])

    elif event == sg.WIN_CLOSED:
        print("ADBtools closed")
        break

window.close()
