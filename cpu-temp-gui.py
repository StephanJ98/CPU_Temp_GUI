from tkinter import Tk, Label
import os

COLOR = "#aaaaaa"
WINDOWSIZE = "180x50"

def get_temp():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    temp = float(temp)/1000
    champ_label["text"] = "  CPU Temp = " + str(temp) + " ºC"
    if temp < 30:
        champ_label2["text"] = "Cold"
        champ_label2["fg"] = "blue"
    elif temp > 60:
        champ_label2["text"] = "Hot"
        champ_label2["fg"] = "red"
    else:
        champ_label2["text"] = "Good"
        champ_label2["fg"] = "green"
    champ_label.after(1000, get_temp)

fenetre = Tk()
champ_label = Label(fenetre, text="Start", fg="white", bg=COLOR)
champ_label2 = Label(fenetre, text="OK", fg="black", bg=COLOR)
fenetre.title("CPU Temp GUI")
fenetre.geometry(WINDOWSIZE)
fenetre.configure(bg=COLOR)
champ_label.grid()
champ_label2.grid()
champ_label.after(1, get_temp)
fenetre.mainloop()