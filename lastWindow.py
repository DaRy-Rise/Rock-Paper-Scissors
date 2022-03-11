from tkinter import *
import random
from PIL import Image as PilImage
from PIL import ImageTk
import os

class LastWindow:
	def __init__(self):
		self.root = Toplevel()
		self.root.title("Камень-ножницы-бумага")

		img = PhotoImage(file='images/icon.gif')
		self.root.tk.call('wm', 'iconphoto', self.root._w, img)

		self.root.geometry("600x340+650+300")

		self.root.resizable(width=False, height=False)

		self.imgf_left = PilImage.open("images/frame.png")
		self.imgf_left = self.imgf_left.resize((100, 100), PilImage.ANTIALIAS)
		self.image_frame_left = ImageTk.PhotoImage(self.imgf_left)

		self.imgf_right = PilImage.open("images/frame.png")
		self.imgf_right = self.imgf_right.resize((100, 100), PilImage.ANTIALIAS)
		self.image_frame_right = ImageTk.PhotoImage(self.imgf_right)

		self.label_frame_left = Label(self.root, image = self.image_frame_left)
		self.label_frame_left.image_frame_left = self.image_frame_left
		self.label_frame_left.place(relx=.77, rely=.5, anchor="c")

		self.label_frame_right = Label(self.root, image = self.image_frame_right)
		self.label_frame_right.image_frame_right = self.image_frame_right
		self.label_frame_right.place(relx=.23, rely=.5, anchor="c")

		self.frame_left = Frame(self.root, width=10, height=64, bg="black", colormap="new").place(relx=.375, rely=.15, anchor="c")
		self.frame_right = Frame(self.root,width=10, height=64, bg="black", colormap="new").place(relx=.625, rely=.15, anchor="c")

		self.frame_up = Frame(self.root, width=160, height=10, bg="black", colormap="new").place(relx=.5, rely=.05, anchor="c")
		self.frame_down = Frame(self.root, width=160, height=10, bg="black", colormap="new").place(relx=.5, rely=.25, anchor="c")

		Label(self.root, width=10, height=1, text="YOU", fg="#000", bg="#fff", font="Calibri 15 bold").place(relx=.23, rely=.75, anchor="c")
		Label(self.root, width=10, height=1, text="BOT", fg="#000", bg="#fff", font="Calibri 15 bold").place(relx=.77, rely=.75, anchor="c")



	def random(self):
		bot = random.randint(1, 3)
		return bot

	def result(self, player, bot):

		x = None

		if player == bot:
			x = "n"
		if player == 1:
			if bot == 2:
				x = "w"
			if bot == 3:
				x = "l"
		elif player == 2:
			if bot == 1:
				x = "l"
			if bot == 3:
				x = "w"
		elif player == 3:
			if bot == 1:
				x = "w"
			if bot == 2:
				x = "l"

		return x

	def choose_img(self, who):
		if who == 1:
			self.img = self.image_rock
		elif who == 2:
			self.img = self.image_scissors
		elif who == 3:
			self.img = self.image_paper
		return self.img

	def loose_win(self, w_or_l):
		if w_or_l == 'n':
			self.img = self.image_nothing
		elif w_or_l == 'w':
			self.img = self.image_win
		elif w_or_l == 'l':
			self.img = self.image_loose
		return self.img

	def img_result(self, player, bot, w_or_l):

		self.imgr = PilImage.open("images/rock.png")
		self.imgr = self.imgr.resize((70, 70), PilImage.ANTIALIAS)
		self.image_rock = ImageTk.PhotoImage(self.imgr)

		self.imgp = PilImage.open("images/paper.png")
		self.imgp = self.imgp.resize((70, 70), PilImage.ANTIALIAS)
		self.image_paper = ImageTk.PhotoImage(self.imgp)

		self.imgs = PilImage.open("images/scissors.png")
		self.imgs = self.imgs.resize((70, 70), PilImage.ANTIALIAS)
		self.image_scissors = ImageTk.PhotoImage(self.imgs)

		self.imgw = PilImage.open("images/winner.png")
		self.imgw = self.imgw.resize((89, 89), PilImage.ANTIALIAS)
		self.image_win = ImageTk.PhotoImage(self.imgw)

		self.imgl = PilImage.open("images/loose.png")
		self.imgl = self.imgl.resize((89, 118), PilImage.ANTIALIAS)
		self.image_loose = ImageTk.PhotoImage(self.imgl)

		self.imgn = PilImage.open("images/tie.png")
		self.imgn = self.imgn.resize((70, 70), PilImage.ANTIALIAS)
		self.image_nothing = ImageTk.PhotoImage(self.imgn)

		self.img = self.choose_img(player)

		self.label_for_player = Label(self.root, image = self.img)
		self.label_for_player.img = self.img
		self.label_for_player.place(relx=.23, rely=.5, anchor="c")

		self.img = self.choose_img(bot)

		self.label_for_bot = Label(self.root, image = self.img)
		self.label_for_bot.img = self.img
		self.label_for_bot.place(relx=.77, rely=.5, anchor="c")

		self.img = self.loose_win(w_or_l)

		self.label_for_w_l = Label(self.root, image = self.img)
		self.label_for_w_l.img = self.img
		self.label_for_w_l.place(relx=.5, rely=.5, anchor="c")

	def again(self):

		Button(self.root, bg='#ffca18', fg="#fff", text = "AGAIN", relief='flat',activebackground='#0ed145', font="Calibri 14 bold", command=self.create_main_window).place(relx=.5, rely=.15, anchor="c", height=60, width=140)

	def create_main_window(self):
		self.root.withdraw()
		os.system('main.py')

	def run(self, player):
		bot = self.random()
		w_or_l = self.result(player, bot)
		self.img_result(player, bot, w_or_l)
		self.again()
		self.root.mainloop()



