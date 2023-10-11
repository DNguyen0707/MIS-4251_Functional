#!/usr/bin/env python3

# Import packages
from datetime import datetime  # to get today date
import PySimpleGUI as sg  # GUI window
from pathlib import Path  # make folder
import pyautogui as pyautogui  # to screenshot monitor

# Import test module
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
testModule_path = os.path.join(current_dir, "Test_Modules")
sys.path.append("Test_Modules")


# Set font
sg.set_options(font=("Arial Bold", 14))

# Result column
image_viewer_column = [
    [sg.Image(key="-IMAGE-")],
    [sg.Text("Pre-Test Result: ", size=(22, 1)), sg.Text(key="T0")],  # Pre-Test
    [sg.Text("Test Step 1 Result: ", size=(22, 1)), sg.Text(key="T1")],  # Power On
    [sg.Text("Test Step 2 Result: ", size=(22, 1)), sg.Text(key="T2")],  # Connectivity
    [sg.Text("Test Step 2 Result: ", size=(22, 1)), sg.Text(key="T3")],  # SysFunc
    [sg.Text("Test Step 4 Result: ", size=(22, 1)), sg.Text(key="T4")],  # MagSen
    [sg.Text("Test Step 5 Result: ", size=(22, 1)), sg.Text(key="T5")],  # Calibrate
    [sg.Text("Test Step 6 Result: ", size=(22, 1)), sg.Text(key="T6")],  # Set Overlay
    [sg.Text("Test Step 7 Result: ", size=(22, 1)), sg.Text(key="T7")],  # Tripwire
    [sg.Text("Test Step 8 Result: ", size=(22, 1)), sg.Text(key="T8")],  # Tamper Switch
    [sg.Text("Test Step 9 Result: ", size=(22, 1)), sg.Text(key="T9")],  # MAG coil
    [sg.Text("Test Step 10 Result: ", size=(22, 1)), sg.Text(key="T10")],  # Walk Setup
    [sg.Text("Test Step 11 Result: ", size=(22, 1)), sg.Text(key="T11")],  # Walking Test
    [sg.Text("Test Step 13 Result: ", size=(22, 1)), sg.Text(key="T13")],  # Object Locator
    [sg.Text("Test Step 14 Result: ", size=(22, 1)), sg.Text(key="T14")],  # Data Cleanup
    [sg.Text("Final Test Result: ", size=(22, 1)), sg.Text(key="T15")],  # Post-Test
]

# Filling column
functional_step_column = [
    [sg.Text("Operator Name: ", size=(22, 1)), sg.InputText(size=(20, 1), key="OP")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text("System Serial Number: ", size=(22, 1)), sg.Text(key="SS")],
    [sg.Text("Carrier Serial Number: ", size=(22, 1)), sg.Text(key="CS")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text("Left Bollard SN: ", size=(22, 1)), sg.InputText(size=(20, 1), key="LB")],
    [sg.Text("Left Carrier SN: ", size=(22, 1)), sg.InputText(size=(20, 1), key="LC")],
    [sg.Text("Right Bollard SN: ", size=(22, 1)), sg.InputText(size=(20, 1), key="RB")],
    [sg.Text("Right Carrier SN: ", size=(22, 1)), sg.InputText(size=(20, 1), key="RC")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text("Date: ", size=(22, 1)), sg.Text(key="DT")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Text("Press Start to begin the Test.")],
    [sg.Button("Start"), sg.Exit()],
]

# Full Layout
layout = [
    [sg.Text("727-4251 MIS BOLLARDS FINAL FUNCTIONAL TEST",font=("Arial Bold", 20),size=20,expand_x=True,justification="center")],
    [sg.Column(functional_step_column),sg.VSeperator(),sg.Column(image_viewer_column)],
]

# Create Window
window = sg.Window("727-4251 Final Functional Test",layout,size=(900, 550),enable_close_attempted_event=True)

# Selection Button
while True:
    event, values = window.read()
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT and sg.popup_yes_no("Exit Test?") == "Yes"):
        break
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Start":
        
        #Save values
        lBollardSN = values["LB"]
        lCarrierSN = values["LC"]
        rBollardSN = values["RB"]
        rCarrierSN = values["RC"]

        # Save bollard value (LEFT-RIGHT)
        BollardSN = lBollardSN + "-" + rBollardSN
        
        # Save carrier value (SMALL-BIG)
        if int(lCarrierSN) < int(rCarrierSN):
            CarrierSN = str(lCarrierSN) + "-" + str(rCarrierSN)
        else:
            CarrierSN = str(rCarrierSN) + "-" + str(lCarrierSN)

        # Update informations
        window["SS"].update(BollardSN)
        window["CS"].update(CarrierSN)
        date = datetime.now().strftime("%H:%M:%S %m/%d/%y")
        window["DT"].update(date)

        if values["OP"] == "":
            sg.popup_no_buttons("Operator Name is empty, please try again")
            break
        elif (lBollardSN == "" or lCarrierSN == "" or rBollardSN == "" or rCarrierSN == ""):
            sg.popup_no_buttons("Missing information, please fill them")
            break

        # Test begin

        # 0 Pre-test
        import PreTest
        Test0Result = PreTest.run()
        if Test0Result:
            window["T0"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 1 Power On
        import PowerOn
        Test1Result = PowerOn.run()
        if Test1Result:
            window["T1"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 2 Connectivity
        import Connectivity
        Test2Result = Connectivity.run()
        if Test2Result:
            window["T2"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 3 SysFunc
        import SysFunc
        Test3Result = SysFunc.run()
        if Test3Result:
            window["T3"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 4 MagSen
        import MagSen
        Test4Result = MagSen.run()
        if Test4Result:
            window["T4"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 5 Calibrate
        import Calibrate
        Test5Result = Calibrate.run()
        if Test5Result:
            window["T5"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 6 Set Overlay
        import SetOverlay
        Test6Result = SetOverlay.run()
        if Test6Result:
            window["T6"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 7 Tripwire
        import Tripwire
        Test7Result = Tripwire.run()
        if Test7Result:
            window["T7"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 8 Tamper Switch
        import TamperSwitch
        Test8Result = TamperSwitch.run()
        if Test8Result:
            window["T8"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 9 MAG Coil
        import MAGCoil
        Test9Result = MAGCoil.run(BollardSN)
        if Test9Result:
            window["T9"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 10 Walk Setup
        import WalkSetup
        Test10Result = WalkSetup.run()
        if Test10Result:
            window["T10"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 11 Walking Test
        import WalkingTest
        Test11Result = WalkingTest.run()
        controlWalk = int(Test11Result[0])
        magnetwalk = int(Test11Result[1])
        print(magnetwalk)
        if controlWalk <= 1 and magnetwalk >= 9:
            window["T11"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 13 Object Location
        import ObjectLocation
        Test13Result = ObjectLocation.run(BollardSN)
        objectWalk = int(Test13Result[0] + Test13Result[1])
        print(objectWalk)
        if objectWalk >= 9:
            window["T13"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 14 Data Cleanup
        import DataCleanup
        Test14Result = DataCleanup.run()
        if Test14Result:
            window["T14"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break

        # 15 Post-test
        import PostTest
        Test15Result = PostTest.run(
            BollardSN,
            CarrierSN,
            lBollardSN,
            rBollardSN,
            values["OP"],
            date,
            controlWalk,
            magnetwalk,
            objectWalk,
        )
        if Test15Result:
            window["T15"].update("Pass")
        else:
            # fail
            sg.popup_ok("Functional Test Failed")
            break
        
        sg.popup_ok("Functional Test Passed")
