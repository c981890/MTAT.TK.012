failinimi = input('Palun sisestage failinimi: ')
asukoht = []
i = 1

fail = open(failinimi, encoding="UTF-8")
for rida in fail:
    realt = rida.strip('\n')
    asukoht.append(realt)
    print(str(i) + '.', realt)
    i = i + 1    
fail.close()

mitmes_sihtkoht = int(input('Valige mitmes sihtkoht broneerida: '))
soovitud_sihtkoht = asukoht[mitmes_sihtkoht - 1].strip()
print('Reis on broneeritud. Sihtkoht on ' + soovitud_sihtkoht + '.')