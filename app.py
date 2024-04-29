from utils import Dice
from tkinter import *

# Defining colors
color1 = "#020f12"
color2 = "#05d7ff"
color3 = "#65e7ff"


# Create a window
window = Tk()

# Config window
window.configure(bg="grey")
window.geometry("700x700")
window.title("IS - Curiosity")
window.resizable(width=False, height=False)

main_frame = Frame(window, bg=color1, pady=40)
main_frame.pack(fill=BOTH, expand=True)
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)

# Roll button
roll_button = Button(
    main_frame,
    text="Roll!",
    background=color2,
    foreground="BLACK",
    activebackground=color3,
    activeforeground="BLACK",
    highlightthickness=2,
    highlightbackground=color2,
    highlightcolor='WHITE',
    width=13,
    height=2,
    border=0,
    cursor='hand2',
    font=("Arial", 16, 'bold')
)

roll_button.grid(column=0, row=0)
# padding
roll_button.pack(padx=10, pady=15)

def roll_button_enter(event):
    roll_button.config(
        background=color3
    )

def roll_button_leave(event):
    roll_button.config(
        background=color2
    )

roll_button.bind('<Enter>', roll_button_enter)
roll_button.bind('<Leave>', roll_button_leave)

# Run Window
window.mainloop()


# TO DO
# Spawn dice based on button click

# Build out button making utils
# position roll button a bit better