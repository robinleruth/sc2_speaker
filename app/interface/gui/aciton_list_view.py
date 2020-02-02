from typing import List
from tkinter import Frame
from tkinter import Label

from app.domain.model.action import Action
from app.domain.service.action_type import ActionType
from app.interface.gui.action_view import ActionView


class ActionListView(Frame):
    def __init__(self, parent, actions: List[Action], action_type: ActionType):
        Frame.__init__(self, parent)
        self.parent = parent
        self.action_type = action_type
        title = ActionView(self, Action(time="Time", name="Name"))
        title.delete_button.destroy()
        title.pack()

        for action in actions:
            component = ActionView(self, action)
            component.pack()

    def delete_entry(self, action: Action):
        self.parent.delete_entry(action, self.action_type)
