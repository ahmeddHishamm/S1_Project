from db_handler import DB_handler


class login_controller:
    # class variable:
    user_info = DB_handler("DB/intents_info.json")

    def __init__(self):
        self.Name = None
        self.ID = None

    def set_info(self, nm, id_num):
        self.Name = nm
        self.ID = id_num

    def search(self, name, id_num):
        if id_num == login_controller.user_info.memory.get(f"{name}"):
            self.set_info(name, id_num)
            return True
        else:
            return False


# ======================= driver code ================
# user = login_controller()
# print(user.Name, user.ID)
# while not user.Name:
#     user.search(input("name>>"), input("ID:"))
#     print(user.Name, user.ID)
