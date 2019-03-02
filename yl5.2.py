ostjate_arv = int(input('Sisesta ostjate arv: '))

tulemus = 0

for i in range(1, ostjate_arv + 1, 2):
    tulemus = tulemus + i

print('Lillede koguarv on ' + str(tulemus))
    
