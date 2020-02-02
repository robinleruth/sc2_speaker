from typing import List
from tkinter import Frame
from tkinter import Label

from app.domain.model.action import Action
from app.interface.gui.action_view import ActionView


class ActionListView(Frame):
    def __init__(self, parent, actions: List[Action]):
        Frame.__init__(self, parent)
        self.name = Label(self, text="Name")
        self.time = Label(self, text="Time")

        self.name.grid(column=0, row=0)
        self.time.grid(column=1, row=0)

        for action in actions:
            component = ActionView(self, action)
            component.pack()
