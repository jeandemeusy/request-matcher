from request import Request
from person import Person
from skill import Skill

from names import get_full_name as name
from random import sample, randint, uniform

import json
import sys


def find_best_candidate(people, request, num=1):
    """
    Matchs people and requested skills, then returns the top [num] people.
    """

   # compare request to people skills
    for p in people:
        p.get_score(request)

    # sort people by score
    people.sort(reverse=True)

    return people[:num]


def generate_data(path, num=25):
    """
    Generates random request and [num] people based on json file at [path].
    """
    # get list of possible skills
    with open(path) as f:
        json_data = json.load(f)

    words = set(json_data["words"])

    # create request (similar to the word list from an email)
    request = Request(*sample(words, randint(3, 4)))

    # create random people, and a known one with given skills
    people = []
    for _ in range(num):
        sublist = sample(words, randint(3, 6))

        person_skills = [Skill(s, uniform(.75, 1.)) for s in sublist]

        people.append(Person(name(), person_skills))

    return people, request


def static_data():
    """
    Returns pre-generated data. Each time the data returned is the same.
    """

    request = Request("fortran", "sql", "word", "github")

    people = [
        Person("Raymond Harris", [
            Skill("latex", 0.76),
            Skill("kotlin", 0.77),
            Skill("powerpoint", 1.00),
            Skill("ios", 0.58),
            Skill("linux", 0.56)
        ]),
        Person("Robert Willis", [
            Skill("macos", 0.99),
            Skill("swift", 0.74),
            Skill("vi", 0.62),
            Skill("adobe", 0.68)
        ]),
        Person("Marta Jordon", [
            Skill("swift", .56),
            Skill("data vis.", 0.72),
            Skill("versionning", 0.84),
            Skill("raspberry pi", 0.93)
        ]),
        Person("Genevieve Keaney", [
            Skill("powerpoint", 0.61),
            Skill("github", 0.84),
            Skill("c++", 0.93)
        ]),
        Person("Christopher Sanders", [
            Skill("word", 0.91),
            Skill("c++", 0.54),
            Skill("linux", 0.52),
            Skill("sql", 0.76),
            Skill("big data", 0.68)
        ])
    ]

    return people, request


if __name__ == "__main__":
    """
    execution:
    python src/main.py [-auto] 
    """

    opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]

    if "-auto" in opts:
        people, request = generate_data('assets/data.json', 5)
    else:
        people, request = static_data()

    candidate = find_best_candidate(people, request, 1)

    for c in candidate:
        print(c)
