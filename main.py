from Logic.CRUD import adaugaRezervare
from Tests.testAll import RunAllTests
from UI.console import runMenu


def main():
    RunAllTests()
    lista = adaugaRezervare("1", "Ruben", "economy", 150, "da", [])
    lista = adaugaRezervare("2", "Andrei", "economy plus", 180, "da", lista)
    lista = adaugaRezervare("3", "George", "economy", 155, "nu", lista)
    runMenu(lista)


main()
