from typing import List
from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

from app.domain.model.action import Action
from app.domain.service.action_type import ActionType
from app.interface.gui.action_view import ActionView
from app.interface.gui.status_bar import StatusBar


class ActionListView(Frame):
    def __init__(self, parent, actions: List[Action], action_type: ActionType):
        Frame.__init__(self, parent)
        self.parent = parent
        self.action_type = action_type
        text = 'FIXED_ACTION' if action_type is ActionType.FIXED_ACTION else 'REPETITIVE_ACTION'
        self.label = Label(self, text=text)
        self.label.pack()
        title = ActionView(self, Action(time="Time", name="Name"))
        title.delete_button.destroy()
        title.pack()

        self.list_frame = Frame(self)

        for action in actions:
            component = ActionView(self.list_frame, action, self)
            component.pack()

        self.list_frame.pack()

        add_action_frame = Frame(self)
        self.new_time = Entry(add_action_frame)
        self.new_name = Entry(add_action_frame)
        new_button = Button(add_action_frame, text="Add action", command=self.add_action)


        self.new_name.grid(column=0, row=0)
        self.new_time.grid(column=1, row=0)
        new_button.grid(column=2, row=0)
        add_action_frame.pack()

    def delete_entry(self, action: Action):
        self.parent.delete_entry(action, self.action_type)
        StatusBar().set_label(f'{action} has been deleted')

    def add_action(self):
        time = self.new_time.get()
        name = self.new_name.get()
        action = Action(time=time, name=name)
        self.parent.add_entry(action, self.action_type)
        component = ActionView(self.list_frame, action, self)
        component.pack()
        self.new_time.delete(0, 'end')
        self.new_name.delete(0, 'end')

        StatusBar().set_label(f'{action} has been added')
