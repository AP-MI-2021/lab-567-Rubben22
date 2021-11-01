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
    return {"id": id, "nume": nume, "clasa": clasa, "pret": pret, "checkin": checkin}


def getId(rezervare):
    """
    Returneaza id-ul unei rezervari
    :param rezervare: un dicitonar de tip rezervare
    :return: id-ul rezervarii - string
    """
    return rezervare["id"]


def getNume(rezervare):
    return rezervare["nume"]


def getClasa(rezervare):
    return rezervare["clasa"]


def getPret(rezervare):
    return rezervare["pret"]


def getCheckin(rezervare):
    return rezervare["checkin"]


def toString(rezervare):
    return "id: {}, nume: {}, clasa: {}, pret: {}, checkin: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin(rezervare)
    )
