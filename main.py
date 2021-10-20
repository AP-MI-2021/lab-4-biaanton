import math

def menu():
    print('1.Citire lista')
    print('2.Afisarea partii intregi a tuturor numerelor din lista')
    print('3.Afisarea numerelor care apartin unui interval deschis citit de la tastatura')
    print('4.Afisarea tuturor numerelor a caror parte intreaga este divizor al partii fractionare')
    print('x.Iesire din program')


def citire_lista():
    lst = []
    lst_str=input('Dati numerele separate prin spatiu')
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(float(num_str))
    return lst


def parte_intreaga(numar):
    '''
    Determina partea intreaga a unui numar
    :param numar: numarul a carui parte intreaga o cautam
    :return: partea intreaga a numarului
    '''
    return math.trunc(numar)


def parte_intreaga_lista(lst):
    '''
    Determina partea intreaga a fiecarui element din lista
    :param lst: lista din care luam numerele
    :return: lista cu partea intreaga a fiecarui element din lista
    '''
    result = []
    for num in lst:
        result.append(int(parte_intreaga(num)))
    return result

def test_parte_intreaga_lista():
    assert parte_intreaga_lista([1.5,-3.3,8,9.8,3.2])==[1,-3,8,9,3]
    assert parte_intreaga_lista([6,7.2,-4.5,5,9.3])==[6,7,-4,5,9]
    assert parte_intreaga_lista([3,12.7,4.6,-7.6])==[3,12,4,-7]


def numere_apartin_intervalului(lst, start, stop):
    '''
    Determina nuemrele din lista care apartin unui interval deschis citit de la tastatura
    :param lst: Lista din care verificam daca numerele apartin intervalului deschis
    :param start:inceputul intervalului
    :param stop:sfarsitul intervalului
    :return: numerele care apartin intervalului deschis citit de la tastatura
    '''
    result = []
    for num in lst:
        if num > start and num < stop:
            result.append(num)
    return result


def test_numere_apartin_intervalului():
    assert numere_apartin_intervalului([1.5,-3.3,8,9.8,3.2],-4,5)==[1.5,-3.3,3.2]
    assert numere_apartin_intervalului([6.3,-4.9,-6,2,7,9],-5,5)==[-4.9,2]
    assert numere_apartin_intervalului([3.2,-5.6,2.2,-1.6,3],-2,4)==[3.2,2.2,-1.6,3]


def parte_fractionara(numar):
    if numar-parte_intreaga(numar)==0: return 0
    return str(numar).split('.')[1]


def este_div(numar):
    '''
    Verifica daca partea intreaga a unui numar este divizor al partii fractionare
    :param numar: numarul la care verificam proprietatea ca partea intreaga sa fie divizor al partii fractionare
    :return: valoarea 1 daca partea intreaga a unui numar este divizor al partii fractionare, respectiv 0 in caz contrar
    '''
    parte_fract=parte_fractionara(numar)
    parte_intr=parte_intreaga(numar)
    if parte_fract==0: return 0
    if int(parte_fract)%int(parte_intr)==0:
        return 1
    return 0

def lista_parte_intreaga_divizor_parte_fract(lst):
    '''
    Determina numerele in care partea intreaga este divizor al partii fractionare
    :param lst: lista din care luam numerele
    :return: numerele in care partea intreaga este divizor al partii fractionare
    '''
    result = []
    for num in lst:
        if este_div(num)==1:
            result.append(num)
    return result

def test_lista_parte_intreaga_divizor_parte_fract():
    assert lista_parte_intreaga_divizor_parte_fract([1.5,-3.3,8,9.8,3.2])==[1.5,-3.3]
    assert lista_parte_intreaga_divizor_parte_fract([2.6,-4.8,9.7,6.3])==[2.6,-4.8]
    assert lista_parte_intreaga_divizor_parte_fract([6.6,-1.8,9.7,6.4,2.8,7])==[6.6,-1.8,2.8]


def main():
    lst = []
    while True:
        menu()
        opt = input('Alege optiunea: ')
        if opt== '1':
            lst=citire_lista()
        elif opt=='2':
            print(f'Afisarea partii intregi a tuturor numerelor din lista: {parte_intreaga_lista(lst)}')
        elif opt=='3':
            start=int(input('Introduceti numarul de unde incepe intervalul'))
            stop=int(input('Intoduceti numarul unde se sfarseste intervalul'))
            print(f'Afisarea numerelor care apartin intervalului deschis ({start},{stop} este: {numere_apartin_intervalului(lst,start,stop)}.')
        elif opt=='4':
            print(f'Afisarea numerelor care au partea intreaga divizor al partii fractionare: {lista_parte_intreaga_divizor_parte_fract(lst)}')
        elif opt == 'x':
            break
        else: print('Optiune invalida, reincearca!')

if __name__=='__main__':
    test_parte_intreaga_lista()
    test_numere_apartin_intervalului()
    test_lista_parte_intreaga_divizor_parte_fract()
    main()


