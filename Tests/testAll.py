from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testGetById
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testSchimbareClasa, testIeftinireRezervare, testDeterminarePretMaximClasa, \
    testOrdonareDescrescatorDupaPret, testSumaPreturiPerNume
from Tests.testUndoRedo import test_undo_redo


def RunAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testSchimbareClasa()
    testModificaRezervare()
    testGetById()
    testIeftinireRezervare()
    testDeterminarePretMaximClasa()
    testOrdonareDescrescatorDupaPret()
    testSumaPreturiPerNume()
    test_undo_redo()