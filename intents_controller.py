from intent import intent
from location import location
from greeting import Greeting
from db_handler import DB_handler
from funcs import search2


class intents_controller:
    basic_intents = DB_handler("DB/intents_values.json")

    def __init__(self):
        self.entity_intent = intent()
        self.clean_text = None

    def search_intent(self):
        # searching algorithm in the database
        for word in self.clean_text:
            for dic in intents_controller.basic_intents.memory:
                if search2(word, dic["ways"]):
                    return dic["key"]
        return "not intent"

    def find_intent_from_text(self, clean_txt):
        self.clean_text = clean_txt
        found_intent = self.search_intent()
        self.entity_intent.set_intent(found_intent)

    def get_intent(self):
        return self.entity_intent.get_intent()

    def respond(self):
        # this function is responsible for responding to the user's intent
        if self.get_intent() == "greeting":  # working
            return Greeting().respond()
        if self.get_intent() == "location":
            print("what location do want to reach: ")
            loca = input(">").upper().strip()
            loc_obj = location(loca, "location")
            return loc_obj.respond()
        if self.get_intent() == "service":
            print("what place do you want to know what its services are: ")
            loca = input(">").upper().strip()
            loc_obj = location(loca, "service")
            return loc_obj.respond()
        if self.get_intent() == "not intent":
            return "sorry sir I didn't get what you want"  # way to restart the program
        if self.get_intent() == "quit":
            return ""
        else:
            loc_obj = location(self.get_intent())
            return loc_obj.respond()


# --------------------- driver code ----------
# intent_ctrl = intents_controller()
# l = input(">").split()
# intent_ctrl.find_intent_from_text(l)
# print(intent_ctrl.respond())
