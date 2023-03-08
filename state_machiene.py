import pygame


class StateMachiene:
    def __init__(self):
        self.current_state = None
        self.next_state = None
    
    def update(self):
        #self.current_state.update()
        pass

    
    def switch_state(self,state):
        # self.current_state.exit()
        self.current_state = state
        # self.current_state.enter()



class State:
    def __init__(self):
        pass

    def enter(self):
        pass

    def update(self):
        pass

    def exit(self):
        pass

class Story(State):
    def __init__(self):
        super().__init__()
        self.next_button = Button((700, 500, 80, 40), OptionQuestion())
    
    def update(self, screen):
        # Draw the dialog box
        pygame.draw.rect(screen, (255, 255, 255), (50, 50, 700, 400))
        
        # Draw the text
        font = pygame.font.SysFont("Arial", 20)
        text_surface = font.render("This is the story text.", True, (0, 0, 0))
        screen.blit(text_surface, (100, 100))
        
        # Draw the button
        self.next_button.draw(screen)

class variableQuestion(State):
    #render a dialog box, and an input box 
    pass

class OptionQuestion(State):
    #render a dialog box, and series of buttons for the user to select from.
    pass

