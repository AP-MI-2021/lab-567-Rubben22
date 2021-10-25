def creeazaRezervare(id, nume, clasa, pret, checkin):
    """
    Creeaza un dictionar ce retine o rezervare
    :param id: id-ul rezervarii - string
    :param nume: numele rezervarii - string
    :param clasa: nume clasa: economy, economy plus, business - string
    :param pret: pretul rezervarii - float
    :param checkin: da sau nu - string
    :return: un dictionar ce contine o rezervare
    """
    return [id, nume, clasa, pret, checkin]


def getId(rezervare):
    """
    Returneaza id-ul unei rezervari
    :param rezervare: un dicitonar de tip rezervare
    :return: id-ul rezervarii - string
    """
    return rezervare[0]


def getNume(rezervare):
    return rezervare[1]


def getClasa(rezervare):
    return rezervare[2]


def getPret(rezervare):
    return rezervare[3]


def getCheckin(rezervare):
    return rezervare[4]


def toString(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
