import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("My Game")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                    
            # Update the state machine
            self.state_machine.update()
            
            # Redraw the screen
            self.screen.fill((255, 255, 255))
            pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

