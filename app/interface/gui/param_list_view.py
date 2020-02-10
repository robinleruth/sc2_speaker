from tkinter import Frame
from typing import List

from app.domain.model.param import Param
from app.domain.service.param.param_service import ParamService
from app.interface.gui.param_view import ParamView


class ParamListView(Frame):
    def __init__(self, parent, params: List[Param], service: ParamService):
        Frame.__init__(self, parent)
        self.service = service

        for param in params:
            ParamView(self, param).pack()

    def delete_param(self, name):
        self.service.delete_param(name)
