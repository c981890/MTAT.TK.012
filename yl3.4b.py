from random import randint

visketabavuse_protsent = int(input("Sisestage visketabavuse protents: "))
i = 1
tabanud_visked = 0

while i <= 1000:
    vise = randint(1, 100)
    if vise <= visketabavuse_protsent:
        print(str(i) + ". vise tabas")
        tabanud_visked += 1
    else:
        print(str(i) + ". vise mööda")
    i += 1
print("Tabas " + str(tabanud_visked) + ". viset.")
