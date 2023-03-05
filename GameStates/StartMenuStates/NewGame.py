import pygame
from ..State import State

pygame.init()

class NewGame(State):
    def __init__(self):
        super().__init__()

        self.screen_width = 800
        self.screen_height = 600

        self.font = pygame.font.Font(None, 24)

        self.title_text = self.font.render("Character Creation", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 200))

        self.name_text = self.font.render("Name:", True, (255, 255, 255))
        self.name_rect = self.name_text.get_rect(center=(self.screen_width//2 - 100, self.screen_height//2))

        self.name_input_rect = pygame.Rect(self.screen_width//2, self.screen_height//2 - 10, 140, 30)
        self.name_input_active = False
        self.name_input_text = ""

        self.create_button_text = self.font.render("Create", True, (255, 255, 255))
        self.create_button_rect = self.create_button_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 100))

    def enter(self):
        print("Entering New Game state")

    def exit(self):
        print("Exiting New Game state")
        

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.name_text, self.name_rect)

        # Render name input box
        name_input_surf = self.font.render(self.name_input_text, True, (255, 255, 255))
        pygame.draw.rect(screen, (255, 255, 255), self.name_input_rect, 2)
        screen.blit(name_input_surf, (self.name_input_rect.x + 5, self.name_input_rect.y + 5))

        screen.blit(self.create_button_text, self.create_button_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_RETURN:
                    if self.name_input_active:
                        self.name_input_active = False
                        print(f"Creating new character with name: {self.name_input_text}")
                        self.next_state = "gameplay"
                elif event.key == pygame.K_BACKSPACE:
                    self.name_input_text = self.name_input_text[:-1]
                else:
                    if self.name_input_active:
                        self.name_input_text += event.unicode

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.create_button_rect.collidepoint(pygame.mouse.get_pos()):
                    print(f"Creating new character with name: {self.name_input_text}")
                    self.next_state = "gameplay"
                elif self.name_input_rect.collidepoint(pygame.mouse.get_pos()):
                    self.name_input_active = True
                else:
                    self.name_input_active = False
