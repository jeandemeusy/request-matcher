class Skill():
    def __init__(self, name, weight=1):
        self.name = name.lower()
        self.weight = weight

    def __repr__(self):
        return f"{self.name} ({self.weight:.2f})"

    def __lt__(self, other):
        return self.weight < other.weight
