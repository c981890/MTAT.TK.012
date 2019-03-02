ostjate_arv = int(input("Sisesta ostjate arv: "))

i = 1
summa = 0

while i <= ostjate_arv:
    summa = summa + i
    i = i + 2
print("Lillede koguarv on ", summa, ".")
