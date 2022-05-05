import json


class Persona:
    def __init__(self, name, last_name, age, email):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email

    def set_name(self, name):
        self.__name = name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_age(self, age):
        self.__age = age

    def set_email(self, email):
        self.__email = email

    def to_json(self):
        return {
            "name": self.__name,
            "last_name": self.__last_name,
            "age": self.__age,
            "email": self.__email
        }

    def __str__(self):
        return "Nombre: {}\nApellido: {}\nEdad: {}\nEmail: {}".format(self.__name, self.__last_name, self.__age,
                                                                      self.__email)


def save_json(personas):
    with open('./personas/personas.json', 'w') as file:
        json.dump(personas, file, indent=4)


def load_json():
    try:
        with open('./personas/personas.json', 'r') as file:
            obj = json.load(file)
            return obj
    # If json file doesn't exist or is empty
    except Exception as e:
        return []


def email_exists(email):
    personas = load_json()
    for persona in personas:
        persona = Persona(**persona)
        if persona.get_email() == email:
            return True
    return False


def create_persona(name, last_name, age, email):
    try:
        if email_exists(email):
            return False
        persona = Persona(name, last_name, age, email)
        personas = load_json()
        personas.append(persona.to_json())
        save_json(personas)
        return True
    except Exception:
        return False


def edit_persona(name, last_name, age, email):
    try:
        personas = load_json()
        for persona in personas:
            persona = Persona(**persona)
            if persona.get_email() == email:
                persona.set_name(name)
                persona.set_last_name(last_name)
                persona.set_age(age)
                save_json(personas)
                return True
        return False
    except Exception:
        return False


def delete_persona(email):
    try:
        personas = load_json()
        for persona in personas:
            persona = Persona(**persona)
            if persona.get_email() == email:
                personas.remove(persona.to_json())
                save_json(personas)
                return True
        return False
    except Exception:
        return False


def show_persona(email):
    personas = load_json()
    for persona in personas:
        persona = Persona(**persona)
        if persona.get_email() == email:
            return persona
    return None


def show_all_personas():
    personas = load_json()
    for persona in personas:
        persona = Persona(**persona)
        print("----------------------------------------------------")
        print(persona)
