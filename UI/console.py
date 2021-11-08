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
    print("u.Undo")
    print("r.Redo")
    print("x.Iesire ")


def uiAdaugaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pretul: "))
        checkin = input("Checkin: ")

        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiStergeRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de sters ")
        rezultat = stergeRezervare(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificaRezervare(lista, undoList, redoList):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul nume: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Checkin: ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def uiSchimbareClasaDupaStringNume(lista, undoList, redoList):
    substringNume = input("Dati substringul numelui: ")
    clasa = "business"
    rezultat = schimbareClasaDupaStringNume(substringNume, clasa, lista)
    undoList.append(lista)
    redoList.clear()
    return rezultat


def uiIeftinireRezervare(lista, undoList, redoList):
    try:
        procentaj = int(input("Dati procentajul cu care se va face ieftinire: "))
        rezultat = ieftinireRezervare(procentaj, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiDterminarePretMaximClasa(lista, undoList, redoList):
    rezultat = determinarePretMaximClasa(lista)
    for clasa in rezultat:
        print("Clasa {} are pretul maxim de {}".format(clasa, rezultat[clasa]))
    undoList.clear()
    redoList.clear()


def uiOrdonareDescrescatorDupaPret(lista, undoList, redoList):
    rezultat = ordonareDescrescatorDupaPret(lista)
    undoList.append(lista)
    redoList.clear()
    showAll(rezultat)


def uiSumaPreturiPerNume(lista, undoList, redoList):
    rezultat = sumaPreturiPerNume(lista)
    for nume in rezultat:
        print("Numele {} are suma preturilor {}".format(nume, rezultat[nume]))
    undoList.clear()
    redoList.clear()


def runMenu(lista):
    undoList = []
    redoList = []
    while True:
        printMenu()
        optiune = input("Alegeti o optiune: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiSchimbareClasaDupaStringNume(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiIeftinireRezervare(lista, undoList, redoList)
        elif optiune == "6":
            uiDterminarePretMaximClasa(lista, undoList, redoList)
        elif optiune == "7":
            uiOrdonareDescrescatorDupaPret(lista, undoList, redoList)
        elif optiune == "8":
            uiSumaPreturiPerNume(lista, undoList, redoList)
        elif optiune == "u":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
                showAll(lista)
            else:
                print("Nu se poate face undo")
        elif optiune == "r":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
                showAll(lista)
            else:
                print("Nu se poate face redo")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati ")
