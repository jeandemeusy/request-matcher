class Person:
    def __init__(self, name: str, skills: list):
        self.name = name
        self.skills = skills
        self.score = 0

    def get_score(self, request) -> int:
        """
        Match the person skills with the request. The number of requested skills that matches is returned.
        """

        weights = []
        for skill in request.skills:
            try:
                idx = self.skills_names.index(skill.name)
            except:
                weights.append(0)
            else:
                weights.append(self.skills[idx].weight)

        score = [a * b for a, b in zip(request.skills_weights, weights)]
        self.score = sum(score) / len(request.skills)

        return self.score

    @property
    def skills_names(self):
        return [s.name for s in self.skills]

    @property
    def skills_weights(self):
        return [s.weight for s in self.skills]

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} object: ({self.score:.2f}) {self.name}): {self.skills}>"

    def __str__(self) -> str:
        return f"({self.score:.2f}) {self.name}: {self.skills}"

    def __lt__(self, other) -> bool:
        return self.score < other.score
