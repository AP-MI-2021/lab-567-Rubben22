from Domain.rezervare import getClasa, getPret, getId
from Logic.CRUD import adaugaRezervare, getById
from Logic.functionalitati import schimbareClasaDupaStringNume, ieftinireRezervare, determinarePretMaximClasa, \
    ordonareDescrescatorDupaPret, sumaPreturiPerNume


def testSchimbareClasa():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus ", 180, "da", lista)
    lista = adaugaRezervare("3", "Andreea", "business", 249.9, "nu", lista)

    lista = schimbareClasaDupaStringNume("And", "business", lista)

    assert getClasa(getById("1", lista)) == "economy"
    assert getClasa(getById("2", lista)) == "business"
    assert getClasa(getById("3", lista)) == "business"


def testIeftinireRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus ", 180, "nu", lista)

    lista = ieftinireRezervare(10, lista)
    assert getPret(getById("1", lista)) == 90
    assert getPret(getById("2", lista)) == 180


def testDeterminarePretMaximClasa():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus", 180, "nu", lista)
    lista = adaugaRezervare("3", "George", "economy", 110, "nu", lista)

    rezultat = determinarePretMaximClasa(lista)

    assert len(rezultat) == 2
    assert rezultat["economy"] == 110
    assert rezultat["economy plus"] == 180


def testOrdonareDescrescatorDupaPret():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus", 180, "nu", lista)
    lista = adaugaRezervare("3", "George", "economy", 110, "nu", lista)

    rezultat = ordonareDescrescatorDupaPret(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "3"
    assert getId(rezultat[2]) == "1"


def testSumaPreturiPerNume():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Andrei", "economy plus", 180, "nu", lista)
    lista = adaugaRezervare("3", "Ruben", "economy", 110, "nu", lista)

    rezultat = sumaPreturiPerNume(lista)

    assert len(rezultat) == 2
    assert rezultat["Ruben"] == 210
    assert rezultat["Andrei"] == 180
