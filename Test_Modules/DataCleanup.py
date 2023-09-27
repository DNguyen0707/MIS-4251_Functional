from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor

def run():
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    picture = [
        [sg.Image(filename = 'Resources/Step14.png', key='IMAGE1')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Go to Operator->Alarm History and click "Clear All Alarms and Reset Tripwire Count. Type "Qualitel" in the popup and press Enter')],
        [sg.Text('Verify Detection Threshold is set to Small (500).')],
        [sg.Text('Verify Ethernet IP setting are set to DHCP and not Static.')],
        [sg.Text('Verify Wi-Fi IP setting are set to DHCP (not Static), or not connected.')],
        [sg.Text('Scroll down on the Sysadmin page and click "SHUTDOWN"')],
        [sg.Text('Disassemble everything')]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 4', layout, size=(800,300), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Fail":
            return False
        elif event == "Pass":
            print('yahallo')
            window.close()
            break
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()