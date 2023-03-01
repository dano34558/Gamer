from State import State

class Exit(State):
    def __init__(self):
        super().__init__()

    def enter(self):
        print("Entering Exit state")

    def exit(self):
        print("Exiting Exit state")

    def update(self):
        pass

    def render(self, screen):
        pass