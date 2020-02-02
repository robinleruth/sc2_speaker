from tkinter import Frame
from tkinter import Label

from app.domain.model.action import Action


class ActionView(Frame):
    def __init__(self, parent, action: Action):
        Frame.__init__(self, parent)
        self.name = Label(self, text=action.name)
        self.time = Label(self, text=action.time)

        self.name.grid(column=0, row=0)
        self.time.grid(column=1, row=0)
