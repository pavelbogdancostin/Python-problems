'''
    In acest program putem introduce intr-un fisier text numele restaurantelor si adresele acestora.
'''

restaurante= open('C:\\Users\\Bogdan\\Desktop\\InfoAcademy_Python\\my_exercices\\restaurante.txt','a', encoding="utf-8")
raspuns=""

def restaurant():
    '''Raspunsul la intrebari trebuie sa fie 'DA' sau 'NU'.'''
    bool = True
    introdeceti_restaunt = input("Doriti sa introduceti un restaurant?" + raspuns + "\n").lower()
    #introdeceti_restaunt=introdeceti_restaunt.lower()
    if introdeceti_restaunt == "da" :
        adauga_restaurant()
        mai_adauga_un_restaurant()
    elif introdeceti_restaunt == "nu":
        print("Nu ati dorit sa introduceti un nou restaurant!")
        bool = False
        return bool
    else:
        bool = False
        print("Nu ati raspuns corect la intrebare!")
        return restaurant()

def adauga_restaurant():
    restaurant = input("Introduceti denumirea restaurantului: ")
    restaurante.write("Restaurant: " + restaurant + "\n")
    mai_multe_adrese = input("Restaurantul se puate gasi la mai multe adrese?" + raspuns + "\n").lower()    
    if mai_multe_adrese == "da":
        adrese_multe()
    elif mai_multe_adrese == "nu":
        adresa = input("Introduceti adresa: ")
        restaurante.write("Adresa: " + adresa + "\n\n")
    else:
        print("Nu ati raspuns corect la intrebare!")

def adrese_multe():
    nr_de_adrese = int(input("Precizati cate adrese doritui sa introduceti: "))
    i = 1 						# i reprezinta nr de adrese, asemanator cu un contor
    while i <= nr_de_adrese:
        adresa = input("Introduceti adresa {0}: ".format(i))
        #restaurante.write("Adresa " + str(i) + ": " + adresa + "\n")
        restaurante.write("Adresa {}".format(i) + ": " + adresa + "\n")
        i += 1
    restaurante.write("\n")

def mai_adauga_un_restaurant():
    introduceti_inca_un_restaurant = input("Doriti sa mai introduceti un restaurant?" + raspuns + "\n").lower()
    if introduceti_inca_un_restaurant == "da":
        adauga_restaurant()
        return mai_adauga_un_restaurant()
    elif introduceti_inca_un_restaurant == "nu":
        print("Nu ati dorit sa introduceti un nou restaurant!")
    else:
        print("Nu ati raspuns corect la intrebare!")
        return mai_adauga_un_restaurant()

print(restaurant.__doc__)
restaurant()