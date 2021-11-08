from Domain.rezervare import getNume, creeazaRezervare, getId, getPret, getCheckin, getClasa


def schimbareClasaDupaStringNume(substringNume, clasa, lista):
    """
    Trece toate rezervarile facute pe un Nume la o clasa superioara
    :param clasa: Clasa superioara cu care se va inlocui vechea rezervare
    :param substringNume: substringul dupa care se cauta rezervarile de modificat
    :param lista: lista continand rezervari
    :return: lista continand rezervarile care au fost modificate, in functie de nume
    """
    listaNoua = []
    for rezervare in lista:
        if substringNume in getNume(rezervare):
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                clasa,
                getPret(rezervare),
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def ieftinireRezervare(procentaj, lista):
    """
    Aplica o reducere pentru rezervarile care au facut checkin
    :param procentaj: procentajul cu care se va face ieftinirea
    :param lista: lista cu rezervari
    :return: lista continand atat rezervarile care au fost ieftinite, cat si cele vechi
    """
    if procentaj < 0:
        raise ValueError("Procentajul nu poate fi negativ! ")
    listaNoua = []
    for rezervare in lista:
        if "da" in getCheckin(rezervare):
            reducere = procentaj / 100 * getPret(rezervare)
            rezervareNoua = creeazaRezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                getPret(rezervare) - reducere,
                getCheckin(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua


def determinarePretMaximClasa(lista):
    """
    Determina cel mai mare pret pentru fiecare clasa
    :param lista: lista cu rezervari
    :return: un dictionar care contine pretul maxim pentru fiecare clasa
    """
    rezultat = {}
    for rezervare in lista:
        clasa = getClasa(rezervare)
        if clasa in rezultat:
            if getPret(rezervare) > rezultat[clasa]:
                rezultat[clasa] = getPret(rezervare)
        else:
            rezultat[clasa] = getPret(rezervare)
    return rezultat


def ordonareDescrescatorDupaPret(lista):
    """
    Functia returneaza o lista in care rezervarile sunt ordonate descrescator dupa pret
    :param lista: lista de rezervari
    :return: lista cu rezervarile ordonate descrescator dupa pret
    """
    return sorted(lista, key=lambda rezervare: getPret(rezervare), reverse=True)


def sumaPreturiPerNume(lista):
    """
    Functia returneaza suma preturilor penru fiecare Nume
    :param lista: lista cu rezervari
    :return: o lista cu suma preturilor pentru fiecare nume
    """
    rezultat = {}
    for rezervare in lista:
        nume = getNume(rezervare)
        pret = getPret(rezervare)
        if nume in rezultat:
            rezultat[nume] = rezultat[nume] + pret
        else:
            rezultat[nume] = pret
    return rezultat

def undo(lista, undolist, redolist):
    if len(undolist) > 0:
        redolist.append(lista)
        lista = undolist.pop()
    else:
        return None
    return lista

def redo(lista, undolist, redolist):
    if len(redolist) > 0:
        undolist.append(lista)
        lista = redolist.pop()
    return lista
