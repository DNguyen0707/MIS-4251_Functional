from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor
import pyperclip

def run(BollardSN = '####-####'):
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    #Set Logging Info
    logName = datetime.now().strftime("%Y.%m.%d") + "_object_location_Walk_" + BollardSN
    systemNumber = BollardSN
    testNumber =datetime.now().strftime("%Y%m%d%H%M")
    location = "2"
    numberOfPasses = "10"
    logNotes = "Qualitel"
    
    picture1 = [
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step13-1.png', key='IMAGE1')],
    ]
    
    instruction1 = [
        [sg.Text('Fill out data logging function using the information provided below and click "Save Settings"')],
    ]
    
    logging1 = [
        [sg.Text('Log Name: ')],
        [sg.InputText(logName, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="logName")],
        
        [sg.Text('System Number: ')],
        [sg.InputText(systemNumber, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="systemNumber")],
        
        [sg.Text('Test Number: ')],
        [sg.InputText(testNumber, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="testNumber")],
        
        [sg.Text('Location: ')],
        [sg.InputText(location, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="location")],
        
        [sg.Text('Number of Passes: ')],
        [sg.InputText(numberOfPasses, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="numberOfPasses")],
        
        [sg.Text('Log Notes:')],
        [sg.InputText(logNotes, size=(20,1), use_readonly_for_disable=True, disabled=True), sg.Button("Copy", key="logNotes")]
    ]
    
    button1 = [
        [sg.Button("Continue"), sg.Exit()],
        ##[sg.Exit()]
    ]
    
    empty = [
        [sg.Text(size=(10, 1))]
    ]
    
    layout1 = [
        [sg.Column(picture1)],
        [sg.Column(instruction1)],
        [sg.Column(logging1), sg.Column(empty), sg.Column(button1)]
    ]
    
    window1 = sg.Window('Test 13', layout1, size=(900,1050), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window1.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Continue":
            window1.close()
            break
            
        match event:
            case "logName":
                pyperclip.copy(logName)
            case "systemNumber":
                pyperclip.copy(systemNumber)
            case "testNumber":
                pyperclip.copy(testNumber)
            case "location":
                pyperclip.copy(location)
            case "numberOfPasses":
                pyperclip.copy(numberOfPasses)
            case "logNotes":
                pyperclip.copy(logNotes)
                
    
    
    #second section
    picture2 = [
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step13-2.png', key='IMAGE2')],
    ]
    
    instruction2 = [
        [sg.Text('Perform Objection Location Walk-test passing through RONIN system (expect 9 or higher).\nEnter the number to the box below')],
        [sg.InputText(size=(20,1), key="ObjectWalk")],
        [sg.Text('Verify the alerts generated a circle drawn on the images on those alerts for each walk.')],
        [sg.Text('Be sure to download all of the nessessary files as shown in the image above.')],
    ]
    
    layout2 = [
        [sg.Column(picture2)],
        [sg.Column(instruction2)],
        [sg.Button("Continue"), sg.Exit()]
    ]
    
    window2 = sg.Window('Test 13', layout2, size=(900,1050), enable_close_attempted_event=True)
    
    while True:
        event, values = window2.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Continue":
            window2.close()
            break
                
    
    return values["ObjectWalk"]

if __name__ == "__main__":
    print("Debug Mode")
    run()