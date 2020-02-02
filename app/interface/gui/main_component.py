from tkinter import Frame
from tkinter import Label


class MainComponent(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.title = Label(self, text='TEMP')

        self.title.pack()
