from datetime import datetime  # to get today date
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import pyautogui as pyautogui  # to screenshot monitor

def run():
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    picture = [
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step14.png', key='IMAGE1')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('1. Go to Operator->Alarm History and click "Clear All Alarms and Reset Tripwire Count.\n     Type "Qualitel" in the popup and press Enter')],
        [sg.Text('2. Verify Detection Threshold is set to Small (500).')],
        [sg.Text('3. Verify Ethernet IP setting are set to DHCP and not Static.')],
        [sg.Text('4. Verify Wi-Fi IP setting are set to DHCP (not Static), or not connected.')],
        [sg.Text('5. Scroll down on the Sysadmin page and click "SHUTDOWN"')],
        [sg.Text('6. Disassemble everything')]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 4 - Data Cleanup', layout, size=(850,800), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Fail":
            return False
        elif event == "Pass":
            window.close()
            break
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()