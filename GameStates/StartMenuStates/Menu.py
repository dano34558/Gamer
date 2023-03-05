import pygame
from ..State import State
from ..StartMenuStates.NewGame import NewGame
from ..StartMenuStates.LoadGame import Load

class Menu(State):
    def __init__(self):
        super().__init__()

        self.screen_width = 800
        self.screen_height = 600

        self.font = pygame.font.Font(None, 24)

        self.title_text = self.font.render("My Game", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 100))

        self.new_game_text = self.font.render("New Game", True, (255, 255, 255))
        self.new_game_rect = self.new_game_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 50))

        self.load_game_text = self.font.render("Load Game", True, (255, 255, 255))
        self.load_game_rect = self.load_game_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 100))

        self.settings_text = self.font.render("Settings", True, (255, 255, 255))
        self.settings_rect = self.settings_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 150))

        self.quit_text = self.font.render("Quit Game", True, (255, 255, 255))
        self.quit_rect = self.quit_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 200))

    def enter(self):
        print("Entering start menu state")

    def exit(self):
        print("Exiting start menu state")

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.new_game_text, self.new_game_rect)
        screen.blit(self.load_game_text, self.load_game_rect)
        screen.blit(self.settings_text, self.settings_rect)
        screen.blit(self.quit_text, self.quit_rect)

        pygame.display.flip()

    def handle_events(self):
        
        for event in pygame.event.get():
            print("t")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.new_game_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Starting new game!")
                    self.next_state = NewGame()
                elif self.load_game_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Loading saved games!")
                    self.next_state = Load()
                elif self.settings_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Opening settings!")
                    self.next_state = Menu()
                elif self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()