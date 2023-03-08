import json
import pygame
import pygame.freetype
import sys

class DialogManager:
    def __init__(self):
        self.current_path = None
        self.dialog_tree = None
        self.dialog_font = pygame.freetype.SysFont('Arial', 24)
        self.input_font = pygame.freetype.SysFont('Arial', 20)
        self.input_box = pygame.Rect(0, 0, 300, 32)
        self.input_box.center = (400, 400)
        self.input_text = ''
        
    def load_scene(self, path):
        with open(path) as f:
            self.dialog_tree = json.load(f)
        self.current_path = 'root'

    def question(self, node, screen):
       if node['input']:
           return self.variable_question(node, screen)
       else:
           return self.option_question(node, screen)
    
    def option_question(self, node, screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    # check if the user clicked on an option button
                    for i, option in enumerate(node['options']):
                        if option['text_rect'].collidepoint(event.pos):
                            return option['text']
            
            screen.fill((255, 255, 255))
            
            text_surf, _ = self.dialog_font.render(node['text'], (0, 0, 0))
            text_rect = text_surf.get_rect(center=(400, 200))
            screen.blit(text_surf, text_rect)
            
            for i, option in enumerate(node['options']):
                option_surf, _ = self.input_font.render(option['text'], (0, 0, 0))
                option_rect = option_surf.get_rect(center=(400, 250 + i * 50))
                option['text_rect'] = option_rect
                pygame.draw.rect(screen, (255, 255, 255), option_rect)
                pygame.draw.rect(screen, (0, 0, 0), option_rect, 2)
                screen.blit(option_surf, option_rect)
        
            pygame.display.flip()
        
    def variable_question(self, node, screen):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # return the user's input as the answer
                        answer = self.input_text
                        self.input_text = ''
                        return answer
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode
        
            screen.fill((255, 255, 255))
            
            text_surf, _ = self.dialog_font.render(node['text'], (0, 0, 0))
            text_rect = text_surf.get_rect(center=(400, 200))
            screen.blit(text_surf, text_rect)
            
            pygame.draw.rect(screen, (0, 0, 0), self.input_box, 2)
            input_surf, _ = self.input_font.render(self.input_text, (0, 0, 0))
            input_rect = input_surf.get_rect(center=self.input_box.center)
            screen.blit(input_surf, input_rect)
            
            pygame.display.flip()
        
    def story(self, node, screen):
        text_surf, _ = self.dialog_font.render(node['text'], (0, 0, 0))
        text_rect = text_surf.get_rect(center=(400, 200))
        screen.blit(text_surf, text_rect)
        pygame.display.flip()
        pygame.time.wait(1000)
        
    def step(self, answer):
        node = self.dialog_tree[self.current_path]
        for option in node['options']:
            if option['text'].lower() == answer.lower():
                self.current_path = option['path']
                return
        # if the user's answer doesn't match any of the options, go to the root
        self.go_to_root()
        
    def go_to_root(self):
        self.current_path = 'root'
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Dialog Manager Demo')
    clock = pygame.time.Clock()
    dialog_manager = DialogManager()
    dialog_manager.load_scene('dialog.json')
    
    while True:
        node = dialog_manager.dialog_tree[dialog_manager.current_path]
        if node['type'] == 'question':
            if node['input']:
                answer = dialog_manager.variable_question(node, screen)
            else:
                answer = dialog_manager.option_question(node, screen)
            dialog_manager.step(answer)
        elif node['type'] == 'story':
            dialog_manager.story(node, screen)
            break
        clock.tick(60)
    pygame.quit()
    
if __name__ == '__main__':
    main()