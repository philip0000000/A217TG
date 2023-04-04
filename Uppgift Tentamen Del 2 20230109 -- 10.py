## Uppgift 1 a)

import math

def areaKon(r):
    """Beräknar basarean på en kon."""
    return math.pi * r**2

def volymKon(r, h):
    """Beräknar volymen på en kon."""
    v = areaKon(r) * h / 3
    return round(v, 1)

## Uppgift 1 b)

import random

def slumpmässiga_tal_hitta():
    random_list = [[random.randint(0, 100) for _ in range(4)] for _ in range(4)]
    # Gör deepcopy för att vi inte bara kopiera första listan
    hittad_list = [row[:] for row in random_list]
    hitta = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    
    print("Talen som vi har hittat är::")
    # Söka efter talen som vi söker och ersät de med "Hittad"
    for n, rad in enumerate(random_list):
        for m, element in enumerate(rad):
            if random_list[n][m] in hitta:
                # Skriv till användaren att vi har hittat ett tal
                hittad_list[n][m] = "Hittad"
                print(f"{element} som är i position ({n}, {m})")
    
    print("Den slumpmässigt skapade listan är:", random_list)
    print("Den modifierade lista är:", hittad_list)

slumpmässiga_tal_hitta()

## Uppgift 2 a)

def singlaslant():
    # Fråga användaren om antalet kast
    kast = int(input("Skriv in önskat antal kast: "))
    print(f"Tack, jag kastar myntet {kast} gånger:")
    
    # Spara resultaten
    krona = 0
    klave = 0
    
    # Simulerar kasten
    for i in range(kast):
        if random.randint(0, 1) == 0: # Simuleras med random 50% att det blir 1 eller 0, 0 för krona och 1 för klave.
            krona += 1
        else:
            klave += 1

    # Skriv till användaren resultatet
    print(f"Utfallet blev {krona} Krona och {klave} Klave.")

singlaslant()

## Uppgift 2 b)

def skapar_användarnamn():
    print("Skriv in ditt förnamn: ")
    namn = input()
    print("Skriv in ditt efternamn: ")
    efternamn = input()
    while True:
        print("Skriv in ditt födelsedatum: ")
        födelsedatum = input()
        if len(födelsedatum) != 6:
            print("Födelsedatumet är inte 6 tecken långt. Gör om.")
        elif int(födelsedatum[4:6]) < 1 or int(födelsedatum[4:6]) > 31:
            print("Födelsedatumet har ogiltiga dagar. Gör om.")
        elif int(födelsedatum[2:4]) < 1 or int(födelsedatum[2:4]) > 12:
            print("Födelsedatumet har ogiltiga månader. Gör om.")
        else:
            print("Födelsedatumet är giltigt.")
            break
            
    # Vi skapar användarnamnet igenom att lägga ihop det som vi frågade efter
    användarnamnet = namn[:4] + efternamn[-4:] + födelsedatum[-4:]
    
    # Fråga efter lösenord och skapa sen ett lösenord
    specialtecken = ['$','%','&','~','!','@','#','^','*','(',')','_','-','+','=']
    while True:
        print("Ange önskat lösenord: ")
        lösenord = input()
        
        # Vi testar lössenordet om det är fel eller inte, om det är fel gör om
        lower = False
        upper = False
        special = False
        for c in lösenord:
            if c.islower():
                lower = True
                break
        for c in lösenord:
            if c.isupper():
                upper = True
                break
        for c in lösenord:
            if c in specialtecken:
                special = True
                break
        if len(lösenord) >= 10 and upper and lower and special:
            print("Lösenordet uppfyller kraven.")
            break
        else:
            print("Lösenordet uppfyller inte kraven. Gör om.")
            
    print(f"Ditt användarnamn är {användarnamnet} och ditt lösenord är {lösenord}")
    
skapar_användarnamn()

## Uppgift 2 c)

def Sort(lista, N):
    for i in range(N):
        min_index = i # inte 0
        for j in range(i+1 , N):
            if lista[j] < lista[min_index]: # inte >
                min_index = j # inte i
        temp = lista[i]
        lista[i] = lista[min_index] # inte lista[j]
        lista[min_index] = temp
    return lista

listan = [5, 45, -4, 101, 78, 188, 97, -104, 47]
print(f'Listan som ska sorteras är {listan} \n')
N = len(listan)
sorteradLista = Sort(listan, N)
print(f'Den sorterade listan är {sorteradLista}')

## Uppgift 3 a)

import csv

def read_file(file_name):
    inkomstData = []
    with open(file_name, newline='', encoding="UTF-8") as csvfile: # Läser CSV-filen för att få information om data
        reader = csv.reader(csvfile)
        for row in reader:
            inkomstData.append(row)
    return inkomstData

inkomstData = read_file("inkomster.csv")

print(inkomstData[:3])

## Uppgift 3 b)

import matplotlib.pyplot as plt

kvinnor = [float(row[1]) for row in inkomstData[1:]]
män = [float(row[2]) for row in inkomstData[1:]]
x = [row[0] for row in inkomstData[1:]]

plt.figure(figsize=(25,10))
plt.plot(x, kvinnor, 'r', label="Kvinnor")
plt.plot(x, män, 'b', label="Män")
plt.xlabel("År")
plt.ylabel("Inkomst (SEK)")
plt.title("Inkomst för män och kvinnor")
plt.legend()
plt.grid()
plt.xticks(rotation=90)
plt.show()

## Uppgift 3 c)

## Uppgift 3 d)

import csv

def read_file2():
    file_name = "inkomsterKommuner.csv"
    inkomstData = []
    with open(file_name, newline='', encoding="UTF-8") as csvfile: # Läser CSV-filen för att få information om data
        reader = csv.reader(csvfile)
        for row in reader:
            inkomstData.append(row)
    return inkomstData

inkomstData = read_file2()

print(inkomstData[:3])
