from Domain.rezervare import getClasa
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitati import schimbareClasaDupaStringNume


def testSchimbareClasa():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus ", 180, "da", lista)
    lista = adaugaRezervare("3", "Andreea", "business", 249.9, "nu", lista)

    lista = schimbareClasaDupaStringNume("And", "business", lista)

    assert getClasa(getById("1", lista)) == "economy"
    assert getClasa(getById("2", lista)) == "business"
    assert getClasa(getById("3", lista)) == "business"