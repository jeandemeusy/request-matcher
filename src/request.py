import uuid
from skill import Skill


class Request:
    def __init__(self, *argv):
        self.uuid = uuid.uuid1()
        self.skills = [Skill(w) for w in argv]

    @property
    def skills_names(self):
        return [s.name for s in self.skills]

    @property
    def skills_weights(self):
        return [s.weight for s in self.skills]

    def __repr__(self):
        return f"<{self.__class__.__name__} object: {self.skills}>"

    def __str__(self):
        return f"{self.skills}"
