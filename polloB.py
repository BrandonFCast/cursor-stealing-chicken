# The chicken image used in this program was made
# by Clint Bellanger and is used under the public
# domain license  specified at  the following URL
# https://opengameart.org/content/tiny-creatures
import tkinter as tk
import pyautogui
import time
import os
import sys

def resource_path(relative_path): # This function reads files as requested by the library (PyInstaller)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

# window config
vx = 10 # view x
vy = 10 # view y
x, y = pyautogui.position() # mouse position
window = tk.Tk()
pyautogui.FAILSAFE = False

# GUI
petLImg = tk.PhotoImage(file=resource_path("assets/polloL.png"))
bigPetLImg = petLImg.zoom(4, 4)
petRImg = tk.PhotoImage(file=resource_path("assets/polloR.png"))
bigPetRImg = petRImg.zoom(4, 4)

petLbl = tk.Label(window, image=bigPetLImg, bg='black')
petLbl.pack()

# constants
WINDOW_SIZE = 70

# others
cursor_in_window = False # if cursor is on the chicken it will be True
after_id = 0

def lose():
    global window
    pyautogui.moveTo(vx + WINDOW_SIZE / 2, vy + WINDOW_SIZE / 2, duration=0)
    window.after(10, lose)

def on_enter(event):
    global after_id, window, vy, vx
    window.after_cancel(after_id)
    lose()

def createWindow():

    # preparing the window
    global window, vx, vy, x, y
    window.configure(background='black', cursor="none")
    window.attributes('-transparentcolor', 'black')
    window.attributes('-topmost', True)
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+{vx}+{vy}")
    window.bind('<F3>', lambda e: window.destroy())
    window.overrideredirect(True)
    window.bind('<Enter>', on_enter)

    start()
    window.mainloop()

def start(): # This function starts the movement of the window
    global x, y, vx, vy, window, petLbl, cursor_in_window, after_id
    speed = 1
    x, y = pyautogui.position()
    if (x > vx + WINDOW_SIZE / 2):
        vx += speed
        petLbl.config(image=bigPetRImg)
        petLbl.image = bigPetRImg
    if (x < vx + WINDOW_SIZE / 2):
        vx -= speed
        petLbl.config(image=bigPetLImg)
        petLbl.image = bigPetLImg
    if (y > vy + WINDOW_SIZE / 2):
        vy += speed
    if (y < vy + WINDOW_SIZE / 2):
        vy -= speed
    window.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}+{int(vx)}+{int(vy)}")
    after_id = window.after(20, start)

time.sleep(10)
createWindow()