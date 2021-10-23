from Domain.rezervare import getNume, creeazaRezervare, getId, getClasa, getPret, getCheckin


def schimbareClasaDupaStringNume(substringNume, clasa, lista):
    """
    Trece toate rezervarile facute pe un Nume la o clasa superioara
    :param substringNume: substringul dupa care se cauta rezervarile de modificat
    :param modificareClasa: clasa superioara cu care se modifica rezervarea
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
