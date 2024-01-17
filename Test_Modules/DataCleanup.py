from datetime import datetime  # to get today date
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import pyautogui as pyautogui  # to screenshot monitor
import pyperclip

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
        [sg.Text('4. Check Ethernet Settings and record down the MAC address')],
        [sg.Text('5. Check Wifi Settings and record down the MAC address')],
        [sg.Text('6. Verify Wi-Fi IP setting are set to DHCP (not Static), or not connected.')],
        [sg.Text('7. Scroll down on the Sysadmin page and click "SHUTDOWN"')],
        [sg.Text('8. Disassemble everything')]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Text(size=(10, 1))],
        [sg.Text("Ethernet MAC Address: "), sg.InputText(size=(20,1), key="EthernetMAC"), sg.Button("Help", key="EthernetHelp")],
        [sg.Text("Wifi MAC Address: "), sg.InputText(size=(20,1), key="WifiMAC"), sg.Button("Help", key="WifiHelp")],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 4 - Data Cleanup', layout, size=(850,900), enable_close_attempted_event=True)
    
    #return variable
    EMAC = ""
    WMAC = ""
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "EthernetHelp":
            sg.popup_ok(image='Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step15-1.png')
        elif event == "WifiHelp":
            sg.popup_ok(image='Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step15-2.png')
            
        elif event == "Fail":
            return False
        elif event == "Pass":
            
            EMAC = values["EthernetMAC"]
            WMAC = values["WifiMAC"]
            window.close()
            break
    
    print (EMAC)
    print (WMAC)
    
    return EMAC, WMAC

if __name__ == "__main__":
    print("Debug Mode")
    run()