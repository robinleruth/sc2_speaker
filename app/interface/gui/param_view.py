from tkinter import Frame
from tkinter import Label
from tkinter import Entry
from tkinter import Button

from app.domain.model.param import Param
from app.domain.service.param.param_name import ParamName


class ParamView(Frame):
    def __init__(self, parent, param: Param = None):
        Frame.__init__(self, parent)
        self.parent = parent

        if param:
            self.name = Label(self, text=param.name)
            self.value = Label(self, text=param.value)
            Button(self, text='Delete', command=self.delete_param).grid(column=2, row=0)
        else:
            self.name = Entry(self)
            self.value = Entry(self)
            Button(self, text='Add', command=self.add_param).grid(column=2, row=0)

        self.name.grid(column=0, row=0)
        self.value.grid(column=1, row=0)

    def add_param(self):
        self.parent.add_param(self.name.get(), self.value.get())

    def delete_param(self):
        name = ParamName(self.name['text'])
        self.parent.delete_param(name)
        self.destroy()
