from tkinter import Frame
from tkinter import Label
from tkinter import Button

from app.domain.model.action import Action


class ActionView(Frame):
    def __init__(self, parent, action: Action, list_parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.list_parent = list_parent
        self.action = action
        self.name = Label(self, text=action.name)
        self.time = Label(self, text=action.time)
        self.delete_button = Button(self, text="Delete",
                                    command=self.delete_entry)

        self.name.grid(column=0, row=0)
        self.time.grid(column=1, row=0)
        self.delete_button.grid(column=2, row=0)

    def delete_entry(self):
        self.list_parent.delete_entry(self.action)
        self.destroy()

    def forget_delete_button(self):
        self.delete_button.grid_forget()
