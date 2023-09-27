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
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step8.png', key='IMAGE1')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Step 8.3: Verify that at least one "orange border" tamper alert for the Right/Primary Bollard')],
        [sg.Text('Step 8.4: Verify that at lease one "orange border" tamper alert for the Left/Secondary Bollard')],
        [sg.Text('You can also check this right after you log in from step 3')]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 8', layout, size=(900,500), enable_close_attempted_event=True)
    
    
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