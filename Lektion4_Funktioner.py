#2 Öva på funktioner och moduler
#Samla ihop dina funktioner så att de ligger i en eller flera moduler.
# Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

#Övning 1 Skriv en funktion som tar en sträng som parameter.
# När den anropas ska den skriva ut strängen och "är en fena på programmering". Exempel:
#my_function("David") → "David är en riktig hacker"
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


#Övning 3 - Koden ska sluta loopa efter 5 varv
def loop(y):
    print("\nÖvning 3 - Koden ska sluta loopa efter 5 varv")
    end = 5
    #y = 1
    for x in range (1, 100): #startar vid 1 och stoppar vid 100
        y *= 2 #samma som y = y*2
        # print (f"Varv {x} är y {y}") #kodrad för extra koll under kodning
        if x == end: #avsluta loop med if sats
            break
    print(y)


#Övning 4 - Den ska ta en lista som parameter och returnera det sista elementet i listan.
def last (number_list):
    print("\nÖvning 4 - returnera det sista elementet i listan.")
    return (number_list[-1])


#Övning 5 - Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
def cut_edges(number_list2):
    print("\nÖvning 5 - Den ska ta en lista som parameter. När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.")
    number_list2 = number_list2 [1:-1]
    return (number_list2)


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


#Övning 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista.
# Exempel:
#pretty_print(["a", "b", 3.14])
#Listan har 3 element:
#1. a
#2. b
#3. 3.14
def print_list(pretty_print):
    print("\nÖvning 8 - Skriva ut innehållet i en lista")
    length = len (pretty_print)
    if length > 0:
        print(f"Listan har {length} element:")
        for element in pretty_print:
            i = pretty_print.index(element) + 1
            print(f"{i}: {element}")
    else:
        print ("Listan är tom!")
