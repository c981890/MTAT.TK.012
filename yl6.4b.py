def pronksikarva_summa(taisarvud):
    ''' (list) -> int
    Tagastab järjendis olevate arvude 1, 2 ja 5 summa.
    >>> pronksikarva_summa([1, 20, 20, 5, 50, 2, 2, 1])
    11
    '''
    summa = 0
    
    for mynt in taisarvud:
        if mynt == 1 or mynt == 2 or mynt == 5:
            summa = summa + mynt
    return summa

failinimi = input('Sisesta failinimi: ')

fail = open(failinimi, encoding="UTF-8")
taisarvud = []
 
for rida in fail:
    taisarvud.append(int(rida))   
fail.close()

print(pronksikarva_summa(taisarvud))