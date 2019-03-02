def teleri_diagonaal(kaugus_meetrites):
    ''' (float) -> int
    1. võtab argumendiks ühe arvu, mis tähistab kaugust diivanist teleri asu-
    kohani meetrites;
    2. arvutab selle põhjal teleri diagonaali tollides;
    3. tagastab teleri diagonaali tollides.
    Tagastatud teleri diagonaal peab olema ümardatud täisarvuni.
    >>> teleri_diagonaal(5.2)
    81
    '''
    return round(kaugus_meetrites * 100 * 0.39 / 2.5)

kaugus_meetrites = float(input('Sisesta kaugus: '))
print(teleri_diagonaal(kaugus_meetrites))