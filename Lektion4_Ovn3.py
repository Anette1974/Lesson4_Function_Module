print("Övning 3 - Koden ska sluta loopa efter 5 varv\n")
end = 5
y = 1
for x in range (1, 100): #startar vid 1 och stoppar vid 100
    y *= 2 #samma som y = y*2
    # print (f"Varv {x} är y {y}") #kodrad för extra koll under kodning
    if x == end: #avsluta loop med if sats
        break
print(y)