def kas_veel_mahub(vabade_kohtade_arv, soovijate_arv):
    ''' (int, int) -> Boolean
    Funktsioon tagastab tõeväärtuse, kas soovijad mahuvad paati.
    >>> kas_veel_mahub(10, 9)
    True
    >>> kas_veel_mahub(10, 10)
    True
    >>> kas_veel_mahub(10, 11)
 failinimi failisisu = []
f = open(failinimi, encoding="UTF-8")= input('Sisestage failinimi: ')
failisisu = []
f = open(failinimi, encoding="UTF-8")
for rida in f.read().split('\n'):
    failisisu.append(int(rida))
f.close()
   False
    '''
    return (vabade_kohtade_arv >= soovijate_arv)

failinimi = input('Sisestage failinimi: ')
failisisu = []
f = open(failinimi, encoding="UTF-8")
for rida in f.read().split('\n'):
    failisisu.append(int(rida))
f.close()

paadi_mahutavus = int(input('Mitu reisijat paati mahub: '))

soidukite_arv = 0
for i in failisisu:
    if kas_veel_mahub(paadi_mahutavus, i):
        paadi_mahutavus = paadi_mahutavus - i
        soidukite_arv += 1

print('Paati said ' + str(soidukite_arv) + ' sõiduki inimesed')
print('Vabu kohti jäi ' + str(paadi_mahutavus))
