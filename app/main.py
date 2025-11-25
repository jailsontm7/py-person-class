class Person:
    # 1. Atributo de classe para armazenar todas as instâncias
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

        # 2. Adiciona a nova instância ao dicionário de classe
        self.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:
    # Passo 1: Limpar o dicionário de classe para garantir isolamento
    Person.people = {}

    person_instances: list[Person] = []

    # 3. Criar todas as instâncias de Person
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        # A chamada ao __init__ preenche automaticamente Person.people
        instance = Person(name, age)
        person_instances.append(instance)

    for person_data in people:
        current_person = Person.people[person_data["name"]]

        spouse_name = None
        if "wife" in person_data:
            spouse_name = person_data["wife"]
            spouse_key = "wife"
        elif "husband" in person_data:
            spouse_name = person_data["husband"]
            spouse_key = "husband"
        else:
            # Não há relacionamento de cônjuge a ser definido
            continue

        # 4. Adicionar o atributo wife/husband se o valor não for None
        if spouse_name is not None:
            # Encontra a instância do cônjuge no dicionário de classe
            spouse_instance = Person.people[spouse_name]

            # Adiciona o atributo dinamicamente (wife ou husband)
            setattr(current_person, spouse_key, spouse_instance)

    return person_instances
