import json


class DB_handler:
    def __init__(self, js):
        with open(js) as db:
            self.memory = json.load(db)

    def print_memory(self):
        print(self.memory)
