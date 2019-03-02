from urllib.request import urlopen

kuu = input('Sisestage kuu: ')
paev = int(input('Sisestage päev: '))
vastus = urlopen("https://courses.cs.ut.ee/MTAT.TK.012/2017_fall/uploads/Main/"
                 + str(kuu))
nimepaevad = vastus.read().splitlines()
print('Kuupäeval ' + str(paev) + '. ' + kuu + ' on nimepäevad järgmiste'
      ' nimedega inimestel: ' + '\n' + str(nimepaevad[paev-1]))
