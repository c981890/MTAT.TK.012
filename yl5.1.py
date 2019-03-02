fail = open("mopeedid.txt", encoding="UTF-8")
mopeedid = []
 
for rida in fail:
    mopeedid.append(int(rida))   
fail.close()

jrk_nr = int(input('Palun sisestage mitmes kuu: '))

print(str(jrk_nr) + '. kuul registreeriti', mopeedid[jrk_nr-1], 'uut mopeedi.')