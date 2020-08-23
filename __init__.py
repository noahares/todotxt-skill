from mycroft import MycroftSkill, intent_file_handler


class Todotxt(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('todotxt.intent')
    def handle_todotxt(self, message):
        self.speak_dialog('todotxt')


def create_skill():
    return Todotxt()

