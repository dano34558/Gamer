import State
import pygame

class StartMenuState(State):
    def __init__(self):
        super().__init__()

        self.screen_width = 800
        self.screen_height = 600

        self.font = pygame.font.Font(None, 24)

        self.title_text = self.font.render("My Game", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 100))

        self.start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.start_rect = self.start_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 50))

        self.quit_text = self.font.render("Quit Game", True, (255, 255, 255))
        self.quit_rect = self.quit_text.get_rect(center=(self.screen_width//2, self.screen_height//2 + 100))

    def enter(self):
        print("Entering start menu state")

    def exit(self):
        print("Exiting start menu state")

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(self.title_text, self.title_rect)
        screen.blit(self.start_text, self.start_rect)
        screen.blit(self.quit_text, self.quit_rect)

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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_rect.collidepoint(pygame.mouse.get_pos()):
                    print("Start game!")
                    self.next_state = "new_game"
                elif self.quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    quit()