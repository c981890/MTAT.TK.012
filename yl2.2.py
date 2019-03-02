suurus = float(input("Sisestage kirja suurus: "))
teema = input("Sisestage kirja teema pealkiri: ")
manus = input("Kas kirjaga on kaasas fail? ")

if not teema or (manus == "jah" and suurus > 1):
    print("Kiri on spämm")
else:
    print ("Kiri ei ole spämm")
