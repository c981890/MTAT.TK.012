from random import randint

valik=input('''Kas soovite istekohta ise valida ("ise") või loosida ("loos")? ''')
if valik == "ise":
    asukoht=input('''Kas soovite istuda akna ääres ("aken") või mitte ("muu")? ''')
    if asukoht == "aken":
        print("Valisite ise. Aknakoht")
    else:
        print("Valisite ise. Vahekäigukoht")
else:
    suvaline_arv = randint(1, 99)    
    if suvaline_arv > 34:
        print("Istekoht loositi. Vahekäigukoht")
    else:
        print("Istekoht loositi. Aknakoht")
    