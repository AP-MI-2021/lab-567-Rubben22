from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare
from Tests.testDomain import testRezervare
from Tests.testFunctionalitati import testSchimbareClasa


def RunAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testSchimbareClasa()
