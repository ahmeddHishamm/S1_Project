from db_handler import DB_handler
from greeting import Greeting
from intents_controller import intents_controller
from intent import intent
from location import location
from login_controller import login_controller
from textprocess import text_processing
from terminal import terminal

# =================== Driver code for the whole chatbot ===============
# 1: check the name and ID of the student

user = login_controller()
found = False
while not found:
    found = user.search(terminal("name").get_txt, terminal("id").get_txt)
    print("hello ", user.Name)
txt = text_processing(" ")
print("I am TKH chatbot, I am here to help you navigate through our beloved uni's campus")
while txt.get_text != "quit":
    intent_ctrl = intents_controller()
    txt = text_processing(terminal("> ").get_txt)
    txt.clean_text
    intent_ctrl.find_intent_from_text(txt.get_text)
    if intent_ctrl.respond() == "":
        break
    print(intent_ctrl.respond())
print("it was a pleasure talking to you sir")
