from GameStates.MainStates.Start import Start
from StateMachine import StateMachine
import pygame

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("MY GaME")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.state_machine = StateMachine(Start())  # initialize with StartState

    def run(self):
        while True:
            

            self.state_machine.update()
            self.state_machine.render(self.screen)

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()