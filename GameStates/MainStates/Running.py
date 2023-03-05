from StateMachine import StateMachine
from ..State import State
from ..RunningStates.simple_game_state import TextboxState
import pygame


class Running(State):
    def __init__(self):
        super().__init__()
        self.state_machine = StateMachine(TextboxState())  # Start with TextboxState as default sub-state

    def enter(self):
        print("Entering Running state")
        self.state_machine.switch_state(TextboxState())  # Switch to TextboxState on entering the Running state

    def exit(self):
        print("Exiting Running state")

    def update(self):
        self.state_machine.update()

    def render(self, screen):
        self.state_machine.render(screen)