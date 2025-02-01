# Denna sida innehåller funktionerna, anropen finns i main filen
#Övning 1 - Skriver ut en text
def my_function(name):
    print("\nÖvning 1, Skriver ut en text")
    print(f"{name} är en riktig hacker!\n")

#Övning 2b - Skriver ut valfritt ord x antal gånger med radbrytning mellan
def eko (ord, antal):
    print("\nÖvning 2b - Skriver ut valfritt ord x antal gånger med radbrytning mellan")
    for antal in range (antal):
        print(f"{ord}")

#Övning 2b - Skriver ut valfritt ord x antal gånger efter varandra
def eko2 (ord, antal):
    print("\nÖvning 2b - Skriver ut valfritt ord x antal gånger efter varandra")
    eko_list = []
    for antal in range (antal):
        eko_list.append(ord)
    print(f"{eko_list}")

#Övning 4 - Den ska ta en lista som parameter och returnera det sista elementet i listan.
def last ():
    print("\nÖvning 4 - returnera det sista elementet i listan.")
    number_list = [1,2,3]
    print (number_list[len(number_list)-1]) #samma som nedan
    print (number_list[- 1])

#Övning 5 - Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
def cut_edges():
    print("\nÖvning 5 - Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.")
    number_list2 = [1,2,3,4]
    number_list2.remove(1)
    number_list2.remove(4)
    print(number_list2)

#Övning 6 - Lös felen i koden
def increase (x):
    print("\nÖvning 6 - Lös felen i koden")
    #return x #return avbryter vidare exekvering och måste därmed flyttas längre ner i koden
    x += 1
    print(x)
    return x
#print(increase(1)) #ger inget print tillbaks när funktionen körs. Däremot gör print det som ligger högre upp

#Övning 7 - Bygg en funktion med namnet average. Den ska ta parametrar: x och y. Båda ska vara tal. Funktionen ska returnera medelvärdet.
def average (x, y):
    print("\nÖvning 7 - Räkna ut medelvärdet")
    medel = (x+y)/2 # räknar ut medelvärdet av talen x och y
    print(f"Medelvärdet av tal {x} och tal {y} är: {medel}")

#Övning 8 - Skriva ut innehållet i en lista
def print_list():
    print("\nÖvning 8 - Skriva ut innehållet i en lista")
    pretty_print = (["a", "b", 3.14]) # Två olika alternativ av pretty_print, om jag vill test tom lista eller med 3 element
    #pretty_print = ([])
    length = len (pretty_print)
    if length > 0:
        print(f"Listan har {length} element:")
        print("1. "+pretty_print[0])
        print("2. "+pretty_print[1])
        print("3. "+str(int(pretty_print[2]))) #Konverterar int till str innan de skrivs ut
    else:
        print ("Listan är tom!")
