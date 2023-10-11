import PySimpleGUI as sg  # GUI window
import pyautogui as pyautogui  # to screenshot monitor

def run():
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    #global Variable
    ControlWalk = 0
    MagnetWalk = 0
    
    picture = [        
        [sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step11.png', key='IMAGE1'),
         sg.Image(filename = 'Z:/05. Manufacturing/60. Uncontrolled/Troubleshoot/Dai/MIS Program/MIS-4251_Func_Test/Resources/Step12.png', key='IMAGE2')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Step 11.5 System alerted on control walk. (expect 1 or lower)')],
        [sg.InputText(size=(20,1), key="ControlWalk")],
        
        [sg.Text('Step 12.3 System alerted on magnet Detection Walk-Test. (expect 9 or higher)')],
        [sg.InputText(size=(20,1), key="MagnetWalk")],
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(instruction)],
        [sg.Button("Continue"), sg.Exit()]
    ]
    
    window = sg.Window('Test 11 - Walking Test', layout, size=(1550,750), enable_close_attempted_event=True)
    
    
    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            return False
        elif event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            return False
        elif event == "Continue":
            ControlWalk = values["ControlWalk"]
            MagnetWalk = values["MagnetWalk"]
            window.close()
            break
    
    return ControlWalk, MagnetWalk

if __name__ == "__main__":
    print("Debug Mode")
    run()