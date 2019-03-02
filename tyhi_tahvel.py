from tkinter import *

raam = Tk()
raam.title('Tühi tahvel')

#loome tahvli laiusega 600 px
tahvel = Canvas(raam, width = 600, height = 600, background = 'red')

tahvel.create_line(50,350,100,350, width=4, fill="green",
arrow=LAST)

#paigutame tahvli raami ja teeme nähtavaks
tahvel.pack()

#siseneme põhitsüklisse
raam.mainloop()
