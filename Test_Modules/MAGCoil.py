from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor
from PIL import Image

#debug mode toggle
debugMode = False

def run(BollardSN = '####-####'):
    #Set font
    sg.set_options(font=('Arial Bold', 14))
    
    #setup path
    if debugMode:
        Path("C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial").mkdir(parents=True, exist_ok=True)
        Path("C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/Download").mkdir(parents=True, exist_ok=True)
    else:
        Path("Z:/05. Manufacturing/20. Test/400 records/Test Records/727/727-4251/Bollard" + BollardSN).mkdir(parents=True, exist_ok=True)
        Path("C:/Users/qtest1/Downloads/Download").mkdir(parents=True, exist_ok=True)
    
    
    picture = [
        [sg.Image(filename= 'Resources/Step9.png', key='IMAGE1')],
        [sg.Text(size=(10, 1))]
    ]
    
    instruction = [
        [sg.Text('Step 9.11: Take the average of each channel. Value under 6?')],
        [sg.Text('Step 9.12: Collect all 4 image')]
    ]
    
    screenshot = [
        [sg.Text('Screenshot:')],
        [sg.Text('- Make sure the web browser is in the primary monitor and Test platform is in the second monitor')],
        [sg.Text('- Let the bollards normalize before screenshot, you can also rescreenshot if needed')],
        [sg.Text('- Take snapshot every 2 minute by clicking the "Snap" button below for each section')],
        [sg.Text('- You can view the image by clicking the "View" button below for each section')],
        [sg.Text(size=(10,1))],
        [sg.Text('Screenshot 1:'), sg.Button("Snap1"), sg.Button("View1")],
        [sg.Text('Screenshot 2:'),  sg.Button("Snap2"), sg.Button("View2")],
        [sg.Text('Screenshot 3:'), sg.Button("Snap3"), sg.Button("View3")],
        [sg.Text('Screenshot RAW:'), sg.Button("SnapRAW"), sg.Button("ViewRAW")],
        [sg.Text(size=(10,1))]
    ]
    
    layout = [
        [sg.Column(picture)],
        [sg.Column(screenshot)],
        [sg.Column(instruction)],
        [sg.Button("Pass"), sg.Button("Fail"), sg.Exit()]
    ]
    
    window = sg.Window('Test 9', layout, size=(1000,680), enable_close_attempted_event=True)
    
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
        
        if debugMode:
            match event:
                case "Snap1":
                    print("snap 1")
                    ima1 = pyautogui.screenshot()
                    ima1.save(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-1.png')
                    continue
                case "Snap2":
                    print("snap 2")
                    ima2 = pyautogui.screenshot()
                    ima2.save(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-2.png')
                    continue
                case "Snap3":
                    print("snap 3")
                    ima3 = pyautogui.screenshot()
                    ima3.save(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-3.png')
                    continue
                case "SnapRAW":
                    print("snap raw")
                    imaRAW = pyautogui.screenshot()
                    imaRAW.save(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-RAW.png')
                    continue
                case "View1":
                    print("view 1")
                    view1 = Image.open(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-1.png')
                    view1.show()
                    continue
                case "View2":
                    print("view 2")
                    view1 = Image.open(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-2.png')
                    view1.show()
                    continue
                case "View3":
                    print("view 3")
                    view1 = Image.open(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-3.png')
                    view1.show()
                    continue
                case "ViewRAW":
                    print("view RAW")
                    view1 = Image.open(r'C:/Users/dain/Documents/Github/MIS-4251_Func_Test/TestTrial/image-RAW.png')
                    view1.show()
                    continue
        else:
            #add directory after
            match event:
                case "Snap1":
                    print("snap 1")
                    ima1 = pyautogui.screenshot()
                    ima1.save(r'')
                    continue
                case "Snap2":
                    print("snap 2")
                    ima2 = pyautogui.screenshot()
                    ima2.save(r'')
                    continue
                case "Snap3":
                    print("snap 3")
                    ima3 = pyautogui.screenshot()
                    ima3.save(r'')
                    continue
                case "SnapRAW":
                    print("snap raw")
                    imaRAW = pyautogui.screenshot()
                    imaRAW.save(r'')
                    continue
                case "View1":
                    print("view 1")
                    view1 = Image.open(r'')
                    view1.show()
                    continue
                case "View2":
                    print("view 2")
                    view1 = Image.open(r'')
                    view1.show()
                    continue
                case "View3":
                    print("view 3")
                    view1 = Image.open(r'')
                    view1.show()
                    continue
                case "ViewRAW":
                    print("view RAW")
                    view1 = Image.open(r'')
                    view1.show()
                    continue

    
    
    
    
    return True

if __name__ == "__main__":
    print("Debug Mode")
    debugMode = True
    run()