ostjate_arv = int(input("Sisesta ostjate arv: "))

i = 0
j = 1
summa = 0

while i < ostjate_arv:
    summa = summa + j
    j += 2
    i += 1
print("Lillede koguarv on ", summa, ".")
