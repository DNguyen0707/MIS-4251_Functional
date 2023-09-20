#!/usr/bin/env python3

from datetime import datetime  # to get today date
import shutil  # to move files
import openpyxl  # edit file excel
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import webbrowser  # open website
import pyautogui as pyautogui  # to screenshot monitor

#import test module
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
testModule_path = os.path.join(current_dir, 'Test_Modules')
sys.path.append("Test_Modules")


#Set font
sg.set_options(font=('Arial Bold', 14))

image_viewer_column = [
    [sg.Image(key="-IMAGE-")],
    [sg.Text('Pre-Test Result: ', size=(22, 1)), sg.Text(key='T0')],        #Pre-Test
    [sg.Text('Test Step 1 Result: ', size=(22, 1)), sg.Text(key='T1')],     #Power On
    [sg.Text('Test Step 2 Result: ', size=(22, 1)), sg.Text(key='T2')],     #Connectivity
    [sg.Text('Test Step 2 Result: ', size=(22, 1)), sg.Text(key='T3')],     #SysFunc
    [sg.Text('Test Step 4 Result: ', size=(22, 1)), sg.Text(key='T4')],     #MagSen
    [sg.Text('Test Step 5 Result: ', size=(22, 1)), sg.Text(key='T5')],     #Calibrate
    [sg.Text('Test Step 6 Result: ', size=(22, 1)), sg.Text(key='T6')],     #Set Overlay
    [sg.Text('Test Step 7 Result: ', size=(22, 1)), sg.Text(key='T7')],     #Tripwire
    [sg.Text('Test Step 8 Result: ', size=(22, 1)), sg.Text(key='T8')],     #Tamper Switch
    [sg.Text('Test Step 9 Result: ', size=(22, 1)), sg.Text(key='T9')],     #MAG coil
    [sg.Text('Test Step 10 Result: ', size=(22, 1)), sg.Text(key='T10')],   #Walk Setup
    [sg.Text('Test Step 11 Result: ', size=(22, 1)), sg.Text(key='T11')],   #Control Walk
    [sg.Text('Test Step 12 Result: ', size=(22, 1)), sg.Text(key='T12')],   #Magnet Walk
    [sg.Text('Test Step 13 Result: ', size=(22, 1)), sg.Text(key='T13')],   #Object Location
    [sg.Text('Test Step 14 Result: ', size=(22, 1)), sg.Text(key='T14')],   #Data Cleanup
    [sg.Text('Final Test Result: ', size=(22, 1)), sg.Text(key='T15')]      #Post-Test
]

functional_step_column = [
    [sg.Text('Operator Name: ', size=(22, 1)), sg.InputText(size=(20,1), key="OP")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text('System Serial Number: ', size=(22, 1)), sg.Text(key='SS')],
    [sg.Text('Carrier Serial Number: ', size=(22, 1)), sg.Text(key='CS')],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text('Left Bollard SN: ', size=(22, 1)), sg.InputText(size=(20,1), key="LB")],
    [sg.Text('Left Carrier SN: ', size=(22,1)), sg.InputText(size=(20,1), key="LC")],
    [sg.Text('Right Bollard SN: ', size=(22, 1)), sg.InputText(size=(20,1), key="RB")],
    [sg.Text('Right Carrier SN: ', size=(22,1)), sg.InputText(size=(20,1), key="RC")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text('Date: ', size=(22, 1)), sg.Text(key='DT')],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text('Press Start to begin the Test.')],
    [sg.Button("Start"), sg.Exit()]
]

# Full Layout
layout = [
    [sg.Text('727-4251 MIS BOLLARDS FINAL FUNCTIONAL TEST', font=('Arial Bold', 20), size=20, expand_x=True, justification='center')],
    [sg.Column(functional_step_column),
    sg.VSeperator(),
    sg.Column(image_viewer_column)],
]

# Create Window
window = sg.Window("727-4251 Final Functional Test", layout, size=(900, 600), enable_close_attempted_event=True)

# Selection Button
while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no('Exit Test?') == 'Yes':
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == "Start":
            
            lBollardSN = values['LB']
            lCarrierSN = values['LC']
            rBollardSN = values['RB']
            rCarrierSN = values['RC']
            
            BollardSN = lBollardSN + '-' + rBollardSN
            CarrierSN = lCarrierSN + '-' + rCarrierSN
            
            window['SS'].update(BollardSN)
            window['CS'].update(CarrierSN)
            date = datetime.now().strftime('%H:%M:%S %m/%d/%y')
            window["DT"].update(date)
            
            
            if values["OP"] == '': 
                sg.popup_no_buttons('Operator Name is empty, please try again')
                break
            elif lBollardSN == '' or lCarrierSN == '' or rBollardSN == '' or rCarrierSN == '':
                sg.popup_no_buttons('Missing information, please fill them')
                break
            
            #Test begin
            
            #0 Pre-test - Done
            import PreTest
            Test0Result = PreTest.run()
            
            if Test0Result:
                window['T0'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            
            #1 Power On - Done
            import PowerOn
            Test1Result = PowerOn.run()
            
            if Test1Result:
                window['T1'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #2 Connectivity - Done
            import Connectivity
            Test2Result = Connectivity.run()
            
            if Test2Result:
                window['T2'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #3 SysFunc - Done
            import SysFunc
            Test2Result = SysFunc.run()
            
            if Test2Result:
                window['T3'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            
            #4 MagSen - Done
            import MagSen 
            Test2Result = MagSen.run()
            
            if Test2Result:
                window['T4'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #5 Calibrate - Done
            import Calibrate
            Test2Result = Calibrate.run()
            
            if Test2Result:
                window['T5'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #6 Set Overlay - Done
            import SetOverlay
            Test2Result = SetOverlay.run()
            
            if Test2Result:
                window['T6'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #7 Tripwire - Done
            import Tripwire
            Test2Result = Tripwire.run()
            
            if Test2Result:
                window['T7'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #8 Tamper Switch - Done
            import TamperSwitch
            Test2Result = TamperSwitch.run()
            
            if Test2Result:
                window['T8'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #9 MAG Coil - Semi-Done, need to add proper directory
            import MAGCoil
            Test2Result = MAGCoil.run(BollardSN)
            
            if Test2Result:
                window['T9'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #10 Walk Setup - 
            import WalkSetup
            Test2Result = WalkSetup.run()
            
            if Test2Result:
                window['T10'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #11 Control Walk
            import ControlWalk
            Test2Result = ControlWalk.run()
            
            if Test2Result:
                window['T11'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #12 Magnet Walk
            import MagnetWalk
            Test2Result = MagnetWalk.run()
            
            if Test2Result:
                window['T12'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #13 Object Location
            import ObjectLocation
            Test2Result = ObjectLocation.run()
            
            if Test2Result:
                window['T13'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #14 Data Cleanup
            import DataCleanup
            Test2Result = DataCleanup.run()
            
            if Test2Result:
                window['T14'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            #15 Post-test
            import PostTest
            Test2Result = PostTest.run()
            
            if Test2Result:
                window['T15'].update('Pass')
            else:
                #fail
                sg.popup_ok("Functional Test Failed")
                break
            
            
