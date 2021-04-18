from datetime import datetime
datetime.strftime(datetime.now(), 'Azi %d %b %Y %H:%M:%S')
enunt = """
    Creati un program cu o lista de carti utilizand dictionare si liste.
    Va avea urmatoarele facilitati:
(afisare, adaugare, stergere element, stergere dictionar, cautare, modificare, iesire din program).
    Afisarea dictionarului se va face de forma: key => Value.
    Folositi chei numerice incepand de la 0, iar valoarea intrarii trebuie sa fie
introdusa de utilizator de la tastatura din meniul adaugare.
    Value va fi o lista care sa contina urmatoarele elemente introduse de utilizator:
        Titlu   	 sir de caractere
        Autor  	sir de caractere
    La adaugarea unei intrari noi in dictionar sa se caute urmatoarea cheie libera (incrementare).
    Dupa fiecare intrare in dictionar afisati fiecare element al listei stocate pe cate un rand.
    Pe langa facilitatile indicate mai sus (adaugare, stergere, afisare, iesire din program)
adaugati posibilitatea de a cauta o intrare dupa un sir de caractere, dupa Titlu
si Continut (in acelasi timp implementat prin  or  ). Listare titlu si autor sau inexistent.
""" #



print("\t\t Dictionar de carti")

carte_dict = {}     # initializam dictionarul
new_key = 1     # initializam cheile dictionarului (prima cheie)
new_val = []    # intializam lista tempoarare utilizata la popularea valorilor in dictionar

while True:
    print("""\nSelecteaza
--------------------------------------------
0 - Pentru afisare dictionar actual
1 - Pentru introducerea unui element nou
2 - Pentru stergerea unui element existent
3 - Pentru stergerea dictionarului
4 - Pentru cautare in dictionar
5 - Pentru modificare element existent
9 - Pentru iesire
--------------------------------------------
""")
    alege = input('Optiunea mea este: ')
    if alege == '0':
        if carte_dict != {}:
            for elem in carte_dict:
                print(elem, 'Titlu:', carte_dict[elem][0], ' Autor:', carte_dict[elem][1])
        else:
            print('Dictionarul este gol\n')

    elif alege == '1':
        titlu = input('Introduceti titlul cartii: ')
        autor = input('Introduceti autorul cartii: ')
        new_val.append(titlu)
        new_val.append(autor)
        carte_dict.update({new_key: new_val})
        for elem in carte_dict:
            print('Element:', elem, ' Titlu:', carte_dict[elem][0], ' Autor:', carte_dict[elem][1])
        new_val = []
        new_key += 1

    elif alege == '2':
        if carte_dict:
            for elem in carte_dict:
                print('Element:', elem, ' Titlu:', carte_dict[elem][0], ' Autor:', carte_dict[elem][1])
            sterge = int(input('Sterge elementul cu cheia: '))
            if sterge in carte_dict.keys():
                carte_dict.pop(sterge)
                print('Elementul cu cheia', sterge, 'a fost sters.')
            else:
                print('Element inexistent!\n')

        else:
            print('Dictionarul este gol\n')

    elif alege == '3':
        carte_dict = {}
        print('Dictionar sters\n')

    elif alege == '4':
        cauta = input('Introduceti textul cautat: ')
        for expr in carte_dict.values():
            if cauta in expr[0] or cauta in expr[1]:
                print('Titlul:', expr[0], 'Autor:', expr[1])
            else:
                print('Textul cautat nu exista.')

    elif alege == '5':
        if carte_dict:
            modifica = int(input('Introduceti cheia elementului de modificat: '))
            if modifica in carte_dict.keys():
                t, c = input('Introduceti titlul: '), input('Introduceti autorul: ')
                carte_dict[modifica] = [t, c]
            else:
                print('Cheia', modifica, 'nu se afla in dictionar.')
        else:
            print('Dictionarul este gol.')

    elif alege == '9':
        print('O zi frumoasa!')
        break

    else:
        print('Nu ai ales o optiune corecta')

input('Apasa <enter> pentru a iesi.')
