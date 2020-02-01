from app.domain.service.action_connector import ActionConnector


class TestActionConnector(ActionConnector):
    def get_action_list() -> List[Action]:
        a = Action(time=1, name="action1")
        b = Action(time=1, name="action2")
        c = Action(time=2, name="action3")
        lst = [a, b, c]
        return lst
