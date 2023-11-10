## Uppgift 1 (3p)

# Skriv din kod här:
import math

def beraknaC(a, b):
    # Omvandla från str till int
    a = int(a)
    b = int(b)
    # Få talets exponent
    a = a**2
    b = b**2
    # Kvadratrot för att få c, pythagoras sats
    c = math.sqrt(a + b)
    # Return och gör så att bara det finns två 2 decimaler
    return format(c, '.2f')

print (beraknaC (input('Ange längd på A: ') , input('Ange längd på B: ')))

## Uppgift 2 (3p)

# Skriv din kod här:

import random

# Fråga efter inmatning
spelomgångar = int(input('Skriv in antal spelomgångar som ska simuleras: '))
print('----------------------------------------')

# Simulera spelomgångar 
for i in range(spelomgångar):
    # Beräkningar
    tärning1 = random.randint(1, 6)
    tärning2 = random.randint(1, 6)
    summa = tärning1 + tärning2
    
    # Skriv ut resultat
    print(f'Tärningarna blev {tärning1} + {tärning2} = {summa}')
    if summa == 7 or tärning1 == tärning2:
        print('Du har vunnit!')

## Uppgift 3 (4p)

# Skriv din kod här:

till_talet = int(input("Ange sista talet som skall kontrolleras: "))
primtalen = []

# Finns inte negativa primtal
if till_talet > 0:
    if till_talet >= 1:
        primtalen.append(1)
    if till_talet >= 2:
        primtalen.append(2)

    # Beräkna alla primtal till sista talet
    for nummer in range(3, till_talet + 1):
        for primtal in reversed(primtalen):
            if primtal == 1:
                primtalen.append(nummer)
            elif nummer % primtal == 0:
                break
        
# Skrivs ut alla primtal som har blivit beräknade
print(f"Följande är primtal från 1 till {till_talet}")
print(primtalen)

## Uppgift 4 (6p)

betygsbok = {'Kalle': [92, 88, 97,72, 98, 96],'Lisa': [82, 95, 99,97, 82, 91],'Erik': [84, 95, 89,98, 78, 75],'Elsa': [97, 91, 88,90, 80, 73],'Emma': [79, 87, 96,76, 84, 93]}
# Skriv din kod här:

import matplotlib.pyplot as plotting

print('Namn       Medelbetyg    Lägsta betyg    Högsta betyg')
print('----------------------------------------------------------')

klassens_summa = 0
klassens_antal_elever = 0
klassens_lägsta = -1
klassens_högsta = -1

medelbetyg_lista = []
namn = []

# Beräkna värderna
for key, value in betygsbok.items():
    # Få värderna för enskilda student
    summa = 0
    lägsta_betyg = value[0]
    högsta_betyg = value[0]
    for number in value:
        summa += number
        if number < lägsta_betyg:
            lägsta_betyg = number
        if number > högsta_betyg:
            högsta_betyg = number
    medelbetyg = summa / len(value)
    
    # Spara information för att sedan visa i stapeldiagrammet
    klassens_summa += summa
    klassens_antal_elever += len(value)
    
    if klassens_lägsta == -1: # Det här är för att initialisera variablerna
        klassens_lägsta = lägsta_betyg
        klassens_högsta = högsta_betyg
        
    if lägsta_betyg < klassens_lägsta:
        klassens_lägsta = lägsta_betyg
    if högsta_betyg > klassens_högsta:
        klassens_högsta = högsta_betyg
    
    namn.append(key)
    medelbetyg_lista.append(medelbetyg)
    
    # Gör att det är 2 decimaler
    lägsta_betyg = format(lägsta_betyg, '.2f')
    högsta_betyg = format(högsta_betyg, '.2f')
    medelbetyg   = format(medelbetyg, '.2f')
    
    print(f'{key:<13}{medelbetyg:<15}{lägsta_betyg:<16}{högsta_betyg}')
    print('----------------------------------------------------------')
           
# Skriv ut sista delen av tabelen
print('==========================================================')
tal = format(klassens_summa/klassens_antal_elever, '.2f')
print(f'Medelbetyget för klassen är: {tal}')
print(f'Lägsta betyget i klassen är: {klassens_lägsta}')
print(f'Högsta betyget i klassen är: {klassens_högsta}')
print('----------------------------------------------------------')

# Skapa stapeldiagrammet
plotting.bar(namn, medelbetyg_lista, width = .2, color = '#1F77B3')

