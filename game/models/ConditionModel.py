class Condition:

    def __init__(self, win_condition):
        self.win_condition = win_condition
        self.conditions = []

    def add_condition(self, condition):
        self.conditions.append(condition)

    # def __str__(self):
    #     return self.condition_name

    # def __repr__(self):
    #     return self.condition_name

    # def __eq__(self, other):
    #     return self.condition_id == other.condition_id

    # def __hash__(self):
    #     return hash(self.condition_id)