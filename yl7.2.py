from datetime import datetime
kuupäev_kellaeg = datetime.today()

print("Kuupäev ja kellaeg: " + str(kuupäev_kellaeg))

fail = open("paevik.txt", "a") # fail avatakse juurde kirjutamiseks
sissekanne = input('Sisesta sissekande tekst: ')
fail.write(str(datetime.today()) + '\n' + sissekanne + '\n' +  '\n')
fail.close()
