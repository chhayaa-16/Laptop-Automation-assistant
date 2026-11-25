import os
import sys
import platform
import socket
import datetime
import webbrowser
import win32com.client as win32
import psutil # process and sysytem utilities
import screen_brightness_control as sbc
import asyncio
from winrt.windows.devices.radios import Radio, RadioKind, RadioState,RadioAccessStatus
import cv2

speaker = win32.Dispatch("SAPI.SpVoice")
speaker.Volume = 100
speaker.Rate = 0 #speed of speech

def speak_and_print(text:str):
    print("assistant_response : ",text)
    speaker.speak(text)


async def bluetooth_task(command):

    radios = await Radio.get_radios_async()

    bluetooth_radio = next(
        (radio for radio in radios if radio.kind == RadioKind.BLUETOOTH),
        None
    )

    if bluetooth_radio is None:
        speak_and_print("Bluetooth adapter not found.")
        return

    print("Current Bluetooth State:", bluetooth_radio.state)

    if "turn on bluetooth" in command:

        result = await bluetooth_radio.set_state_async(RadioState.ON)

        print("ON Result:", result)

        if result == RadioAccessStatus.ALLOWED:
            speak_and_print("Bluetooth turned ON successfully.")
        else:
            speak_and_print(f"Unable to turn ON Bluetooth. Reason: {result}")

    elif "turn off bluetooth" in command:

        result = await bluetooth_radio.set_state_async(RadioState.OFF)

        print("OFF Result:", result)

        print("Bluetooth State After Request:", bluetooth_radio.state)

        if result == RadioAccessStatus.ALLOWED:
            speak_and_print("Bluetooth turned OFF successfully.")
        else:
            speak_and_print(f"Unable to turn OFF Bluetooth. Reason: {result}")

    else:

        if bluetooth_radio.state == RadioState.ON:
            speak_and_print("Bluetooth is currently ON.")

        elif bluetooth_radio.state == RadioState.OFF:
            speak_and_print("Bluetooth is currently OFF.")

        else:
            speak_and_print(f"Bluetooth state: {bluetooth_radio.state}")
def laptop_task(command:str):
    cmd = command.lower().strip()   #convert command to lower case and remove extra spaces in user input

    if any(word in cmd for word in["battery","charging","power","charged","pluged","power","capacity"]):
        battery = psutil.sensors_battery()  #laptop battery information store in battery variable
        if battery:
            percent = battery.percent
            if_plug = "plugged in" if battery.power_plugged else "not plugged in"

            print(f"Battery: {percent}% | Charging: {if_plug}")
            speak_and_print(f"battery percentage is: {percent} and charge is {if_plug}")
        else:
                speak_and_print("Battery information is not available.")
    

    if any(word in cmd for word in["time","date","day"]):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")     # strftime() method is used to format date and time in a specific way. Here, %H:%M:%S represents hours, minutes, and seconds in 24-hour format.
        current_date = now.strftime("%Y-%m-%d")         #strftime() ----string format time
        current_day = now.strftime("%A")   
        speak_and_print(f"Current time is: {current_time} and today's date is: {current_date} and today is: {current_day}")
       

    if any(word in cmd for word in["ram","memory"]):
        ram = psutil.virtual_memory()    #provide ram information 
        total_ram = round(ram.total / (1024 ** 3), 2)  # Convert bytes to gb
        available_ram = round(ram.available / (1024 ** 3), 2)
        speak_and_print(f"Total RAM: {total_ram} GB, Available RAM: {available_ram} GB")

    if any(word in cmd for word in["cpu","processor"]):
        cpu_usage = psutil.cpu_percent(interval=1)     # interval=1 means it will calculate the CPU usage over a 1-second period
        speak_and_print(f"CPU usage is: {cpu_usage}%")

    if any(word in cmd for word in["c drive","storage","disk","drive"]):
        c_drive = psutil.disk_usage('C:\\')      #.disk_usage() method is used to get disk information---- ('C:\\') fakt c drive cha access karaycha ahe
        free_space = round(c_drive.free / (1024 ** 3), 2)  
        speak_and_print(f"Free space on C drive: {free_space} GB")

    if any(word in cmd for word in["notepad","open notepad"]):
        os.system("notepad")
        speak_and_print("Opening Notepad.")

    if any(word in cmd for word in["calculator","open calculator","calc"]):
        os.system("calc")
        speak_and_print("Opening Calculator.")

    if any(word in cmd for word in["youtube","open youtube"]):
        webbrowser.open("https://www.youtube.com")
        speak_and_print("Opening YouTube.")

    if any(word in cmd for word in["google","open google"]):
        webbrowser.open("https://www.google.com")
        speak_and_print("Opening Google.")

    if any(word in cmd for word in["operating system","os details","system info","os"]):
        os_info = platform.uname()
        speak_and_print(f"Operating System: {os_info.system}, Version: {os_info.version}, Machine: {os_info.machine}")

    if any(word in cmd for word in["internet","connectivity","network","net"]):
        try:
            socket.create_connection(("www.google.com", 80))
            speak_and_print("Internet is connected.")
        except OSError:
            speak_and_print("Internet is not connected.")

        
    if any(word in cmd for word in["camera","open camera","cam"]):
        cap = cv2.VideoCapture(0)
        speak_and_print("Opening Camera.")
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow("Camera", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

    if any(word in cmd for word in["excel","open excel"]):
        os.system("start excel")
        speak_and_print("Opening Microsoft Excel.")

    if any(word in cmd for word in["powerbi","open powerbi"]):
        os.system("start powerbi")
        speak_and_print("Opening Microsoft Power BI.")

        # Bluetooth Control

    if "bluetooth" in cmd:

        asyncio.run(bluetooth_task(cmd))


    # Brightness Control

    if any(word in cmd for word in ["brightness", "increase brightness", "decrease brightness"]):

        current_brightness = sbc.get_brightness()[0]

        if "increase" in cmd:
            new_brightness = min(current_brightness + 10, 100)

            sbc.set_brightness(new_brightness)

            speak_and_print(
                f"Brightness increased to {new_brightness} percent."
            )

        elif "decrease" in cmd:
            new_brightness = max(current_brightness - 10, 0)

            sbc.set_brightness(new_brightness)

            speak_and_print(
                f"Brightness decreased to {new_brightness} percent."
            )

        else:
            speak_and_print(
                f"Current brightness is {current_brightness} percent."
            )
    
    # Open Email

    if any(word in cmd for word in ["email", "open email", "gmail", "open gmail"]):
        webbrowser.open("https://mail.google.com")
        speak_and_print("Opening Gmail.")


#    currenttime and todays date
#    ram and memory usage
#    cpu and processor usage
#    c drive free storage
#    open notepad
#    open calculator
#    open youtube and google in browser
#    operating system details 
#    internet on/off
#    open camera
#    open any app ----Excel / powerbi
#    turn on/off bluetooth
#    brightness (increase/decrease)
#     open email



if __name__ == "__main__":
    command = input("Enter a command for laptop task: ")
    laptop_task(command)
