from Domain.rezervare import creeazaRezervare, toString
from Logic.CRUD import stergeRezervare, adaugaRezervare


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def meniu():
    print("add, id, nume, clasa, pret, checkin")
    print("delete, id")
    print("showall")
    print("vezi comenzile")


def command(lista):
    lista = []
    while True:
        optiune = input("Dati comenzile: ")
        if optiune == "vezi comenzile":
            meniu()
        else:
            cuvinte = optiune.split(";")
            if cuvinte[0] == "iesire":
                break
            else:
                for rezervare in cuvinte:
                    cuvant = rezervare.split(",")
                    if cuvant[0] =="add":
                        try:
                            lista = adaugaRezervare(cuvant[1], cuvant[2],cuvant[3],cuvant[4], lista)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return lista
                    elif cuvant[0] == "delete":
                        lista = stergeRezervare(cuvant[0], lista)
                    elif cuvant[0] == "showall":
                        showAll(lista)
                    else:
                        print("Comanda gresita! Reincercati")


def run_menu():
    lista = []
    lista = adaugaRezervare("2", "Andrei", "economy plus", 180, "da", lista)
    command(lista)

run_menu()
