# app/main.py
from __future__ import annotations


class Person:
    people: dict[str, Person] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}

    person_instances: list[Person] = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        current = Person.people[person_data["name"]]

        for spouse_key in ("wife", "husband"):
            if spouse_key not in person_data:
                continue

            spouse_name = person_data[spouse_key]
            if spouse_name is None:
                continue

            if spouse_name not in Person.people:
                continue

            spouse = Person.people[spouse_name]
            setattr(current, spouse_key, spouse)

    return person_instances
