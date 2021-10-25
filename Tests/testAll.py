from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare, testGetById
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testSchimbareClasa


def RunAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testSchimbareClasa()
    testModificaRezervare()
    testGetById()