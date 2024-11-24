class Booster:
    def __init__(self, name):
        self.name = name
        self.ability = None     # function

    def __str__(self):
        return f"{self.name}"
    
    def set_ability(self, ability):
        self.ability = ability

    def use_ability(self):
        self.ability()

    def __repr__(self):
        return f"Booster(name={self.name}, ability={self.ability})"