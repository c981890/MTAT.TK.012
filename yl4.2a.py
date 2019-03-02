from tkinter import *

raam = Tk()
raam.title = ('Võru lipp')

tahvel = Canvas(raam, width = 600, height = 300)
kitsa_osa_korgus = 60
laia_osa_korgus = 180
i = 0

tahvel.create_rectangle(0, 0, 600, 60, fill = 'yellow', outline = 'yellow')
tahvel.create_rectangle(0, 240, 600, 600, fill = 'yellow', outline = 'yellow')
tahvel.create_rectangle(0, 60, 600, 240, fill = 'green', outline = 'green')

#while i < 3:
#    if i == 0 or i == 2:
#        tahvel.create_rectangle(0, 0, 600, 60, fill = 'yellow', outline = 'yellow')
#        tahvel.create_rectangle(0, 240, 600, 600, fill = 'yellow', outline = 'yellow')
#    else:
#        tahvel.create_rectangle(0, 60, 600, (i + 1) * kitsa_osa_korgus, fill = 'green', outline = 'green')
#    i += 1

tahvel.pack()
raam.mainloop()
