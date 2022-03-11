from tkinter import *
from lastWindow import LastWindow
from PIL import Image as PilImage
from PIL import ImageTk

class GameWindow:

	def __init__(self):
		self.root = Toplevel()
		self.root.title("Камень-ножницы-бумага")

		img = PhotoImage(file='images/icon.gif')
		self.root.tk.call('wm', 'iconphoto', self.root._w, img)

		self.root.geometry("600x340+650+300")
		self.root['bg']='white'

		self.root.resizable(width=False, height=False)

		self.imgr = PilImage.open("images/rock.png")
		self.imgr = self.imgr.resize((45, 45), PilImage.ANTIALIAS)
		self.image_rock = ImageTk.PhotoImage(self.imgr)

		self.imgp = PilImage.open("images/paper.png")
		self.imgp = self.imgp.resize((45, 45), PilImage.ANTIALIAS)
		self.image_paper = ImageTk.PhotoImage(self.imgp)

		self.imgs = PilImage.open("images/scissors.png")
		self.imgs = self.imgs.resize((45, 45), PilImage.ANTIALIAS)
		self.image_scissors = ImageTk.PhotoImage(self.imgs)

		self.imgf = PilImage.open("images/frames.png")
		self.imgf = self.imgf.resize((380, 128), PilImage.ANTIALIAS)
		self.image_frames = ImageTk.PhotoImage((self.imgf))

		self.label1 = Label(self.root, width=35, height=1, text="Choose", fg="#fff", bg="#00a8f3", font="Calibri 15 bold")

		self.label1.place(relx=.5, rely=.2, anchor="c")

		self.frame_left = Frame(self.root, width=10, height=50, bg="black", colormap="new")
		self.frame_right = Frame(self.root, width=10, height=50, bg="black", colormap="new")

		self.frame_up = Frame(self.root, width=356, height=10, bg="black", colormap="new")
		self.frame_down = Frame(self.root, width=356, height=10, bg="black", colormap="new")

		self.frame_left.pack()
		self.frame_left.place(relx=.2, rely=.2, anchor="c")

		self.frame_right.pack()
		self.frame_right.place(relx=.805, rely=.2, anchor="c")

		self.frame_down.pack()
		self.frame_down.place(relx=.5, rely=.26, anchor="c")

		self.frame_up.pack()
		self.frame_up.place(relx=.5, rely=.14, anchor="c")

		self.label_for_img = Label(self.root, image = self.image_frames)
		self.label_for_img.image_frames = self.image_frames
		self.label_for_img.place(relx=.5, rely=.7, anchor="c")

	def choose_rock(self):
		Button(self.root, bg='#fff', text = "image", image=self.image_rock, relief='flat',activebackground='#0ed145', command=lambda: self.create_last_window(1)).place(relx=.293, rely=.71, anchor="c", height=62, width=65)

	def choose_scissors(self):
		Button(self.root, bg='#fff', text = "image", image=self.image_scissors, relief='flat',activebackground='#0ed145', command=lambda: self.create_last_window(2)).place(relx=.713, rely=.71, anchor="c", height=62, width=65)

	def choose_paper(self):
		Button(self.root, bg='#fff', text = "image", image=self.image_paper, relief='flat',activebackground='#0ed145', command=lambda: self.create_last_window(3)).place(relx=.504, rely=.71, anchor="c", height=62, width=65)


	def create_last_window(self, x):
		self.root.withdraw()
		LastWindow().run(x)

	def run (self):
		self.choose_rock()
		self.choose_paper()
		self.choose_scissors()
		self.root.mainloop()

	