import random

random.seed()
scelta = ""
g_scelta = ""

while True:
    num_list = [0]
    num_min = int(input("Inserisci il numero minimo: "))
    num_max = int(input("Inserisci il numero massimo: "))
    num_list  = range(num_min, num_max + 1)
    p_scelta = random.choice(num_list)

    while g_scelta != p_scelta:
        g_scelta = int(input("Indovina il numero che ho scelto: "))
        if g_scelta > p_scelta:
            print("Il numero che io ho pensato è minore rispetto al tuo. Riprova")
        elif g_scelta < p_scelta:
            print("Il numero che io ho pensato è maggiore rispetto al tuo. Riprova")
        else:
            print("Hai indovinato!!")
            break


    scelta  = str(input("Vuoi rigiocare [Y/n]:"))
    if scelta == "" or scelta == "Y" or scelta == "y":
        pass
    else:
        break

print("Alla prossima partita!")