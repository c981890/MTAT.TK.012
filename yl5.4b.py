synnid = []
surmad = []
iibed = []

fail = open("synnid.txt", encoding="UTF-8")
for rida in fail:
    synnid.append(int(rida))
fail.close()

fail = open("surmad.txt", encoding="UTF-8")
for rida in fail:
    surmad.append(int(rida))
fail.close()

for i in range(len(synnid)):
    iibed.append(synnid[i] - surmad[i])

print(iibed)

for i in range(len(synnid)):
    if iibed[i] > 0:
        print(i+1)
