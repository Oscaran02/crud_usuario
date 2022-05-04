import os

import controller

from colorama import init, Fore


# To clear the screen
def clear():
    # If the OS is Windows
    if os.name == "nt":
        os.system("cls")
    # If the OS is Linux or Mac
    else:
        os.system("clear")


# To change the menu screen
def changing_screen():
    input(Fore.MAGENTA+"Presione enter para continuar...")
    clear()


# Main program
if __name__ == "__main__":
    init(autoreset=True)  # To reset the colors after each print
    option = 0
    clear()

    # Show the menu
    while option != 6:
        print(Fore.GREEN+"Bienvenido, digite el número de la acción que desea realizar: ")
        print(Fore.BLUE+"1. Crear persona")
        print(Fore.BLUE+"2. Editar persona")
        print(Fore.BLUE+"3. Eliminar persona")
        print(Fore.BLUE+"4. Mostrar una persona")
        print(Fore.BLUE+"5. Mostrar todas las personas")
        print(Fore.YELLOW+"6. Salir")
        try:
            option = int(input(Fore.GREEN+">>>Opción: "))

            # If the option is not between 1 and 6, the program will ask again
            if option < 1 or option > 6:
                print(Fore.RED+"Ingrese un número valido")
            else:
                clear()

            # Create a new person
            if option == 1:
                print("<<< Crear persona >>>")
                name = input("Nombre: ")
                last_name = input("Apellido: ")
                age = input("Edad: ")
                email = input("Email: ")
                if controller.create_persona(name, last_name, age, email):
                    print(Fore.GREEN+"Persona creada")
                else:
                    print(Fore.RED + "No se pudo crear la persona")

            # Edit a person
            elif option == 2:
                print("<<< Editar persona >>>")
                email = input("Ingrese el email de a persona a editar: ")
                print("<<< Datos a editar >>>")
                name = input("Nombre: ")
                last_name = input("Apellido: ")
                age = input("Edad: ")
                if controller.edit_persona(name, last_name, age, email):
                    print(Fore.GREEN+"Persona editada")
                else:
                    print(Fore.RED+"No se pudo editar la persona")

            # Delete a person
            elif option == 3:
                print("<<< Eliminar persona >>>")
                email = input("Ingrese el email: ")
                if controller.delete_persona(email):
                    print(Fore.GREEN+"Persona eliminada")
                else:
                    print(Fore.RED + "No se pudo eliminar la persona")

            # Show a person
            elif option == 4:
                print("<<< Mostrar una persona >>>")
                email = input("Ingrese el email de la persona: ")
                if controller.show_persona(email) is not None:
                    print("---- Persona ----")
                    print(controller.show_persona(email))
                else:
                    print(Fore.RED + "No existe una persona con ese email")

            # Show all people
            elif option == 5:
                print("<<< Mostrar todas las personas >>>")
                controller.show_all_personas()

            # Exit the program
            elif option == 6:
                print(Fore.YELLOW+"<<< Salir >>>")
                print(Fore.YELLOW+"Saliendo...")

        # If the user does not enter a number, the program will ask again
        except ValueError:
            print(Fore.RED+"Ingrese un número, las letras no son validas")
        finally:
            changing_screen()
