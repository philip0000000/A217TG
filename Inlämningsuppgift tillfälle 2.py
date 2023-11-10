## Deluppgift 1

import csv

def read_file(csv_filename):
    """Läs innehållet i en CSV-filen och returnera den som en lista."""
    with open(csv_filename, mode="r", encoding="UTF-8") as csv_data: # Läser CSV-filen för att få information om data
        reader = csv.reader(csv_data, delimiter=";")                 # Gör varje rad i CSV-filen till en lista, och lämna tillbaka det
        return list(reader)                                          # Skapar en lista med innehållet av flera listor

# Läs data från CSV-filerna och lagra dem för att kunna använd i den här cellen och andra celler
kpiData       = read_file("kpi-1.csv")
tjansteData   = read_file("tjänster-1.csv")
livsmedelData = read_file("livsmedel-1.csv")

# Skriv ut de två första raderna av varje fil för att visa lite exempel data till användaren
print("\033[1mkpiData:\033[0m")         # Bold text
print(kpiData[:2])
print("\n\033[1mtjansteData:\033[0m")   # Ny rad och sen bold text
print(tjansteData[:2])
print("\n\033[1mlivsmedelData:\033[0m") # Ny rad och sen bold text
print(livsmedelData[:2])

## Deluppgift 2

import matplotlib.pyplot as plt

def calc_mean(all_år, få_månad):
    """Skapa data från list i parametrar för grafer och ett stapeldiagram."""
    data_alla_år, lista_medelvärde, månad_värde_för_alla_år = [], [], []
    # Beräkna all åren data för grafen
    for år in reversed(all_år[1:]):
        data_alla_år.append(int(år[0])) # Lägg till året
        # Samla ihop hela årets gemensam summa, använd inte första index eftersom det är året som data är för
        summa = 0
        for månad in år[1:]:
            summa += float(månad)
        summa /= len(år) - 1 # Beräkna medelvärde
        # Lägg till medelvärdet
        lista_medelvärde.append(summa)
        if år[0] == "2022" and få_månad > 7: # Undvik att lägg till om index är över 7 för år 2022
            continue
        månad_värde_för_alla_år.append(float(år[få_månad]))

    # Skapa grafer och ett stapeldiagram
    if len(månad_värde_för_alla_år) != len(data_alla_år):                 # Hantera fel om inte samma längd på x och y
        plt.plot(data_alla_år[:-1], månad_värde_för_alla_år, color="red")
    else:
        plt.plot(data_alla_år, månad_värde_för_alla_år, color="red")
    plt.plot(data_alla_år, lista_medelvärde, color="black")
    plt.bar(data_alla_år,  lista_medelvärde, color="#ADD8E6")

    # Lägg till info
    str = "Linje diagram för " \
    + ["","januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"][få_månad]
    plt.legend((str, "Linje diagram för medel kpi", "kpiMedel"), loc="upper left")

    plt.title("Konsumentprisindex År 1980-2022")
    plt.xlabel("År")     # X-axel och y-axel namn
    plt.ylabel("Konsumentprisindex")
    plt.xlim(1980, 2021) # Max och min värde på x-axel och y-axel.
    plt.ylim(100, 400)
    plt.grid(True)
    plt.show()

# Fråga efter en månad (1 – 12).
presentera_månad = int(input("Ange vilken månad som ska presenteras: "))
# Felkontroll, lite grann
if presentera_månad > 12:
    presentera_månad = 12
elif presentera_månad <= 0:
    presentera_månad = 1
calc_mean(kpiData, presentera_månad) # Beräkna och skapa en graf

## Deluppgift 3

def plotta_data(data_lista):
    """Skapa ett diagram utifrån prisutvecklingen från en lista."""
    max_värde = 0
    data_str = [] # Samla alla olika varor tjänster
    åren = [int(year) for year in data_lista[0][1:]] # Samla alla år i en lista
    
    # Skapa grafen
    for data in data_lista[1:]:
        data_str.append(data[0])     # Spara tjänst
        y = []
        for d in data[1:]:           # Spara alla värderna för kategori
            y.append(float(d))
            if float(d) > max_värde: # Spara största värdet för y-axeln, beroende på största värdet som finns i data_lista
                max_värde = float(d)
        plt.plot(åren, y)            # Gör graf för kategori
    
    plt.legend(data_str, loc="upper left")
    plt.xlim(1978, 2025)
    max_värde += max_värde / 20 #  Lägg till +5% i y-axel värdet för att det ska se snyggt ut
    plt.ylim(80, max_värde)

    # Lägg till info till diagramet som skapas
    plt.xlabel("År")
    plt.ylabel("Prisutvecklingen")
    if len(data_str) == 7:
        plt.title("Prisutvecklingen för olika kategorier av varor och tjänster År 1980-2022")
    else: #elif: len(data_str) == 8:
        plt.title("Prisutvecklingen för olika livsmedel År 1980-2022")
    plt.grid(True)
    plt.show()

