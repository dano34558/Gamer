import pygame
from StateMachine import StateMachine
from GameStates.StartMenuState import StartMenuState

class GameManager:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("My Game")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

        self.state_machine = StateMachine(StartMenuState())

    def run(self):
        while True:
            self.clock.tick(60)

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Update current state
            self.state_machine.update()

            # Render current state
            self.screen.fill((0, 0, 0))
            self.state_machine.render(self.screen)
            pygame.display.flip()

if __name__ == "__main__":
    game_manager = GameManager()
    game_manager.run()