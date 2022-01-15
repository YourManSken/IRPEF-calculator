#INIT
#Reddito sotto il quale non si pagano imposte
reddito_senza_aliquote =  8174

#Aliquote e fasce 2020
fasce_2020 = [0, 15000, 28000, 55000, 75000]
aliquote_2020 = [23, 27, 38, 41, 43]

#Aliquote e fasce 2022
fasce_2022 = [0, 15000, 28000, 50000]
aliquote_2022 = [23, 25, 35, 43]

#Init global arrays fasce e aliquote
fasce_scelte, aliquote_scelte = [], []

#FUNC
#Calcola l'IRPEF sul reddito
def calcola_irpef(reddito, fasce, aliquote, tabella=None): #Function overloading: possiamo chiamare calcola_irpef con o senza l'arg tabella
    #CHECK
    try:
        #Esegue un codice se non incontra errori
        reddito = int(reddito)  #Controlla se il reddito puó essere trasformato in numero, ovvero se é un numero, altrimenti da errore
    except:
        #Se incontra errori esegue questo altro codice
        print(f'\nInput {reddito} in calcola_irpef é invalido')
        api()   #Chiama la funzione api() ovvero quella che permette l'input dei dati

    #INIT
    irpef = 0
    somme_irpef = []
    tributi_irpef = []
    
    #RUN
    if (reddito > reddito_senza_aliquote):  #Controlla se il reddito é superiore a 8174 Euro
        for i in range(len(aliquote)-1):    #Ripete per numero di aliquote - 1 volte
            if (reddito < (dimensione_fascia := fasce[i+1] - fasce[i])):    #Controlla se il reddito é inferiore alla dimensione della fascia
                #Se é inferiore
                reddito_fascia = reddito
                #Dichiara il reddito tassato in questa fascia uguale al reddito
                #Es: reddito = 10000, fascia = 0-15000, il reddito tassato nella fascia é 10000, ovvero il reddito totale
                reddito = 0 #Azzera il reddito
            else:
                #Se é maggiore
                reddito_fascia = dimensione_fascia
                #Dichiara il reddito tassato in questa fascia uguale alla dimensione della fascia
                #Es: reddito = 20000, fasica = 0-15000, il reddito tassato nella fascia é 15000, ovvero la dimensione della fascia
                reddito -= (dimensione_fascia)  #Riduce il reddito del quantitativo tassato nella fascia

            somme_irpef.append(reddito_fascia)  #Aggiunge il reddito tassato nella fascia a un array
            tributi_irpef.append(tributo := reddito_fascia*aliquote[i]/100) #Aggiunge l'imposta della fascia a un array
            irpef += tributo    #Aumenta l'irpef totale dell'imposta della fascia

        #Stessa cosa ma per il reddito superiore alla fascia piú alta
        somme_irpef.append(reddito)
        tributi_irpef.append(tributo := reddito*aliquote[-1]/100)
        irpef += tributo

    else:   #Riferito al reddito troppo basso per l'imposta
        #Mette l'irpef a 0
        irpef = 0
        somme_irpef = [reddito]
        tributi_irpef = [0]

    if str(tabella).lower() == 'true' or str(tabella).lower() == 'y':
        #Se richiesta, crea una tabella
        print_tabella(somme_irpef, tributi_irpef)
    else:
        #Altrimenti scrive l'irpef totale
        print(irpef)

#Costruisce una tabella coi valori degli scaglioni e del reddito
def print_tabella(somme, tributi):
    riga = ''
    len_tab = 16    #Grandezza colonne di default in caratteri

    #Allarga le colonne
    if (len_s := len(str(sum(somme)))) > len_tab:   #Se il reddito é maggiore della dimensione delle colonne le allarga
        len_tab = len_s+2
    
    for _ in range(4): riga+=('{:<'+str(len_tab)+'}') #Costruisce una riga della tabella con colonne di determinata lunghezza

    print(riga.format('SCAGLIONI', 'SOMMA', 'ALIQUOTA', 'IMPOSTA')) #Printa titoli

    #Separatore
    for _ in range(len_tab*4): print('─', end='') #Fa una riga di separazione (──────────)
    print('')   #Printa un newline (siccome la stringa é nulla e end='\n' scrive \n)

    #Printa tabella
    for scaglione, somma, aliquota, imposta in zip(fasce_scelte, somme, aliquote_scelte, tributi):  #Itera attraverso l'universo
        print(riga.format(scaglione, somma, aliquota, imposta))

    #Separatore
    for _ in range(len_tab*4): print('─', end='')
    print('')

    #Printa totali
    print(riga.format('TOTALE:', str(sum(somme)), str(sum(aliquote_scelte)), str(sum(tributi))))

#Input vari
def api():
    #INIT
    global fasce_scelte
    global aliquote_scelte

    anno = input('\nInserire 2020 o 2022 per utilizzare le aliquote dell\'anno corrispondente: ')

    #CHECK
    if anno == '2020':
        fasce_scelte = fasce_2020
        aliquote_scelte = aliquote_2020
    elif anno == '2022':
        fasce_scelte = fasce_2022
        aliquote_scelte = aliquote_2022
    else:
        print(f'Input {anno} non é valido, inserire 2020 o 2022.')
        api()   #Recursion: la funzione si chiama da sola (quando metto un valore non valido, la funzione ricomincia)

    #RUN
    #Calcola l'irpef coi parametri dell'input
    calcola_irpef(input('Inserire reddito: '), fasce_scelte, aliquote_scelte, input("Restituire una tabella o solo l'imposta (y/n): "))

    #Ripete lo script se 'y'
    if input("Calcolare l'imposta di un altro reddito? (y/n): ").lower() == 'y': api()

#RUN
api()   #Chiama la funzione api()