def kuu_nimi(kuu):
    ''' (int) -> str
    Tagastab vastava kuu nime väikeste tähtedega.
    >>> kuu_nimi(1)
    'jaanuar'
    '''
    kuud = [
        'jaanuar',
        'veebruar',
        'märts',
        'aprill',
        'mai',
        'juuni',
        'juuli',
        'august',
        'september',
        'oktoober',
        'november',
        'detsember',
        ]
    kuu = int(kuu)
    return kuud[kuu - 1]

def kuupäev_sõnena(kuupaev):
    ''' (str) -> str
    Võtab argumendiks ühe sõnena esitatud kuupäeva formaadis “DD.MM.YYYY”;
    Tagastab selle sama kuupäeva kujul <päev>. <kuu_nimi> <aasta>. a,
    kusjuures kuupäev_sõnena peab ühe toimingu delegeerima funktsioonile
    kuu_nimi.
    >>> kuupäev_sõnena('24.02.1918')
    '24. veebruar 1918. a'
    '''
    kuupaev_list = []
    kuupaev_list = kuupaev.split('.')
    vastus = (kuupaev_list[0] + '.', kuu_nimi(kuupaev_list[1]), kuupaev_list[2]
              + '. a')
    return " ".join(vastus)

kuupaev = input('Sisesta kuupäev kujul DD.MM.YYYY: ')
print(kuupäev_sõnena(kuupaev))