plotta_data(tjansteData)
plotta_data(livsmedelData)

## Deluppgift 4

def Prisutveckling_I_Procentform(lista1, lista2):
    """Beräknar prisutvecklingen i procentform för olika kategorier, år 1980–2021.
    Skriver sen ut och ritar resultatet i en tabell och ett stapeldiagram."""
    for index, Data_Lista in enumerate([lista1, lista2]):
        # Skriv ut text fyllning för tabelen
        print("+-------------------------------------------------------------------------+")
        # Lägg till rätt text för rubrik
        titel = "|Kategorier "
        if len(Data_Lista) == 7:
            titel += "av varor och tjänster"
        else: #len(Data_Lista) == 8:
            titel += "olika typer av livsmedel"
        # Skriv ut titeln och rubriken för tabelen
        print("{:42.50}{:<10}".format(titel, "|Prisutvecklingen i procentform"))
        print("+=========================================+===============================+")
        
        x, y = [], [] # Spara x-axeln och y-axeln
        for data in Data_Lista[1:]:
            # Spara och beräkna prisutveckling i olika kategorier
            pip = data[-1:][0]
            pip = float(pip) - 100 # Ta bort 100%
            pip = round(pip, 2)    # Begränsar floats till två decimaler
            y.append(data[0])      # Spara kategori till stapeldiagram
            x.append(pip)          # Spara beräkning på kategori till stapeldiagram
            
            # Skriv ut kategori och prisutvecklingen i procentform.
            print("|{:41.50}|{:<10}".format(data[0], pip)) # data[0] är namn på varor eller tjänst
            if data != Data_Lista[-1]:
                print("+-----------------------------------------+-------------------------------+")
            else:
                print("+-------------------------------------------------------------------------+")
                
        # Rita stapeldiagram
        plt.barh(y, x, color=["#00008B", "#0000FF"][index])
    # Skapa stapeldiagram
    plt.xlim(0, 800)
    plt.title("Prisutvecklingen för olika kategorier av varor och tjänster samt för olika typer av livsmedel År 1980-2021 i procenform")
    plt.xlabel("Prisutvecklingen i procentform")
    plt.ylabel("Olika kategorier av varor och tjänster samt för olika typer av livsmedel")
    plt.show()

Prisutveckling_I_Procentform(tjansteData, livsmedelData)

## Deluppgift 5

