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
    
    layout = [
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Req.png', key='IMAGE1')],
        [sg.Image(filename= 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Gen.png', key='IMAGE2')],
        [sg.Image(filename= 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Set.png', key='IMAGE3')],
        [sg.Exit()]
    ]
    
    window = sg.Window('Pre-test', layout, size=(900,950), enable_close_attempted_event=True)
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
        
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            window.close()
        
        
        pre = sg.popup_yes_no("Following the test plan and verify steps follow: "
                              "\n\nPre-2. Left/Secondary Bollard powers up using POE+ supply."
                              "\nPre-3. Right/Primary Bollard powers up using POE+ supply."
                              "\nPre-2. Left/Secondary Bollard powers up using 24V supply."
                              "\nPre-3. Right/Primary Bollard powers up using 24V supply.", title="Pre-Steps")
        
        if pre == "Yes":
            break
            #return True
        else:
            return False
    
    
    return True


if __name__ == "__main__":
    print("Debug Mode")
    run()