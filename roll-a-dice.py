# angeloaugusto; 20/11/2023; 10:29
import random

response = "y"

while response == "y":
    print("Jogando o dado...")
    numero = random.randint(1, 6)

    if numero == 1:
        print("-------")
        print("|     |")
        print("|  •  |")
        print("|     |")
        print("-------")
    elif numero == 2:
        print("-------")
        print("| •   |")
        print("|     |")
        print("|   • |")
        print("-------")
    elif numero == 3:
        print("-------")
        print("| •   |")
        print("|  •  |")
        print("|   • |")
        print("-------")
    elif numero == 4:
        print("-------")
        print("| • • |")
        print("|     |")
        print("| • • |")
        print("-------")
    elif numero == 5:
        print("-------")
        print("| • • |")
        print("|  •  |")
        print("| • • |")
        print("-------")
    else:
        print("-------")
        print("| • • |")
        print("| • • |")
        print("| • • |")
        print("-------")

    response = input("Deseja jogar novamente? (y/n): ")
    while response != "y" and response != "n":
        response = input("Por favor, digite 'y' para continuar ou 'n' para sair: ")

print("Obrigado por jogar!")