from tkinter import Frame
from tkinter import Label

from app.infrastructure.singleton import Singleton


class StatusBar(Frame, metaclass=Singleton):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.label = Label(self, text='Initialisation done')

        self.label.pack()

    def set_label(self, value: str):
        self.label['text'] = value
