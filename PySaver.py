"""
PySaver 0.1
A PyQt5 Appindicator for selecting Power Profiles under XFCE4.
***
# Brief Description
This small and humble utility I created allows you to switch between different power profiles.
It makes use of the 'powerprofilesctl' utility present in many Linux machines. I could not find
any satisfying way for switching between power profiles, so I decided to create my own utility.
I hope you can easily exploit it: enjoy! 
***
Author: Guido Mascia, PhD
Email: mascia.guido@gmail.com
Last Edit: 01.20.2024
"""

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import subprocess
from subprocess import run
import tkinter as tk
import tkinter.messagebox as tkmb

# Check which profile is currently active
tmp = str(subprocess.check_output(["powerprofilesctl", "get"]))
tmp1 = tmp.replace("b'", "")
tmp2 = tmp1.replace("\\n", "")
profile_0 = tmp2.replace("'", "")

app = QApplication([]) 
app.setQuitOnLastWindowClosed(False) 

def switch_to_ps():
    subprocess.call(["powerprofilesctl", "set", "power-saver"])
    option2.setChecked(False)
    option3.setChecked(False)

def switch_to_bal():
    subprocess.call(["powerprofilesctl", "set", "balanced"])
    option1.setChecked(False)
    option3.setChecked(False)

def switch_to_per():
    subprocess.call(["powerprofilesctl", "set", "performance"])
    option1.setChecked(False)
    option2.setChecked(False)

def show_about():
    info_message = "PSave 0.1\n\nCreated by Guido Mascia, PhD\n\nmascia.guido@gmail.com"
    # info message box
    tkmb.showinfo("About", info_message)

# Adding an icon 
icon = QIcon("/usr/share/icons/gnome/24x24/categories/xfce4-settings.png") 
  
# Adding item on the menu bar 
tray = QSystemTrayIcon() 
tray.setIcon(icon) 
tray.setVisible(True) 
  
# Creating the options 
menu = QMenu()

option1 = QAction("power-saver", checkable=True)
if profile_0 == "power-saver":
    option1.setChecked(True)

option2 = QAction("balanced", checkable=True)
if profile_0 == "balanced":
    option2.setChecked(True)
        
option3 = QAction("performance", checkable=True)
if profile_0 == "performance":
    option3.setChecked(True)

option1.triggered.connect( switch_to_ps )
option2.triggered.connect( switch_to_bal )
option3.triggered.connect( switch_to_per )

menu.addAction(option1)
menu.addAction(option2)
menu.addAction(option3)

about = QAction("About")
about.triggered.connect(show_about)
menu.addAction(about)

# To quit the app 
quit = QAction("Quit") 
quit.triggered.connect(app.quit) 
menu.addAction(quit) 

# Adding options to the System Tray 
tray.setContextMenu(menu) 
  
app.exec_() 