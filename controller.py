import model

from validate_email import validate_email


# check if email is valid
def validating_email(email):
    return validate_email(email)


# check if age is valid
def validating_age(age):
    if age.isdigit():
        if 100 > int(age) > 0:
            return True
    else:
        return False


# Create and validate a new person
def create_persona(name, last_name, age, email):
    if validating_email(email):
        if validating_age(age):
            if model.create_persona(name, last_name, age, email):
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# Edit and validate a person
def edit_persona(name, last_name, age, email):
    if validating_age(age):
        if model.edit_persona(name, last_name, age, email):
            return True
        else:
            return False


# Delete a person
def delete_persona(email):
    if model.delete_persona(email):
        return True
    else:
        return False


# Show a person
def show_persona(email):
    return model.show_persona(email)


# Show all people
def show_all_personas():
    model.show_all_personas()
