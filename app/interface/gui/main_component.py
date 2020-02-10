from tkinter import Frame
from tkinter import Label

from app.interface.gui.manage_view import ManageView
from app.interface.gui.run_view import RunView
from app.interface.gui.manage_param_view import ManageParamView
from app.infrastructure.singleton import Singleton


class MainComponent(Frame, metaclass=Singleton):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.title = Label(self, text='SC2 SPEAKER')
        self.manage_view = ManageView(self)
        self.run_view = RunView(self)
        self.param_view = ManageParamView(self)

        self.title.pack()
        self.run_view.pack()
        self.manage_view.pack()
        self.param_view.pack()
        self.run_view.pack_forget()
        self.manage_view.pack_forget()
        self.param_view.pack_forget()

    def switch(self, component_name: str):
        if component_name.upper() == 'START':
            self.run_view.pack()
            self.manage_view.pack_forget()
            self.param_view.pack_forget()
        elif component_name.upper() == 'MANAGE':
            self.run_view.pack_forget()
            self.manage_view.pack()
            self.param_view.pack_forget()
        elif component_name.upper() == 'PARAM':
            self.run_view.pack_forget()
            self.manage_view.pack_forget()
            self.param_view.pack()
        else:
            raise NotImplementedError('{} Not implemented'.format(component_name))
