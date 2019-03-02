nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))

esialgne_tulemus = (lubatud_kiirus - tegelik_kiirus) * -3
trahv = min(190, esialgne_tulemus)

print(str(nimi) + ", kiiruse ületamise eest on teie trahv " + str(trahv) + " eurot.")


