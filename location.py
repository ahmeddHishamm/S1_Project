from db_handler import DB_handler
class location:
    # class variable:
    location_DB = DB_handler("DB/intents_Locations.json")

    def __init__(self, name=None, tag=None):
        self.place = name
        self.tag = tag
        if tag == "service":
            self.service = tag
        elif tag == "location":
            self.location = tag

    def get_first_key(self):
        print("please enter what place do you want to ask about: ")
        self.place = input(">").strip().upper()

    def get_second_key(self):
        print("please enter whether you need the 'location' or the 'service' of " + self.place)
        self.tag = input(">").strip()

    def _set_location(self, loc):
        self.location = loc

    def _set_service(self, serv):
        self.service = serv

    def search_db(self):
        found = False
        while not found:
            for item in location.location_DB.memory:
                if item.get(self.place, None):
                    self._set_location(item.get(self.place))
                    self._set_service(item.get("service"))
                    found = True
                    break
            if not found:
                self.get_first_key()

    def get_location(self):
        return self.location

    def get_service(self):
        return self.service

    def respond(self):
        self.search_db()
        while True:
            if self.tag == "service":
                return self.get_service()
            if self.tag == "location":
                return self.get_location()
            self.get_second_key()

# ================== driver code =============
#
# find_me = location("LIBRARY","")
# print(find_me.respond())
