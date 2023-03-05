from ..State import State
import pygame

class TextboxState(State):
    def __init__(self):
        super().__init__()

    def enter(self):
        print("Entering Textbox state")

    def exit(self):
        print("Exiting Textbox state")

    def update(self):
        pass

    def render(self, screen):
        # Render the large text box in the center of the screen
        pygame.draw.rect(screen, (255, 255, 255), (100, 100, 600, 400))
        # Render some sample text
        font = pygame.font.SysFont(None, 24)
        text = font.render("This is a sample text box.", True, (0, 0, 0))
        screen.blit(text, (120, 120))

       
        