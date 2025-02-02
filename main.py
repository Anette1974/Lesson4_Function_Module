print("Övning 2 - Funktioner och moduler\n")
import Lektion4_Funktioner #Importerar funktioner från Lektion4_Funktioner

Lektion4_Funktioner.my_function("Anette")

Lektion4_Funktioner.eko("Hej", 3)

Lektion4_Funktioner.eko2("Hej", 20)

Lektion4_Funktioner.loop(1)

#Övning 4 Skriv en funktion med namnet last. Den ska ta en lista som parameter och returnera det sista elementet i listan.
#last([1, 2, 3]) → 3
print("Sista elementet i listan är: ", Lektion4_Funktioner.last([5,25,14]))

#Övning 5 Skriv en funktion med namnet cut_edges. Den ska ta en lista som parameter.
# När den anropas ska den returnera en ny lista, där den har tagit bort första och sista elementet.
#cut_edges([1, 2, 3, 4]) → [2, 3]
print ("Elementen i mitten är: ", Lektion4_Funktioner.cut_edges([1,2,3,4]))

Lektion4_Funktioner.increase(2)

Lektion4_Funktioner.average(2,4)

#Övning 8 Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom, eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista.
# Exempel:
#pretty_print(["a", "b", 3.14])
#Listan har 3 element:
#1. a
#2. b
#3. 3.14
Lektion4_Funktioner.print_list(["a",9,3.14])