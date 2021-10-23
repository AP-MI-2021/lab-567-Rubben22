from Domain.rezervare import getNume, creeazaRezervare, getId, getPret, getCheckin


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
