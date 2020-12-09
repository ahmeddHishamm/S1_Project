from random import choice


class Greeting:

    @staticmethod
    def respond():
        return choice(Greeting.responds_pool)

    # class variable
    responds_pool = ["Hello, I'm TKH chatbot and I am honored to meet you",
                     "nice to meet you mate", "I'm honored to meet you", "Good morning!", "Hello, hope you are doing well",
                     "happy to meet you"]