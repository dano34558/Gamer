import os
import pygame
from ..State import State

pygame.init()

class Load(State):
    def __init__(self):
        super().__init__()

        self.screen_width = 800
        self.screen_height = 600

        self.font = pygame.font.Font(None, 24)

        self.title_text = self.font.render("Load Game", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(self.screen_width//2, self.screen_height//2 - 100))

        self.back_text = self.font.render("Back", True, (255, 255, 255))
        self.back_rect = self.back_text.get_rect(center=(self.screen_width//2, self.screen_height - 50))

        self.saved_games = self.get_saved_games()
        self.saved_games_texts = []
        for i, saved_game in enumerate(self.saved_games):
            text = self.font.render(saved_game, True, (255, 255, 255))
            rect = text.get_rect(center=(self.screen_width//2, self.screen_height//2 + i*50))
            self.saved_games_texts.append((text, rect))

    def enter(self):
        print("Entering Load state")

    def exit(self):
        print("Exiting Load state")

    def update(self):
        self.handle_events()

    def render(self, screen):
        screen.fill((0, 0, 0))

        screen.blit(self.title_text, self.title_rect)

        if self.saved_games:
            for text, rect in self.saved_games_texts:
                screen.blit(text, rect)
        else:
            no_saved_games_text = self.font.render("No saved games.", True, (255, 255, 255))
            no_saved_games_rect = no_saved_games_text.get_rect(center=(self.screen_width//2, self.screen_height//2))
            screen.blit(no_saved_games_text, no_saved_games_rect)

        screen.blit(self.back_text, self.back_rect)

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
                if self.back_rect.collidepoint(pygame.mouse.get_pos()):
                    self.next_state = "start"

                for i, (_, rect) in enumerate(self.saved_games_texts):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        print(f"Loading saved game: {self.saved_games[i]}")
                        # load saved game code here

    def get_saved_games(self):
        saved_games = []
        for file_name in os.listdir("C:/users/dano3/Desktop/Gamer/saved_games.txt"):
            if file_name.endswith(".txt"):
                saved_games.append(file_name[:-4])
        return saved_games