from tkinter import Frame
from tkinter import Label
from tkinter import IntVar
from tkinter import Radiobutton

from app.infrastructure.singleton import Singleton
from app.interface.gui.status_bar import StatusBar
from app.interface.gui import lookup_table
from app.interface.gui.main_component import MainComponent


class NavBar(Frame, metaclass=Singleton):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        Label(self, text='NavBar').pack()
        self.var = IntVar()

        Radiobutton(self, text='Start', variable=self.var, value=1, command=self.switch).pack()
        Radiobutton(self, text='Manage', variable=self.var, value=2, command=self.switch).pack()

    def switch(self):
        value = lookup_table[self.var.get()]
        StatusBar().set_label(value)
        MainComponent().switch(value)
