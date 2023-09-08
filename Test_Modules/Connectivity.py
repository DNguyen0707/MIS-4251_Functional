from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor

def run():
    #Global Var
    IP = ""
    
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    picture = [
    [sg.Image(filename = 'Resources/Step2.png', key='IMAGE1')],
    [sg.Text(size=(10, 1))]
    ]
    
    instructionText = [
        [sg.Text('Enter the IP Address from the Bollard: ')],
        [sg.Text('IP Address: '), sg.InputText(size=(20,1), key="IPAddress")],
        [sg.Text(size=(10, 1))]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instructionText)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 2', layout, size=(1050,350), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Fail":
            return False
        elif event == "Pass":
            IP = values['IPAddress']
            print(IP)
            window.close()
            webbrowser.open(IP)
            break
    
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    run()