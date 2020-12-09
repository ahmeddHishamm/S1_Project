import json


class DB_handler:
    def __init__(self, js):
        with open(js) as db:
            self.memory = json.load(db)
        self.db = js
    def print_memory(self):
        print(self.memory)

    def update_memory(self):
        with open(self.db, "w") as js:
            if self.memory != json.load(js)
            json.dump(self.memory,js)
