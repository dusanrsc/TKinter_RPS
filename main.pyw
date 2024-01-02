# all static files (images) need to be in the same directory as main.py for proper working!
# importing modules
import tkinter
import random

# importing sub-modules (classes, functions etc...)
from tkinter import Tk, Button, Label, FLAT
from random import randint
from PIL import Image, ImageTk

# game functions
def rock():
	# player choice
	player_choice = "rock"

	# cpu choice
	cpu_choice = random.randint(0, 2)

	# cpu choice drawing
	if cpu_choice == 0:
		cpu_label.config(image=rock1)
	elif cpu_choice == 1:
		cpu_label.config(image=paper1)
	elif cpu_choice == 2:
		cpu_label.config(image=scissors1)

	# game logic
	# tie game logic
	if cpu_choice == 0 and player_choice == "rock":
		vs_label.config(image=vst)
	elif cpu_choice == 1 and player_choice == "paper":
		vs_label.config(image=vst)
	elif cpu_choice == 2 and player_choice == "scissors":
		vs_label.config(image=vst)

	# player win game logic
	if cpu_choice == 0 and player_choice == "paper":
		vs_label.config(image=vsp)
	elif cpu_choice == 1 and player_choice == "scissors":
		vs_label.config(image=vsp)
	elif cpu_choice == 2 and player_choice == "rock":
		vs_label.config(image=vsp)

	# cpu win game logic
	if cpu_choice == 0 and player_choice == "scissors":
		vs_label.config(image=vsc)
	elif cpu_choice == 1 and player_choice == "rock":
		vs_label.config(image=vsc)
	elif cpu_choice == 2 and player_choice == "paper":
		vs_label.config(image=vsc)

def paper():
	# player choice
	player_choice = "paper"

	# cpu choice
	cpu_choice = random.randint(0, 2)

	# cpu choice drawing
	if cpu_choice == 0:
		cpu_label.config(image=rock1)
	elif cpu_choice == 1:
		cpu_label.config(image=paper1)
	elif cpu_choice == 2:
		cpu_label.config(image=scissors1)

	# game logic
	# tie game logic
	if cpu_choice == 0 and player_choice == "rock":
		vs_label.config(image=vst)
	elif cpu_choice == 1 and player_choice == "paper":
		vs_label.config(image=vst)
	elif cpu_choice == 2 and player_choice == "scissors":
		vs_label.config(image=vst)

	# player win game logic
	if cpu_choice == 0 and player_choice == "paper":
		vs_label.config(image=vsp)
	elif cpu_choice == 1 and player_choice == "scissors":
		vs_label.config(image=vsp)
	elif cpu_choice == 2 and player_choice == "rock":
		vs_label.config(image=vsp)

	# cpu win game logic
	if cpu_choice == 0 and player_choice == "scissors":
		vs_label.config(image=vsc)
	elif cpu_choice == 1 and player_choice == "rock":
		vs_label.config(image=vsc)
	elif cpu_choice == 2 and player_choice == "paper":
		vs_label.config(image=vsc)

def scissors():
	# player choice
	player_choice = "scissors"

	# cpu choice
	cpu_choice = random.randint(0, 2)

	# cpu choice drawing
	if cpu_choice == 0:
		cpu_label.config(image=rock1)
	elif cpu_choice == 1:
		cpu_label.config(image=paper1)
	elif cpu_choice == 2:
		cpu_label.config(image=scissors1)

	# game logic
	# tie game logic
	if cpu_choice == 0 and player_choice == "rock":
		vs_label.config(image=vst)
	elif cpu_choice == 1 and player_choice == "paper":
		vs_label.config(image=vst)
	elif cpu_choice == 2 and player_choice == "scissors":
		vs_label.config(image=vst)

	# player win game logic
	if cpu_choice == 0 and player_choice == "paper":
		vs_label.config(image=vsp)
	elif cpu_choice == 1 and player_choice == "scissors":
		vs_label.config(image=vsp)
	elif cpu_choice == 2 and player_choice == "rock":
		vs_label.config(image=vsp)

	# cpu win game logic
	if cpu_choice == 0 and player_choice == "scissors":
		vs_label.config(image=vsc)
	elif cpu_choice == 1 and player_choice == "rock":
		vs_label.config(image=vsc)
	elif cpu_choice == 2 and player_choice == "paper":
		vs_label.config(image=vsc)

# game variables
# game version
__version__ = "v1.0"

# game constants
TITLE = "RPS"
SCREEN_WIDTH = "800"
SCREEN_HEIGHT = "600"

# rgb color constants
WHITE = "#FFFFFF"

ALPHA = "#0000FF"

BACKGROUND_COLOR = "#1F1F1F"

# creating main game window
# game settings
root = Tk()
root.title(f"{TITLE} {__version__}")
root.config(bg=BACKGROUND_COLOR)
root.resizable(False, False)
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

# loading images
# cpu image
cpu_img = Image.open("img.png")
cpu_img1 = ImageTk.PhotoImage(cpu_img)

# versus image
vs = Image.open("vst.png")
vst = ImageTk.PhotoImage(vs)

vs1 = Image.open("vsp.png")
vsp = ImageTk.PhotoImage(vs1)

vs2 = Image.open("vsc.png")
vsc = ImageTk.PhotoImage(vs2)

# rock image
rock_img = Image.open("rock.png")
rock1 = ImageTk.PhotoImage(rock_img)

# paper image
paper_img = Image.open("paper.png")
paper1 = ImageTk.PhotoImage(paper_img)

# scissors image
scissors_img = Image.open("scissors.png")
scissors1 = ImageTk.PhotoImage(scissors_img)

# drawing items on main root
# cpu label
cpu_label = Label(root, image=cpu_img1)
cpu_label.place(x=300, y=50)

# versus label
vs_label = Label(root, image=vst, relief=FLAT)
vs_label.place(x=375, y=275)

# players rock button
rock_button = Button(root, image=rock1, relief=FLAT, command=rock)
rock_button.place(x=50, y=350)

# players paper button
paper_button = Button(root, image=paper1, relief=FLAT, command=paper)
paper_button.place(x=300, y=350)

# players scissors button
scissors_button = Button(root, image=scissors1, relief=FLAT, command=scissors)
scissors_button.place(x=550, y=350)

# starting game mainloop
root.mainloop()
