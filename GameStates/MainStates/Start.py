from State import State

class Start(State):
    def __init__(self):
        super().__init__()

    def enter(self):
        print("Entering Start state")

    def exit(self):
        print("Exiting Start state")

    def update(self):
        pass

    def render(self, screen):
        pass