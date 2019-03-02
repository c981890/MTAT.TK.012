from datetime import *

failinimi = input('Sisestage failinimi: ')
nimekiri = []

fail = open(failinimi, encoding="UTF-8")
for rida in fail:
    realt = rida.strip('\n')
    nimekiri.append(realt)
fail.close()

paev = datetime.now().day
print(paev)
print(nimekiri[paev-1])
