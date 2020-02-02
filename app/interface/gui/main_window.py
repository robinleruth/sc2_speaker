from tkinter import Frame

from app.interface.gui.main_component import MainComponent
from app.interface.gui.nav_bar import NavBar
from app.interface.gui.tool_bar import ToolBar
from app.interface.gui.status_bar import StatusBar


class MainWindow(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.main_component = MainComponent(self)
        self.nav_bar = NavBar(self)
        self.tool_bar = ToolBar(self)
        self.status_bar = StatusBar(self)

        self.nav_bar.pack(side="left", fill="y")
        self.tool_bar.pack(side="top", fill="x")
        self.status_bar.pack(side="bottom", fill="x")
        self.main_component.pack(side="right", fill="both", expand=True)
