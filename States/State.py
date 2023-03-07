class State:
    def __init__(self,_dialog):
        self.next_state = None
        self.dialog = _dialog
    def enter(self):
        pass

    def exit(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass

    def handle_events(self):
        pass