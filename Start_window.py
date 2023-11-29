from tkinter import *
from tkinter import messagebox
from Resztvevok import Resztvevok
from egyes import Eredmenyek_kiirasa

def Turnament_nev_megadas():
    turnament = Tk()
    turnament.title("Bajnokság")

    Turnament_neve_cimke = Label(turnament, text="Kérem írja be a Bajnokság nevét: ")

    Tn = StringVar()
    Tn.set("")
    Turnament_neve = Entry(turnament, textvariable=Tn, width=50)

    def ok_gomb():
        Turnament_nev = Turnament_neve.get()
        turnament.destroy()
        Resztvevok_megadasa(Turnament_nev)

    def kilepes_gomb():
        messagebox.showinfo("", "Viszlát!")
        turnament.destroy()

    gomb_ok = Button(turnament, text="OK", command=ok_gomb)
    gomb_kilepes =Button(turnament, text="Kilépés", command=kilepes_gomb)

    Turnament_neve_cimke.grid(row=0, column=0, pady=20, padx=10, sticky=E)
    Turnament_neve.grid(row=0, column=1, padx=10, sticky=W)

    gomb_ok.grid(row=2, column=0, pady=20)
    gomb_kilepes.grid(row=2, column=1)

    turnament.mainloop()

def Resztvevok_megadasa(T_nev):
    resztvevok = Tk()
    resztvevok.title(T_nev)

    Resztvevok_cimke = Label(resztvevok, text=T_nev)
    Resztvevok_szama = Label(resztvevok, text="Kérem adja meg a Résztvevők számát: ")

    Rn = IntVar()
    resztvevok_szama = Entry(resztvevok, textvariable=Rn, width=20)

    def resztvevo_hozzaadas_gomb():
        rsz = resztvevok_szama.get()
        resztvevok_szam = int(rsz)
        resztvevok.destroy()
        Resztvevok_neve_megadas(resztvevok_szam)

    def kilepes_gomb():
        messagebox.showinfo("", "Viszlát")
        resztvevok.destroy()

    gomb_resztvevo_hozzaadas = Button(resztvevok, text="Hozzáadás", command=resztvevo_hozzaadas_gomb)
    gomb_kilepes = Button(resztvevok, text="Kilépés", command=kilepes_gomb)

    Resztvevok_cimke.grid(row=0, column=0, pady=50, padx=50, sticky=E)
    Resztvevok_szama.grid(row=1, column=0, pady=20, padx=10, sticky=E)
    resztvevok_szama.grid(row=1, column=1, pady=20, padx=10, sticky=E)

    gomb_resztvevo_hozzaadas.grid(row=3, column=0, pady=20, padx=20)
    gomb_kilepes.grid(row=3, column=3, pady=20, padx=20)

    resztvevok.mainloop()

def Resztvevok_neve_megadas(resztvevok_szam):
    Resztvevok_adatok = []
    list = []  # Résztvevők neve
    list1 = []  # Részvevők győzelmeinek száma
    list2 = []  # Strinvar vereségeinek száma

    resztvevok = Tk()
    resztvevok.title("Részvevők neve, győzelmei, vereségei")

    r_n_cimke = Label(resztvevok, text="Résztvevő neve: ")
    r_n_cimke.grid(row=0, column=0, pady=10, padx=10, sticky=W)
    r_gy_cimke = Label(resztvevok, text="Résztvevő győzelmeinek száma: ")
    r_gy_cimke.grid(row=0, column=1, pady=10, padx=10, sticky=W)
    r_v_cimke = Label(resztvevok, text="Résztvevő vereségeinek száma: ")
    r_v_cimke.grid(row=0, column=2, pady=10, padx=10, sticky=W)

    i = 0
    while i < int(resztvevok_szam):
        list.append(str(i))
        list1.append(str(i))
        list2.append(str(i))
        i += 1

    x = 0
    while x < int(resztvevok_szam):
        rn = StringVar()
        rn.set("")
        list[x] = Entry(resztvevok, textvariable=rn, width=50)
        list[x].grid(row=x+1, column=0, pady=10, padx=10, sticky=W)

        rgy = IntVar()
        rgy.set(0)
        list1[x] = Entry(resztvevok, textvariable=rgy, width=5)
        list1[x].grid(row=x+1, column=1, pady=10, padx=10, sticky=W)

        rv = IntVar()
        rv.set(0)
        list2[x] = Entry(resztvevok, textvariable=rv, width=5)
        list2[x].grid(row=x+1, column=2, pady=10, padx=10, sticky=W)

        x += 1

    def hozzaad_gomb():
        a = 0
        while a < resztvevok_szam:
            nev = list[a].get()
            gyozelem = list1[a].get()
            vereseg = list2[a].get()
            Resztvevok_adatok.append(Resztvevok(nev,gyozelem,vereseg))
            a += 1

        messagebox.showinfo("", "Résztvevők neve, győzelmei, vereségei hozzáadva.")
        resztvevok.destroy()
        Eredmenyek_kiirasa(Resztvevok_adatok)

    def kilepes_gomb():
        resztvevok.destroy()

    gomb_hozzaad = Button(resztvevok, text="Hozzáad", command=hozzaad_gomb)
    gomb_hozzaad.grid(row=x+2, column=0, pady=20, padx=10)
    gomb_kilepes = Button(resztvevok, text="Kilépés", command=kilepes_gomb)
    gomb_kilepes.grid(row=x+2, column=3, pady=20, padx=10)


    resztvevok.mainloop()

Turnament_nev_megadas()