import pygame
from States.StateMachine import StateMachine
from States.Start import StartMenu
from DialogManager import DialogManager

class GameManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.dialog = DialogManager("")
        self.clock = pygame.time.Clock()
        self.state_machine = StateMachine(StartMenu(self.dialog))
        
    def run(self):
        while True:
            self.state_machine.update()
            self.state_machine.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()