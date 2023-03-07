import json

class DialogManager:
    def __init__(self, dialog_path):
        self.dialog_tree = {}
        self.current_node = None
        self.answers = {}
        self.load_dialog(dialog_path)

    def load_dialog(self, dialog_path):
        with open(dialog_path, 'r') as f:
            self.dialog_tree = json.load(f)
        self.current_node = self.dialog_tree['root']

    def show_dialog(self):
        print(self.current_node['dialogue'])

    def ask_question(self):
        print(self.current_node['question'])
        for i, option in enumerate(self.current_node['options']):
            print(f"{i+1}. {option}")
        choice = input("Enter your choice (1-{0}): ".format(len(self.current_node['options'])))
        if choice.isdigit() and 1 <= int(choice) <= len(self.current_node['options']):
            self.answers[self.current_node['variable']] = self.current_node['options'][int(choice)-1]
            self.current_node = self.dialog_tree[self.current_node['children'][int(choice)-1]]

    def step(self):
        if self.current_node['type'] == 'dialogue':
            self.show_dialog()
            self.current_node = self.dialog_tree[self.current_node['children'][0]]
        elif self.current_node['type'] == 'question':
            self.ask_question()

    def reset(self):
        self.answers = {}
        self.current_node = self.dialog_tree['root']