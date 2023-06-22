class Woman:
    def __init__(self, name):
        self.name = name

class ITGuy:
    def __init__(self, name):
        self.name = name
        self.is_shy = True

    def try_to_express_interest(self, woman):
        if self.is_shy:
            print(f"{self.name} sees {woman.name}, he wants to express interest but he is shy and doesn't know how to interact with unfamiliar woman.")
        else:
            print(f"{self.name} confidently expresses interest in {woman.name}.")

woman = Woman("Olga")
it_guy = ITGuy("Josef")

it_guy.try_to_express_interest(woman)
