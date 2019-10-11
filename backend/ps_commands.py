from frontend.GUI import *
from tkinter import messagebox
import time
import subprocess

all_applications = {"3dbuilder": "Get-AppxPackage *3dbuilder* | Remove-AppxPackage",
                    "Alarm": "Get-AppxPackage *windowsalarms* | Remove-AppxPackage",
                    "Calculator": "Get-AppxPackage *windowscalculator* | Remove-AppxPackage",
                    "Skype": "Get-AppxPackage *skype* | Remove-AppxPackage",
                    "Get Started": "Get-AppxPackage *getstarted* | Remove-AppxPackage",
                    "Zune Music": "Get-AppxPackage *zunemusic* | Remove-AppxPackage",
                    "Maps": "Get-AppxPackage *windowsmaps* | Remove-AppxPackage",
                    "Solitaire": "Get-AppxPackage *solitairecollection* | Remove-AppxPackage",
                    "Finance": "Get-AppxPackage *bingfinance* | Remove-AppxPackage",
                    "Zune Video": "Get-AppxPackage *zunevideo* | Remove-AppxPackage",
                    "Bing News": "Get-AppxPackage *bingnews* | Remove-AppxPackage",
                    "OneNote": "Get-AppxPackage *onenote* | Remove-AppxPackage",
                    "Windows Phone": "Get-AppxPackage *windowsphone* | Remove-AppxPackage",
                    "Bing Sports": "Get-AppxPackage *bingsports* | Remove-AppxPackage",
                    "Voice Recorder": "Get-AppxPackage *soundrecorder* | Remove-AppxPackage",
                    "Bing Weather": "Get-AppxPackage *bingweather* | Remove-AppxPackage",
                    "Xbox": "Get-AppxPackage *xboxapp* | Remove-AppxPackage",
                    "Feedback Hub": "Get-AppxPackage *feedback* | Remove-AppxPackage",
                    "Wallet": "Get-AppxPackage *wallet* | Remove-AppxPackage",
                    "OneConnect": "Get-AppxPackage *oneconnect* | Remove-AppxPackage",
                    "Comms Phone": "Get-AppxPackage *commsphone* | Remove-AppxPackage",
                    "Sway": "Get-AppxPackage *sway* | Remove-AppxPackage"}

utility_apps = ["Get-AppxPackage *3dbuilder* | Remove-AppxPackage",
                "Get-AppxPackage *windowsalarms* | Remove-AppxPackage",
                "Get-AppxPackage *windowscalculator* | Remove-AppxPackage",
                "Get-AppxPackage *windowsmaps* | Remove-AppxPackage",
                "Get-AppxPackage *bingfinance* | Remove-AppxPackage", "Get-AppxPackage *bingnews* | Remove-AppxPackage",
                "Get-AppxPackage *onenote* | Remove-AppxPackage",
                "Get-AppxPackage *windowsphone* | Remove-AppxPackage",
                "Get-AppxPackage *soundrecorder* | Remove-AppxPackage",
                "Get-AppxPackage *bingweather* | Remove-AppxPackage", "Get-AppxPackage *wallet* | Remove-AppxPackage",
                "Get-AppxPackage *zunevideo* | Remove-AppxPackage",
                "Get-AppxPackage *bingnews* | Remove-AppxPackage"]

entertainment_apps = ["Get-AppxPackage *skype* | Remove-AppxPackage",
                      "Get-AppxPackage *zunemusic* | Remove-AppxPackage",
                      "Get-Appxpackage *solitairecollection* | Remove-AppxPackage",
                      "Get-AppxPackage *bingsports* | Remove-AppxPackage",
                      "Get-AppxPackage *xboxapp* | Remove-AppxPackage"]


def remove_all_applications():
    for commands in all_applications.values():
        subprocess.Popen(["powershell.exe", commands], stdout=subprocess.PIPE)
    while True:
        time.sleep(3)
        messagebox.showinfo(title="All Apps", message="All Apps have been removed")
        break


def remove_utilities():
    for commands in utility_apps:
        subprocess.Popen(["powershell.exe", commands], stdout=subprocess.PIPE)
    while True:
        time.sleep(2)
        messagebox.showinfo(title="Utility Apps", message="Utility Apps have been removed")
        break


def remove_entertainment():
    for commands in entertainment_apps:
        subprocess.Popen(["powershell.exe", commands], stdout=subprocess.PIPE)
    while True:
        time.sleep(2)
        messagebox.showinfo(title="Entertainment Apps", message="Entertainment Apps have been removed")
        break


def remove_app(command):
    subprocess.Popen(["powershell.exe", command], stdout=subprocess.PIPE)
    while True:
        time.sleep(1)
        messagebox.showinfo(title="Remove App", message="'{}' has been removed".format(command))
        break
