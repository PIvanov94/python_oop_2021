class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        result = self.people + other.people
        return Group(self.name, result)

    def __str__(self):
        return f"Group {self.name} with members {', '.join(list(map(str, self.people)))}"

    def __getitem__(self, item):
        return f"Person {item}: {self.people[item].__str__()}"
