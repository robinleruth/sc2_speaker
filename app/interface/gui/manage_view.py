from tkinter import Frame

from app.domain.service.main_service import MainService
from app.domain.service.action_type import ActionType
from app.domain.model.action import Action
from app.interface.gui.aciton_list_view import ActionListView


class ManageView(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.service = MainService()
        lst = self.service.fixed_action_service.get_action_list()
        self.fixed_action_service_view = ActionListView(self, lst,
                                                        ActionType.FIXED_ACTION)
        lst = self.service.repetitive_action_service.get_action_list()
        self.repetitive_action_service_view = ActionListView(self, lst,
                                                             ActionType.REPETITIVE_ACTION)

        self.fixed_action_service_view.grid(column=0, row=0)
        self.repetitive_action_service_view.grid(column=2, row=0)

    def delete_entry(self, action: Action, action_type: ActionType):
        self.service.delete_action(action, action_type)
