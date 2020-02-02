from typing import List
from tkinter import Frame
from tkinter import Label

from app.domain.model.action import Action
from app.interface.gui.action_view import ActionView


class ActionListView(Frame):
    def __init__(self, parent, actions: List[Action]):
        Frame.__init__(self, parent)
        ActionView(self, Action(time="Time", name="Name")).pack()

        for action in actions:
            component = ActionView(self, action)
            component.pack()
