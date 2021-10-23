from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitati import schimbareClasaDupaStringNume


def printMenu():
    print("1.Adauga rezervare ")
    print("2.Sterge rezervare ")
    print("3.Modifica rezervare ")
    print("4.Trecerea rezervarilor la o clasa superioara dupa un Nume dat")
    print("a.Afiseaza toate rezervarile ")
    print("x.Iesire ")


def uiAdaugaRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin = input("Checkin: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)

def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters ")
    return stergeRezervare(id, lista)

def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Checkin: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)

def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def uiSchimbareClasaDupaStringNume(lista):
    substringNume = input("Dati substringul numelui: ")
    clasa = "business"
    return schimbareClasaDupaStringNume(substringNume, clasa, lista)

def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiSchimbareClasaDupaStringNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati ")

