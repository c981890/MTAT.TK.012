import string
failinimi = input('Sisestaga failinimi: ')

f = open(failinimi, encoding="UTF-8")

failisisu = f.read()
vaiketaht_failisisu = failisisu.lower()
asendatud = vaiketaht_failisisu.replace("ä","ae").replace('ö', 'oe').replace('õ', 'oe').replace('ü', 'ue')
print(asendatud.upper()) 

f.close()



