# set up

import PySimpleGUI as sg
import os

sg.theme("DarkGrey6")

versionID = ("v1")

layout = [ [sg.Text("ADBtools")],
           [sg.Text('')],
           [sg.Text("Run commands:"), sg.Button("adb devices"), sg.Button("adb reboot"), sg.Button("adb reboot bootloader")],
           [sg.Text('')],
           [sg.Text("Install:"), sg.Text("adb install"), sg.InputText(), sg.Button("Install")],
           [sg.Text("Input file path of .apk file, including the file name")],
           [sg.Text('')],
           [sg.Text("Custom ADB command:"), sg.Text("adb"), sg.InputText(), sg.Button("Send")],
           [sg.Text('')],
           [sg.Text('')],
           [sg.Button("Close ADBtools")],
           [sg.Text('')],
           [sg.Text("ADBtools - Made by ConsciousBone and ChatGPT - " + versionID)] ]

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

    elif event == "adb reboot":
        os.system("adb.exe reboot")

    elif event == "adb reboot bootloader":
        os.system("adb.exe reboot bootloader")

    elif event == "Install":
        print("Attempting install: the GUI could stop responding, do not close it!")
        os.system('adb.exe install "' + values[0] + '"')

    elif event == "Send":
        os.system("adb.exe " + values[1])

    elif event == "Close ADBtools":
        print("ADBtools closed")
        break

    elif event == sg.WIN_CLOSED:
        print("ADBtools closed")
        break

window.close()
