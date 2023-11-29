from tkinter import *
from tkinter import messagebox
from Resztvevok import *

def Eredmenyek_kiirasa(lista):


    eredmenyek = Tk()
    eredmenyek.title("Versenyzők eredményei")

    Resztvevok_neve_cimke = Label(eredmenyek, text="Résztvevő neve")
    Resztvevok_gyozelmei_cimke = Label(eredmenyek, text="Részvevő győzelme")
    Resztvevok_veresegei_cimke = Label(eredmenyek, text="Részvevő veresége")
    Eredmenyek_cimke = Label(eredmenyek, text="Eredmények")

    Eredmenyek_cimke.grid(row=0, column=2, pady=50, padx=50, sticky=W)
    Resztvevok_neve_cimke.grid(row=1, column=1, pady=50, padx=50, sticky=W)
    Resztvevok_gyozelmei_cimke.grid(row=1, column=2, pady=50, padx=50, sticky=W)
    Resztvevok_veresegei_cimke.grid(row=1, column=3, pady=50, padx=50, sticky=W)

    lista.sort(key=lambda x: x.gyozelem_szam, reverse=True)

    b = 0
    while b < len(lista):

        R_nev_cimke = Label(eredmenyek, text=lista[b].nev)
        R_gyozelem_cimke = Label(eredmenyek, text=lista[b].gyozelem_szam)
        R_vereseg_cimke = Label(eredmenyek, text=lista[b].vereseg_szam)
        Helyezett_szam = Label(eredmenyek, text=str(b+1) + ". hely")

        Helyezett_szam.grid(row=b+2, column=0, pady=2, padx=10, sticky=N)
        R_nev_cimke.grid(row=b+2, column=1, pady=2, padx=2, sticky=N)
        R_gyozelem_cimke.grid(row=b+2, column=2, pady=2, padx=2, sticky=N)
        R_vereseg_cimke.grid(row=b+2, column=3, pady=2, padx=2, sticky=N)
        b += 1

    def lementes_gomb():
        eredmeny_text_file = open("Eredmények.txt", "w")
        i = 0
        while i < len(lista):
            eredmeny_text_file.write("Résztvevő neve: " + lista[i].nev + "\nRésztvevő helyezése: " + str(i+1) + ".hely" + "\nGyőzelmeinek száma: " + str(lista[i].gyozelem_szam) + "\nVereségeinek száma: " + str(lista[i].vereseg_szam) + "\n\n")
            i += 1
        eredmeny_text_file.close()

    def kilepes_gomb():
        messagebox.showinfo("", "Viszlát")
        eredmenyek.destroy()

    gomb_kilepes = Button(eredmenyek, text="Kilépés", command=kilepes_gomb)
    gomb_kilepes.grid(row=b+2, column=3, pady=20, padx=20)
    gomb_lementes = Button(eredmenyek, text="Eredmények lementése", command=lementes_gomb)
    gomb_lementes.grid(row=b+2, column=0, pady=20, padx=20)

    eredmenyek.mainloop()