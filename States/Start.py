import pygame
from State import State
from ..States.Character import CharacterCreation

pygame.init()

class StartMenu(State):
    def __init__(self,_dialog):
        super().__init__()
        self.screen_width = 800
        self.screen_height = 600
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("MY GAME", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 100))
        self.start_button_text = self.font.render("Start", True, (255, 255, 255))
        self.start_button_rect = self.start_button_text.get_rect(center=(self.screen_width//2, self.screen_height//2))
        self.quit_button_text = self.font.render("Quit", True, (255, 255, 255))
        self.quit_button_rect = self.quit_button_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 100))
        self.dialog = _dialog
    def enter(self):
        print("Entering Start Menu state")

    def exit(self):
        print("Exiting Start Menu state")

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.start_button_text, self.start_button_rect)
        screen.blit(self.quit_button_text, self.quit_button_rect)
        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.next_state = "exit"

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.next_state = CharacterCreation(self.dialog())
                elif self.quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.next_state = "exit"