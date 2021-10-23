from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, stergeRezervare, getById


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", lista)
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Ruben"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 250
    assert getCheckin(getById("1", lista)) == "da"


def testStergeRezervare():
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", [])
    lista = adaugaRezervare("2", "Carmen", "economy plus", 100, "nu", lista)

    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None

    lista = stergeRezervare("3", lista)
    assert len(lista) == 1
    assert getById("2", lista) is not None
