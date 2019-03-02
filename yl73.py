from easygui import *
esimene_arv = integerbox("Sisestage esimene täisarv lõigus 1-10:", lowerbound = 1, upperbound = 10)
teine_arv = integerbox("Sisestage teine täisarv lõigus 1-10:", lowerbound = 1, upperbound = 10)

nupud = ["+","-","*"]
vajutati = buttonbox('Valige tehe: ', choices = nupud)

if vajutati == '+':
    vastus = esimene_arv + teine_arv
    msgbox("Tehte tulemus on " + str(vastus))
elif vajutati == "-":
    vastus = esimene_arv - teine_arv
    msgbox("Tehte tulemus on " + str(vastus))
else:
    vastus = esimene_arv * teine_arv
    msgbox("Tehte tulemus on " + str(vastus) + ".")