# Olika plottiningsfunktioner för att få det som i uppgiftsbeskrivningen
plotting.title('Medelbetyg av studenter')
plotting.xlabel('Namn')
plotting.ylabel('Medelbetyg')
plotting.xticks(rotation=45)
plotting.grid()
plotting.show()

## Uppgift 5 (4p)

# Hitta felen och rätta koden. Glöm inte skriva kommentar vid varje rättning.

talgare = int(input('Ange täljaren: '))
namnare = int(input('Ange namnaren: '))
gemensam = namnare
if talgare < namnare:
    gemensam = talgare # 1. vi måste ha den minsta av talgare eller namnare, inte dela
while gemensam > 1: # 2. så länge gemensam är störe än 1 finns det möjlighet att vi kan hitta mindre täljare
    if talgare % gemensam == 0 and namnare % gemensam == 0: # 3. båda måste var helt delbara tal, inte ett, måste var and och inte or
        talgare /= gemensam; # 4. vi behöver dela inte module, för anars blir det 0. ändra från / till %
        namnare /= gemensam
    gemensam -= 1
print('Det förenklade bråket blev:',int(talgare),'/',int(namnare))

## Uppgift 6 (20p)
# Skriv din kod här:
# a)
import csv

def lasaFil(): 
    arr = []
    
    # Öppnar csv-filen
    with open('energipriser.csv', mode="r", encoding="UTF-8") as csv_filename: # Läser CSV-filen
        reader = csv.reader(csv_filename, delimiter=";")                 # Gör varje rad i CSV-filen till en lista
        for row in reader:
            arr.append(row)                                       # Lägger varje rad i listan
    return arr # return array med data

energiData = lasaFil()

# Skriver ut 3 första raderna för att vissa att allt stämer
for i in range(3):
    print(energiData[i])

# b)
import matplotlib.pyplot as plt

def plotta_data(data_lista):
    """Skapa ett diagram utifrån prisutvecklingen från en lista."""
    max_värde = 0
    data_str = [] # samla alla olika varor tjänster
    åren = [int(year) for year in data_lista[0][1:]] # samla alla år i en lista
    
    # Skapa grafen
    for data in data_lista[1:]:
        data_str.append("['" + data[0] + "']")
        y = []
        for d in data[1:]:           # spara alla värderna för kategori
            y.append(float(d))
            if float(d) > max_värde: # spara största värdet för y-axeln, beroende på största värdet som finns i data_lista
                max_värde = float(d)
        plt.plot(åren, y)            # gör graf för kategori
    
    plt.legend(data_str, loc="upper left")
    max_värde += max_värde / 20 #  lägg till +5% i y-axel värdet för att det ska se snyggt ut
    plt.ylim(45, max_värde)

    # Lägg till info
    plt.xlabel("År")
    plt.ylabel("Energipriser för hushållskunder (öre/kWh)")
    plt.title("Energipriser för hushållskunder 1996-2021")
    plt.grid(True)
    plt.show()

plotta_data(energiData)

# c)

def medelvärde_av_energipriser_för_hushållskunder():
    namn = []
    medelvärde_lista = []
    
    print('Medelvärde av energipriser för hushållskunder År 1996–2021')
    print('-----------------------------------------------------------------------+')
    print('|Namn                                        |Medelvärde               |')
    print('+============================================+=========================+')
    # Beräkna medelvärdet av olika produkter
    for row in energiData[1:]:
        summa = 0
        for värde in row[1:]:
            summa += int(värde)
        
        # Spara till stapeldiagramet värderna
        namn.append(row[0])
        medelvärde_lista.append(summa/(len(row)-1))
        
        medelvärde = format(summa/(len(row)-1), '.2f')
        
        print(f'|{row[0]:<44}|{medelvärde}')
        print('+--------------------------------------------+-------------------------+')
    
    # Skapa stapeldiagrammet
    plt.bar(namn, medelvärde_lista, width = .2, color = 'green')

    # Olika plottiningsfunktioner för att få det som i uppgiftsbeskrivningen
    plt.title('Medelvärde av energipriser för hushållskunder 1996–2021 ')
    plt.xlabel('Namn')
    plt.ylabel('Medelvärde av energipriser för hushållskunder (öre/kWh)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
    
medelvärde_av_energipriser_för_hushållskunder()
//
