from db_handler import DB_handler


class Tour:
    tours_intents = DB_handler("DB/intents_Tours.json")

    def __init__(self, tour_name):
        tour_idx = Tour.find_tour(tour_name)
        self.tour = Tour.tours_intents.memory[tour_idx]

    @staticmethod
    def find_tour(ID):
        for dictionary_idx in range(0, len(Tour.tours_intents.memory)):
            if Tour.tours_intents.memory[dictionary_idx]["TourID"] == ID:
                return dictionary_idx
        return False

    def __repr__(self):
        output = ""
        for k in self.tour:
            if k == "TourID":
                continue
            if k == "TourAvailability":
                if k:
                    output = output + f"{k}\tAvailable\n"
                else:
                    output = output + f"{k}\tNot available\n"
                continue
            output = output + f"{k}\t\t\t{self.tour[k]}\n"
        return output
