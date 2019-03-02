inimeste_arv=int(input("Inimeste arv: "))
kohtade_arv=int(input("Kohtade arv: "))

busse_vaja = inimeste_arv // kohtade_arv
viimases_bussis = inimeste_arv % kohtade_arv

if viimases_bussis == 0:
    print("Busse vaja: " + str(busse_vaja))
    print("Viimases bussis inimesi: " + str(kohtade_arv))
else:
    print("Busse vaja: " + str(busse_vaja+1))
    print("Viimases bussis inimesi: " + str(viimases_bussis))