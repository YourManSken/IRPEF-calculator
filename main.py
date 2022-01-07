reddito_senza_tasse =  8174

fasce_2020 = [0, 15000, 28000, 55000, 75000]
tasse_2020 = [23, 27, 38, 41, 43]

fasce_2022 = [0, 15000, 28000, 50000]
tasse_2022 = [23, 25, 35, 43]

fasce = fasce_2022
tasse = tasse_2022

def calcola_irpef(reddito):
    irpef = 0
    if (reddito > reddito_senza_tasse):
        for i in range(len(tasse)-1):
            if ((reddito - (dimensione_fascia := fasce[i+1] - fasce[i])) < 0):
                reddito_fascia = reddito
                reddito = 0
            else:
                reddito_fascia = dimensione_fascia
                reddito -= (dimensione_fascia)

            irpef += reddito_fascia*tasse[i]/100

        irpef += reddito*tasse[-1]/100
    else:
        irpef = 0

    return irpef

reddito = 50000
print(calcola_irpef(reddito))