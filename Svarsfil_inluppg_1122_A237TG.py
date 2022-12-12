# Deluppgift 1

import csv

def read_file(csv_filename):
    """Läs innehållet i en CSV-filen och returnera den som en lista."""
    with open(csv_filename, mode="r", encoding="UTF-8") as csv_data: # Läser CSV-filen
        reader = csv.reader(csv_data, delimiter=";")                 # Gör varje rad i CSV-filen till en lista, och lämna tillbaka det
        return list(reader)                                          # Skapar en lista med innehållet av flera listor

# Läs data från CSV-filerna och lagra dem
kpiData       = read_file("kpi-1.csv")
tjansteData   = read_file("tjänster-1.csv")
livsmedelData = read_file("livsmedel-1.csv")

# Skriv ut de två första raderna av varje fil
print('\033[1mkpiData:\033[0m')         # Bold text
print(kpiData[:2])
print('\n\033[1mtjansteData:\033[0m')   # Ny rad och sen bold text
print(tjansteData[:2])
print('\n\033[1mlivsmedelData:\033[0m') # Ny rad och sen bold text
print(livsmedelData[:2])

# Deluppgift 2

import matplotlib.pyplot as plt

def calc_mean(all_år, få_månad):
    """Skapa data från list i parametrar för grafer och ett stapeldiagram."""
    data_alla_år = []
    lista_medelvärde = []
    månad_värde_för_alla_år = []
    for år in reversed(all_år[1:]):
        data_alla_år.append(int(år[0])) # lägg till året
        # Samla Ihop hela årets gemensam summa, använd inte första index eftersom det är året som data är för
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
    if len(månad_värde_för_alla_år) != len(data_alla_år):                 # Hantera fel om inte samma längd.
        plt.plot(data_alla_år[:-1], månad_värde_för_alla_år, color="red")
    else:
        plt.plot(data_alla_år, månad_värde_för_alla_år, color="red")
    plt.plot(data_alla_år, lista_medelvärde, color="black")
    plt.bar(data_alla_år, lista_medelvärde, color="#ADD8E6")

    # Lägg till info
    str = "Linje diagram för " \
    + ['',"januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"][få_månad]
    plt.legend((str, "Linje diagram för medel kpi", "kpiMedel"), loc="upper left")

    plt.title("Konsumentprisindex År 1980-2022")
    plt.xlabel("År")     # X-axel och y-axel namn
    plt.ylabel("Konsumentprisindex")
    plt.xlim(1980, 2023) # Max och min värde på x-axel och y-axel.
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

# Deluppgift 3

def plotta_data(data_lista):
    """Skapa ett diagram utifrån prisutvecklingen från en lista."""
    max_värde = 0
    data_str = [] # samla alla olika varor tjänster
    åren = [int(year) for year in data_lista[0][1:]] # samla alla år i en lista
    
    # Skapa grafen
    for data in data_lista[1:]:
        data_str.append(data[0])
        y = []
        for d in data[1:]:           # spara alla värderna för kategori
            y.append(float(d))
            if float(d) > max_värde: # spara största värdet för y-axeln, beroende på största värdet som finns i data_lista
                max_värde = float(d)
        plt.plot(åren, y)            # gör graf för kategori
    
    plt.legend(data_str, loc='upper left')
    plt.xlim(1978, 2025)
    max_värde += max_värde / 20 #  lägg till +5% i y-axel värdet för att det ska se snyggt ut
    plt.ylim(80, max_värde)

    # Lägg till info
    plt.xlabel('År')
    plt.ylabel('Prisutvecklingen')
    if len(data_str) == 7:
        plt.title('Prisutvecklingen för olika kategorier av varor och tjänster År 1980-2022')
    else: #elif: len(data_str) == 8:
        plt.title('Prisutvecklingen för olika livsmedel År 1980-2022')
    plt.grid(True)
    plt.show()

plotta_data(livsmedelData)
plotta_data(tjansteData)

# Deluppgift 4

# Deluppgift 5

# Deluppgift 6
