arv = int(input("Sisestage täisarv: "))
i = 1
astendamise_tulemus = 0
summa = 0

while i <= arv:
    if i == 1:
        summa = 1
    elif i == 2:
        summa = 2   
    else:
        summa = 2 ** (i - 1)
    i += 1
print("Nisuteri " + str(arv) + ". ruudu eest: " + str(summa))

    
