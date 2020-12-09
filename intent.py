class intent:

    def __init__(self):
        self.user_intents = None

    def set_intent(self, inten):
        self.user_intents = inten

    def get_intent(self):
        return self.user_intents

    def reset_intents(self):
        self.user_intents = None
