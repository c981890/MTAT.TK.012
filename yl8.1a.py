def lõimede_pikkus(vaiba_pikkus, loimede_arv):
    ''' (float, int) -> float
    Arvutab  ja väljastab, kui palju läheb lõimeniiti vaja kõigi vaipade peale
    kokku ümardatuna sajandikeni.
    >>> lõimede_pikkus(7, 120)
    1068.0
    '''
    print(round((loimede_arv * (vaiba_pikkus * 1.2 + 0.5)), 2))
    return round((loimede_arv * (vaiba_pikkus * 1.2 + 0.5)), 2)
  
failinimi = input('Sisestaga failinimi: ')
failisisu = []
f = open(failinimi, encoding="UTF-8")
for rida in f.read().split('\n'):
    failisisu.append(float(rida))
f.close()

pikemate_vaipade_loimede_arv = int(input('Sisestage 5-meetriste ja pikemate'
                                         ' vaipade lõimede arv: '))
luhemate_vaipade_loimede_arv = int(input('Sisestage lühemate vaipade lõimede'
                                         ' arv: '))

lühemate_vaipade_pikkus = 0
pikemate_vaipade_pikkus = 0

for i in failisisu:
    if i < 5:
        #print(i)
        lühemate_vaipade_pikkus = (lühemate_vaipade_pikkus
                                   + lõimede_pikkus(i, luhemate_vaipade_loimede_arv))
    else:
        #print(i)
        pikemate_vaipade_pikkus = (pikemate_vaipade_pikkus
                                   + lõimede_pikkus(i, pikemate_vaipade_loimede_arv))

print('Kõigi vaipade peale läheb vaja '
      + str(round((lühemate_vaipade_pikkus + pikemate_vaipade_pikkus), 2))
      + ' meetrit lõimeniiti.')