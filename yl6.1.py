def banner(reklaamlause):
    ''' (str) -> str
    Tagastab reklaamlause, kus kõik tähed on suurtähed.
    >>> banner('Ole tegija!')
    'OLE TEGIJA!'
    '''
    
    return reklaamlause.upper()

mitu_korda = int(input('Mitu korda soovite reklaamlauset kuvada? '))
reklaamlause = input('Sisestage reklaamlause: ')
i = 0

while i != mitu_korda:
    print(banner(reklaamlause))
    i = i + 1