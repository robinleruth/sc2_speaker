from tkinter import Frame
from tkinter import Label

from app.interface.gui.manage_view import ManageView


class MainComponent(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.title = Label(self, text='TEMP')
        self.manage_view = ManageView(self)

        self.title.pack()
        self.manage_view.pack()
