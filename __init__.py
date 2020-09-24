from mycroft import MycroftSkill, intent_file_handler
from time import sleep


class Todotxt(MycroftSkill):
    file_path = None
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.file_path = self.settings.get('todo_file', '/home/ares/Nextcloud/todo/todo.txt')

    @intent_file_handler('todotxt.intent')
    def handle_todotxt(self, message):
        file = open(self.file_path, 'r')
        relevant_lines = []
        for line in file:
            if "(A)" in line and not line.startswith('x'):
                relevant_lines.append(line)
        self.speak_dialog('todotxt')
        for line in relevant_lines:
            output = line.split()
            output = [word for word in output if not word.startswith('+') and not word.startswith('@') and word != "(A)"]
            output_line = ' '.join(output)
            self.speak(output_line)
            sleep(2)
        file.close()

    @intent_file_handler('add.to.list.intent')
    def handle_add_to_todo_intent(self, message):
        file = open(self.file_path, 'a')
        item_to_add = message.data.get('item')
        full_item = item_to_add + " @from_mycroft"
        file.write(full_item)
        file.write("\n")
        file.close()
        self.speak("Adding %s to your to do list" % item_to_add)

def stop(self):
    pass

def create_skill():
    return Todotxt()
