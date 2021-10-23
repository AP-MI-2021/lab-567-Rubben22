from Domain.rezervare import creeazaRezervare, getId, getClasa


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    """
    Adauga o rezervare intr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista continand atat rezervarile vechi cat si cele noi..
    """
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def stergeRezervare(id, lista):
    '''
    sterge o rezervare dupa id-ul dintr-o lista
    :param id: id-ul rezervarii de sters, string
    :param lista: lista de rezervari
    :return: o lista continand prajiturile cu id-ul diferit de id
    '''
    return [rezervare for rezervare in lista if getId(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    '''
    Modifica o rezervare dintr-o lista
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin: string
    :param lista: lista de rezervari
    :return: o lista care contine rezervarile vechi cat si cele modificate
    '''
    listaNoua = []
    for rezervare in lista:
        if getId(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def getById(id, lista):
    '''

    :param id:
    :param lista:
    :return:
    '''
    for rezervare in lista:
        if getId(rezervare) == id:
            return rezervare
    return None