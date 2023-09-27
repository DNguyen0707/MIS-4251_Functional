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
        [sg.Image(filename = 'Resources/Step11.png', key='IMAGE1')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Step 11.5 System alerted on control walk. (expect 0/10)')],
        [sg.InputText(size=(20,1), key="ControlWalk")],
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Continue"), sg.Exit()]
    ]
    
    window = sg.Window('Test 11', layout, size=(800,300), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Continue":
            if (values["ControlWalk"] > 1):
                window.close()
                return False
            else:
                print("Yahallo!")
                break
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()