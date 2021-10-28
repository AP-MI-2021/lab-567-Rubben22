from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervare
from Logic.functionalitati import schimbareClasaDupaStringNume, ieftinireRezervare, determinarePretMaximClasa, \
    ordonareDescrescatorDupaPret, sumaPreturiPerNume


def printMenu():
    print("1.Adauga rezervare ")
    print("2.Sterge rezervare ")
    print("3.Modifica rezervare ")
    print("4.Trecerea rezervarilor la o clasa superioara dupa un Nume dat")
    print("5.Ieftinirea tuturor rezervărilor la care s-a făcut checkin cu un procentaj citit ")
    print("6.Determinarea pretului maxim pentru fiecare clasa ")
    print("7.Ordonarea rezervarilor descrescator dupa pret ")
    print("8.Afisare suma preturi pentru fiecare nume ")
    print("a.Afiseaza toate rezervarile ")
    print("x.Iesire ")


def uiAdaugaRezervare(lista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Checkin: ")
        return adaugaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de sters ")
        return stergeRezervare(id, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Checkin: ")
        return modificaRezervare(id, nume, clasa, pret, checkin, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiSchimbareClasaDupaStringNume(lista):
    substringNume = input("Dati substringul numelui: ")
    clasa = "business"
    return schimbareClasaDupaStringNume(substringNume, clasa, lista)


def uiIeftinireRezervare(lista):
    try:
        procentaj = int(input("Dati procentajul cu care se va face ieftinire: "))
        rezultat = ieftinireRezervare(procentaj, lista)
        showAll(rezultat)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDterminarePretMaximClasa(lista):
    rezultat = determinarePretMaximClasa(lista)
    for clasa in rezultat:
        print("Clasa {} are pretul maxim de {}".format(clasa, rezultat[clasa]))


def uiOrdonareDescrescatorDupaPret(lista):
    rezultat = ordonareDescrescatorDupaPret(lista)
    showAll(rezultat)


def uiSumaPreturiPerNume(lista):
    rezultat = sumaPreturiPerNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))


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
        elif optiune == "5":
            lista = uiIeftinireRezervare(lista)
        elif optiune == "6":
            uiDterminarePretMaximClasa(lista)
        elif optiune == "7":
            uiOrdonareDescrescatorDupaPret(lista)
        elif optiune == "8":
            uiSumaPreturiPerNume(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati ")
