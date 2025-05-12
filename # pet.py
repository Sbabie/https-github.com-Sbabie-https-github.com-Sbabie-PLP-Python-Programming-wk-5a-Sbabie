# pet.py
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        if self.hunger > 0:
            self.hunger -= 3
            self.happiness += 1
        else:
            print(f"{self.name} is not hungry.")

    def sleep(self):
        if self.energy < 10:
            self.energy += 5
        else:
            print(f"{self.name} is fully rested.")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness += 2
            self.hunger += 1
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
