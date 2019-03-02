perenimi = input("Sisestage Leedu perekonnanimi: ")

if perenimi[-2:] == "ne":
    print("Abielus")
elif perenimi[-2:] == "te":
    print("Vallaline")
elif perenimi[-1] != "e":
    print("Pole ilmselt leedulanna perekonnanimi")
elif perenimi[-1] == "e" and perenimi[-2:] != "ne":
    print("Määramata")