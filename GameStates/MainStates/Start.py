from GameStates.StartMenuStates.Menu import Menu
from StateMachine import StateMachine
from ..State import State
import pygame


class Start(State):
    def __init__(self):
        super().__init__()
        self.state_machine = StateMachine(Menu())
        

    def enter(self):
        print("Entering Start state")
        self.state_machine.switch_state(Menu())

    def exit(self):
        print("Exiting Start state")

    def update(self):
        self.state_machine.update()
        

    def render(self, screen):
        self.state_machine.render(screen)