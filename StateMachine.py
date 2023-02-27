class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state

    def switch_state(self, state):
        self.current_state.exit()
        self.current_state = state
        self.current_state.enter()

    def update(self):
        if self.current_state.next_state is not None:
            self.switch_state(self.current_state.next_state)

        self.current_state.update()

