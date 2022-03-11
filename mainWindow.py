from tkinter import *
from gameWindow import GameWindow
import ctypes

class MainWindow:

	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('Случайная строка')

	def __init__(self):
		self.root = Tk()
		self.root.title("Камень-ножницы-бумага")

		img = PhotoImage(file='images/icon.gif')
		self.root.tk.call('wm', 'iconphoto', self.root._w, img)

		self.root.geometry("600x340+650+300")

		self.root.resizable(width=False, height=False)

		self.frame_left = Frame(width=10, height=70, bg="black", colormap="new")
		self.frame_right = Frame(width=10, height=70, bg="black", colormap="new")

		self.frame_up = Frame(width=160, height=10, bg="black", colormap="new")
		self.frame_down = Frame(width=160, height=10, bg="black", colormap="new")

		self.frame_left.pack()
		self.frame_left.place(relx=.375, rely=.5, anchor="c")

		self.frame_right.pack()
		self.frame_right.place(relx=.625, rely=.5, anchor="c")

		self.frame_down.pack()
		self.frame_down.place(relx=.5, rely=.619, anchor="c")

		self.frame_up.pack()
		self.frame_up.place(relx=.5, rely=.382, anchor="c")

	def create_game_window(self):
		self.root.withdraw()
		GameWindow().run()
		
	def open_game_window(self):
		btn = Button(
			text="START A GAME",
			fg="#fff",
			bg='#ffca18',
			activeforeground='#fff',
			activebackground='#0ed145',
			font="Calibri 14 bold",
			relief='flat',
			command=self.create_game_window
			)
		btn.pack()

		btn.place(relx=.5, rely=.5, anchor="c", height=70, width=140,)

	def run (self):
		self.open_game_window()
		self.root.mainloop()

