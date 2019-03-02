vanus=int(input("Sisestage enda vanus: "))
sugu=input("Sisestage enda sugu: ")
treeningu_tyyp=input("Sisestage treeningu tüüp: ")

maks_pulss_m = 220 - vanus
vahim_pulss_1_m = round(maks_pulss_m * 50 / 100)
suurim_pulss_1_m = round(maks_pulss_m * 70 / 100)
suurim_pulss_2_m = round(maks_pulss_m * 80 / 100)
suurim_pulss_3_m = round(maks_pulss_m * 87 / 100)

maks_pulss_n = 206 - vanus*0.88
vahim_pulss_1_n = round(maks_pulss_n * 50 / 100)
suurim_pulss_1_n = round(maks_pulss_n * 70 / 100)
suurim_pulss_2_n = round(maks_pulss_n * 80 / 100)
suurim_pulss_3_n = round(maks_pulss_n * 87 / 100)
    
if sugu.lower() == "m" and treeningu_tyyp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(vahim_pulss_1_m) + " kuni " + str(suurim_pulss_1_m) + ".")
if sugu.lower() == "m" and treeningu_tyyp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(suurim_pulss_1_m) + " kuni " + str(suurim_pulss_2_m) + ".")
if sugu.lower() == "m" and treeningu_tyyp == "3":
    print("Pulsisagedus peaks olema vahemikus " + str(suurim_pulss_2_m) + " kuni " + str(suurim_pulss_3_m) + ".")

if sugu.lower() == "n" and treeningu_tyyp == "1":
    print("Pulsisagedus peaks olema vahemikus " + str(vahim_pulss_1_n) + " kuni " + str(suurim_pulss_1_n) + ".")
if sugu.lower() == "n" and treeningu_tyyp == "2":
    print("Pulsisagedus peaks olema vahemikus " + str(suurim_pulss_1_n) + " kuni " + str(suurim_pulss_2_n) + ".")
if sugu.lower() == "n" and treeningu_tyyp == "3":
    print("Pulsisagedus peaks olema vahemikus " + str(suurim_pulss_2_n) + " kuni " + str(suurim_pulss_3_n) + ".")
    