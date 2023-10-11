import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import pyautogui as pyautogui  # to screenshot monitor

def run():
    
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    
    picture = [
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step1.png', key='IMAGE1')],
        [sg.Text(size=(40, 1))]
    ]
    
    instructionText = [
        [sg.Text('Following the test plan and verify steps follow:')],
        [sg.Text('Step 1.3 Blue LED light on Right/Primary bollard base box, blinks, turns off at power up.')],
        [sg.Text('Step 1.3 Blue LED light on Left/Secondary bollard base box, blinks, turns off at power up.')],
        [sg.Text('Step 1.5 LED Right/Primary Bollard, Front Red.')],
        [sg.Text('Step 1.6 LED Right/Primary Bollard, Front Green.')],
        [sg.Text('Step 1.5 LED Right/Primary Bollard, Back Red.')],
        [sg.Text('Step 1.6 LED Right/Primary Bollard, Back Green.')],
        [sg.Text('Step 1.5 LED Left/Secondary Bollard Front Red.')],
        [sg.Text('Step 1.6 LED Left/Secondary Bollard Front Green.')],
        [sg.Text('Step 1.5 LED Left/Secondary Bollard Back Red.')],
        [sg.Text('Step 1.6 LED Left/Secondary Bollard Back Green.')],
        [sg.Text('Step 1.7 Right Bollard Speaker “Gong” sound on boot at audible volume level.')],
        [sg.Text('Step 1.8 LEDs on Right/Primary and Left/Secondary bollard go to a solid color.')],
        [sg.Text('Step 1.9 Ethernet Link light LEDs Right/Primary bollard are active (Amber and green).')]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instructionText)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 1 - Power On', layout, size=(1000,700), enable_close_attempted_event=True)
    
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