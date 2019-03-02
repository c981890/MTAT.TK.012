def tervitus(jrknr):
    ''' (int) -> str
    
    Võtab argumendiks tervituse järjekorranumbri arvuna, mis näitab mitmes
    tervitus on käsil;
    Kuvab väljakutsel ekraanile täpselt sellisel kujul tervituse ja vastuse
    koos tervituse järjekorranumbriga (n tähistab tervituse järjekorranumbrit):
    Võõrustaja: "Tere!"
    Täna n. kord tervitada, mõtiskleb võõrustaja.
    Külaline: "Tere, suur tänu kutse eest!"
    
    >>> tervitus(2)
    Võõrustaja: "Tere!"
    Täna 2. kord tervitada, mõtiskleb võõrustaja.
    Külaline: "Tere, suur tänu kutse eest!"
    '''
    print('Võõrustaja: "Tere"!\n'
          'Täna ' + str(jrknr) + '. kord tervitada, mõtiskleb võõrustaja.\n'
          'Külaline: "Tere, suur tänu kutse eest!"')

kylalisi = int(input('Sisestaga külaliste arv: '))
i = 1

while i != kylalisi + 1:
    tervitus(i)
    i = i + 1

