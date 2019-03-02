def eelarve(kylalisi):
    ''' (int) -> int
    Eelarve koosneb kahest osast: söök ja ruumi rent. Söögi peale arvestatakse
    iga osaleja kohta 10 eurot. Ruumi rent maksab sõltumata osalejate arvust
    55 eurot.
    Arvutab kylalisi põhjal eelarve kogusumma;
    Tagastab eelarve kogusumma.
    >>> eelarve(5)
    105
    '''
    
    return kylalisi * 10 + 55

inimesi_kutsutud = int(input('Mitu inimest on kutsutud? '))
inimesi_tuleb = int(input('Mitu inimest tuleb? '))

print('Maksimaalne eelarve: ' + str(eelarve(inimesi_kutsutud)) + ' eurot')
print('Minimaalne eelarve: ' + str(eelarve(inimesi_tuleb)) + ' eurot')
