from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin
from Logic.CRUD import adaugaRezervare, stergeRezervare, getById, modificaRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", lista)
    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Ruben"
    assert getClasa(getById("1", lista)) == "economy"
    assert getPret(getById("1", lista)) == 150
    assert getCheckin(getById("1", lista)) == "da"


def testStergeRezervare():
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", [])
    lista = adaugaRezervare("2", "Carmen", "economy plus", 100, "nu", lista)

    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert getById("1", lista) is None
    try:
        lista = stergeRezervare("3", lista)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False


def testModificaRezervare():
    lista = []
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", lista)
    lista = adaugaRezervare("2", "Carmen", "economy plus", 100, "nu", lista)

    lista = modificaRezervare("1", "Mihai", "business", 260, "nu", lista)

    rezervareUpdatata = getById("1", lista)
    assert getId(rezervareUpdatata) == "1"
    assert getNume(rezervareUpdatata) == "Mihai"
    assert getClasa(rezervareUpdatata) == "business"
    assert getPret(rezervareUpdatata) == 260
    assert getCheckin(rezervareUpdatata) == "nu"

    rezervareNeUpdatata = getById("2", lista)
    assert getId(rezervareNeUpdatata) == "2"
    assert getNume(rezervareNeUpdatata) == "Carmen"
    assert getClasa(rezervareNeUpdatata) == "economy plus"
    assert getPret(rezervareNeUpdatata) == 100
    assert getCheckin(rezervareNeUpdatata) == "nu"

    lista = []
    lista = adaugaRezervare("2", "Carmen", "economy plus", 100, "nu", lista)
    try:
        lista = modificaRezervare("1", "Mihai", "business", 260, "nu", lista)
    except ValueError:
        rezervareNeUpdatata = getById("2", lista)
        assert getId(rezervareNeUpdatata) == "2"
        assert getNume(rezervareNeUpdatata) == "Carmen"
        assert getClasa(rezervareNeUpdatata) == "economy plus"
        assert getPret(rezervareNeUpdatata) == 100
        assert getCheckin(rezervareNeUpdatata) == "nu"
    except Exception:
        assert False


def testGetById():
    lista = []
    lista = adaugaRezervare("1", "Carmen", "economy plus", 100, "nu", lista)
    lista = adaugaRezervare("2", "Andrei", "economy", 50, "nu", lista)
    assert getId(getById("1", lista)) == "1"
    assert getNume(getById("1", lista)) == "Carmen"
    assert getClasa(getById("1", lista)) == "economy plus"
    assert getPret(getById("1", lista)) == 100
    assert getCheckin(getById("1", lista)) == "nu"
