from Logic.CRUD import adaugaRezervareUndoRedo
from Logic.functionalitati import undo, redo


def test_undo_redo():
    undoList = []
    redoList = []
    lista = []
    lista = adaugaRezervareUndoRedo("1", "Andrei", "economy plus", 180, "da", lista, undoList, redoList)
    lista = adaugaRezervareUndoRedo("2", "Carmen", "economy plus", 100, "nu", lista, undoList, redoList)
    lista = adaugaRezervareUndoRedo("3", "Andreea", "business", 249.9, "nu", lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "2", "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": "3", "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]

    lista = undo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "2", "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"}]

    lista = undo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista = undo(lista, undoList, redoList)
    assert lista == []
    lista = undo(lista, undoList, redoList)
    assert lista is None

    undoList = []
    redoList = []
    lista = []

    lista = adaugaRezervareUndoRedo("1", "Andrei", "economy plus", 180, "da", lista, undoList, redoList)
    lista = adaugaRezervareUndoRedo("2", "Carmen", "economy plus", 100, "nu", lista, undoList, redoList)
    lista = adaugaRezervareUndoRedo("3", "Andreea", "business", 249.9, "nu", lista, undoList, redoList)
    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "2", "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": "3", "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]

    lista = undo(lista, undoList, redoList)
    lista = undo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "2", "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"}]

    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "2", "nume": "Carmen", "clasa": "economy plus", "pret": 100, "checkin": "nu"},
                     {"id": "3", "nume": "Andreea", "clasa": "business", "pret": 249.9, "checkin": "nu"}]

    lista = undo(lista, undoList, redoList)
    lista = undo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista = adaugaRezervareUndoRedo("4", "Mircea", "economy", 150, "da", lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "4", "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]
    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "4", "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]

    lista = undo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"}]

    lista = undo(lista, undoList, redoList)
    assert lista == []

    lista = redo(lista, undoList, redoList)
    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "4", "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]

    lista = redo(lista, undoList, redoList)
    assert lista == [{"id": "1", "nume": "Andrei", "clasa": "economy plus", "pret": 180, "checkin": "da"},
                     {"id": "4", "nume": "Mircea", "clasa": "economy", "pret": 150, "checkin": "da"}]
