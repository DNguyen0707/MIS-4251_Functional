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
    [sg.Image(filename = 'Resources/Step3.png', key='IMAGE1')],
    [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Login using the username and password below')],
        [sg.Text('Username: '), sg.InputText('fsr', size=(20,1), use_readonly_for_disable=True, disabled=True)],
        [sg.Text('Passwords: '), sg.InputText('magnet0meter1', size=(20,1), use_readonly_for_disable=True, disabled=True)]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 3', layout, size=(800,300), enable_close_attempted_event=True)
    
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