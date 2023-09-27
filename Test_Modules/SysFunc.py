from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor
import pyperclip

def run():
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    picture = [
    [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step3.png', key='IMAGE1')],
    [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Login using the username and password below')],
        [sg.Text('Username: '), sg.InputText('fsr', size=(20,1), use_readonly_for_disable=True, disabled=True),sg.Button("Copy", key="user")],
        [sg.Text('Passwords: '), sg.InputText('magnet0meter1', size=(20,1), use_readonly_for_disable=True, disabled=True),sg.Button("Copy", key="pass")]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 3', layout, size=(800,320), enable_close_attempted_event=True)
    
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
        
        match event:
            case "user":
                pyperclip.copy("fsr")
            case "pass":
                pyperclip.copy("magnet0meter1")
    
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()