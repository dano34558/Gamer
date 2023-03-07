from .State import State




class CharacterCreation(State):
    def __init__(self,_dialog):
        super().__init__()
        self.dialog_manager = _dialog('Story/character_creation.json')

    def enter(self):
        print("Entering Character Creation state")
        self.dialog_manager.start_dialog()

    def exit(self):
        print("Exiting Character Creation state")

    def update(self):
        if self.dialog_manager.current_node['type'] == 'question':
            self.handle_question()
        elif self.dialog_manager.current_node['type'] == 'dialog':
            self.handle_dialog()
        else:
            pass

    def render(self, screen):
        pass

    def handle_question(self):
        question_text = self.dialog_manager.current_node['text']
        options = self.dialog_manager.current_node.get('options')
        variable = self.dialog_manager.current_node.get('variable')
        answer = self.dialog_manager.ask_question(question_text, options)
        if variable:
            self.dialog_manager.store_answer(variable, answer)

    def handle_dialog(self):
        dialog_text = self.dialog_manager.current_node['text']
        self.dialog_manager.show_dialog(dialog_text)