def Månad_Varje_År_Störst_KPI_Förändringen(åren):
    """Beräknar och presenterar den månad från år 2000-2022 som har största KPI-förändringen
    från en månad till nästkommande i utskriven tabel och punktdiagram."""
    alla_månader = ["", "Jan", "Feb", "Mar", "Apr", "Maj", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dec"]
    största_förändring = [ 0, ""]
    tabel_data = []
    index = 1
    
    # Spara och beräkna data
    while index < len(åren):
        if int(åren[index][0]) > 1999:    # Bara år efter 1999 beräkna
            månader = åren[index]         # All data för all månader.
            summa = float(månader[1])
            
            # Beräkna januari (anvönd förra året dec)
            största_KPIChange_månad_värde = (float(åren[index][1]) - float(åren[index+1][12])) / float(åren[index+1][12])
            största_KPIChange_månad = 1

            # Beräkna feb till dec
            index2 = 2
            while index2 < len(månader):
                summa += float(månader[index2]) # Sammanlagda värdet för månaden.
                
                # KPI-förändringen från en månad till nästkommande.
                temp = (float(månader[index2]) - float(månader[index2-1])) / float(månader[index2-1])
                if abs(temp) > abs(största_KPIChange_månad_värde): # Spara största värdet.
                    största_KPIChange_månad_värde = temp
                    största_KPIChange_månad = index2
                index2 += 1
                
            # Beräkna
            årsmedelvärde = summa / (len(månader) - 1)
            
            # Spara
            tabel_data.append([månader[0],                    # år
                               största_KPIChange_månad_värde, # procent förändring
                               största_KPIChange_månad,       # månad med störs förändring
                               årsmedelvärde])
            if abs(största_KPIChange_månad_värde) > abs(största_förändring[0]): # Spara om störst
                största_förändring[0] = största_KPIChange_månad_värde
                största_förändring[1] = alla_månader[största_KPIChange_månad] + " " + åren[index][0]
        index += 1

    # Skriva ut tabel data
    print("==========================================================================")
    print()
    print("                      ANALYS AV KPI UNDER ÅREN 2000 - 2022")
    print("                      ------------------------------------")
    print()
    print("                      Största förändring")
    print("                      ------------------")
    print("År                    %            månad                  Årsmedelvärde")
    print("--------------------------------------------------------------------------")

    for data in reversed(tabel_data):
        #         år | %     mån | årsmedelvärde
        print("{:<22}{:<13}{:<23}{}".format(data[0],
                                            round(data[1] * 100, 2), # Omvandla till procent och avrunda
                                            alla_månader[data[2]],
                                            round(data[3], 2) ))     # Omvandla till procent och avrunda
    print()
    print("Största förändring:   {:<13}{}".format(round(största_förändring[0] * 100, 2), # Omvandla till procent och avrunda
                                                  största_förändring[1]))
    print("==========================================================================")
    
    # Skapa punktdiagram
    for row in reversed(tabel_data):
        året = row[0]
        månad = row[2]
        plt.scatter(månad, året, color = "#403DCD")  
    
    # Lägg till text
    plt.xlabel("Månad")
    plt.ylabel("År")
    plt.title("Största förändring av KPI för en enskild månad under åren 2000-2022")
    plt.grid(True)
    plt.show()

Månad_Varje_År_Störst_KPI_Förändringen(kpiData)

## Deluppgift 6

def Main():
    """Meny där användaren anger ett av menyalternativen.
    När menyalternativet är utfört ska användaren på nytt kunna ange ett menyalternativ."""
    Loop = True
    while Loop == True:
        print("Program för att läsa in och analysera resultatet i uppgift 1 – 5")
        print()
        print("1. Läser in csv-filerna")
        print("2. Konsumentprisindex under åren 1980 – 2022")
        print("3. Prisutvecklingen för de olika kategorierna i filerna ”Varor och tjänster” samt ”Livsmedel” under åren 1980 – 2021")
        print("4. Prisutvecklingen i procentform för de olika kategorierna i filerna ”Varor och tjänster” samt ”Livsmedel” under åren 1980 – 2021")
        print("5. Förändringar i KPI under åren 2000 – 2022")
        print("6. Avsluta programmet")
        print()
        val = input("Välj menyalternativ (1–6): ")
        if val == "1": # Läser in csv-filerna
            # Få information om data filernas namn
            val = input("namn för kpi.csv(standardnamn: kpi-1.csv): ")
            kpiData = val if val != "" else "kpi-1.csv"
            val = input("namn för tjänster.csv(standardnamn: tjänster-1.csv): ")
            tjansteData = val if val != "" else "tjänster-1.csv"
            val = input("namn för livsmedel.csv(standardnamn: livsmedel-1.csv): ")
            livsmedelData = val if val != "" else "livsmedel-1.csv"
            # Hämta data
            kpiData = read_file(kpiData)
            tjansteData = read_file(tjansteData)
            livsmedelData = read_file(livsmedelData)
            # Skriv ut de två första raderna av varje fil
            print("\033[1mkpiData:\033[0m")         # Bold text
            print(kpiData[:2])
            print("\n\033[1mtjansteData:\033[0m")   # Ny rad och sen bold text
            print(tjansteData[:2])
            print("\n\033[1mlivsmedelData:\033[0m") # Ny rad och sen bold text
            print(livsmedelData[:2])
        elif val == "2": # Konsumentprisindex under åren 1980 – 2022
            # Fråga efter en månad (1 – 12).
            presentera_månad = int(input("Ange vilken månad som ska presenteras: "))
            # Felkontroll, lite grann
            if presentera_månad > 12:
                presentera_månad = 12
            elif presentera_månad <= 0:
                presentera_månad = 1
            calc_mean(kpiData, presentera_månad) # Beräkna och skapa en graf
        elif val == "3": # Prisutvecklingen för de olika kategorierna
            plotta_data(tjansteData)
            plotta_data(livsmedelData)
        elif val == "4": # Prisutvecklingen i procentform för de olika kategorierna
            Prisutveckling_I_Procentform(tjansteData, livsmedelData)
        elif val == "5": # Förändringar i KPI
            Månad_Varje_År_Störst_KPI_Förändringen(kpiData)
        elif val == "6": # Avsluta programmet
            print("Avslutar programmet")
            Loop = False
        else:
            print("Okänt kommando")
            
Main()
print("Programmet är avslutat")
