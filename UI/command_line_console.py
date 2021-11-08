from Domain.rezervare import toString
from Logic.CRUD import stergeRezervare, adaugaRezervare


def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))

def meniu():
    print("add, id, nume, clasa, pret, checkin")
    print("delete, id")
    print("showall")
    print("iesire")

def uiAdaugaRezervare2(lista, listacuvinte):
    try:
        id = listacuvinte[0]
        nume = listacuvinte[1]
        clasa = listacuvinte[2]
        pret = listacuvinte[3]
        checkin = listacuvinte[4]
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiStergeRezervare2(id, lista):
    try:
        rezultat = stergeRezervare(id, lista)
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def command(listaNoua):
    listacuvinte = []
    while True:
        optiune = input("Dati comenzile: ")
        if optiune == "ajutor":
            meniu()
        else:
            cuvinte = optiune.split(";")
            if cuvinte[0] == "iesire":
                break
            else:
                print(cuvinte)
                for rezervare in cuvinte:
                    cuvant = rezervare.split(",")
                    if cuvant[0] == "add":
                        id = cuvant[1]
                        nume = cuvant[2]
                        clasa = cuvant[3]
                        pret = float(cuvant[4])
                        checkin = cuvant[5]
                        listacuvinte = [id, nume, clasa, pret, checkin]
                        listaNoua = uiAdaugaRezervare2(listaNoua, listacuvinte)
                    elif cuvant[0] == 'delete':
                        try:
                            id = cuvant[1]
                            listaNoua= uiStergeRezervare2(id, listaNoua)
                        except ValueError as ve:
                            print("Eroare: {}".format(ve))
                            return listaNoua
                    elif cuvant[0] == 'showall':
                        showAll(listaNoua)
                    else:
                        print("Comanda gresita! Reincercati sau tastati 'ajutor' pentru a vedea comenzile")


def run_menu():
    lista = []
    command(lista)

run_menu()
