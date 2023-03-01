from State import State

class Running(State):
    def __init__(self):
        super().__init__()

    def enter(self):
        print("Entering Running state")

    def exit(self):
        print("Exiting Running state")

    def update(self):
        pass

    def render(self, screen):
        pass