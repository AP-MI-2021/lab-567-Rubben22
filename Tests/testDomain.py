from Domain.rezervare import creeazaRezervare, getId, getNume, getClasa, getPret, getCheckin


def testRezervare():
    rezervare = creeazaRezervare("1", "Ruben", "business", 250, "nu")
    assert getId(rezervare) == "1"
    assert getNume(rezervare) == "Ruben"
    assert getClasa(rezervare) == "business"
    assert getPret(rezervare) == 250
    assert getCheckin(rezervare) == "nu"
