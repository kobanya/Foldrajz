import tkinter as tk
from PIL import ImageTk, Image

def mutasd_orszag_adatokat(orszag):
    orszag_adatok = {
        'Ausztria': {
            'főváros': 'Bécs',
            'terület': '83 879 km²',
            'népesség': '8 900 000',
            'zászló': 'AT.GIF'
        },
        'Franciaország': {
            'főváros': 'Párizs',
            'terület': '551 695 km²',
            'népesség': '67 410 000',
            'zászló': 'FR.GIF'
        },
        'Egyesült Királyság': {
            'főváros': 'London',
            'terület': '242 500 km²',
            'népesség': '66 040 229',
            'zászló': 'GB.GIF'
        },
        'Magyarország': {
            'főváros': 'Budapest',
            'terület': '93 030 km²',
            'népesség': '9 769 000',
            'zászló': 'HU.GIF'
        },
        'Németország': {
            'főváros': 'Berlin',
            'terület': '357 022 km²',
            'népesség': '83 149 300 fő',
            'zászló': 'N.png'
        }
    }

    adatok_cimke.config(text=f'Ország: {orszag}\nFőváros: {orszag_adatok[orszag]["főváros"]}\nTerület: {orszag_adatok[orszag]["terület"]}\nNépesség: {orszag_adatok[orszag]["népesség"]}')

    if orszag == "Magyarország":
        kep = ImageTk.PhotoImage(Image.open('hu_t.png').resize((450, 270)))
        terkep_cimke.config(image=kep)
        terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képetm memóriában tartjuk, hogy a Python ne kkukázza ki

    if orszag == "Ausztria":
        kep = ImageTk.PhotoImage(Image.open('at_t.png').resize((450, 270)))
        terkep_cimke.config(image=kep)
        terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képet

    if orszag == "Franciaország":
        kep = ImageTk.PhotoImage(Image.open('fr_t.png').resize((350, 290)))
        terkep_cimke.config(image=kep)
        terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képet

    if orszag == "Németország":
        kep = ImageTk.PhotoImage(Image.open('de_t.png').resize((270, 300)))
        terkep_cimke.config(image=kep)
        terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képet

    if orszag == "Egyesült Királyság":
        kep = ImageTk.PhotoImage(Image.open('gb_t.png').resize((270, 300)))
        terkep_cimke.config(image=kep)
        terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képet


# Ablak létrehozása
ablak = tk.Tk()
ablak.title('Földrajzi adatok')

# Felső keret a gomboknak
gomb_keret = tk.Frame(ablak)
gomb_keret.pack()

# Gombok létrehozása és elhelyezése
gomb_ausztria = tk.Button(gomb_keret, text='Ausztria', compound=tk.TOP)
gomb_ausztria.pack(side=tk.LEFT)

gomb_franciaorszag = tk.Button(gomb_keret, text='Franciaország', compound=tk.TOP)
gomb_franciaorszag.pack(side=tk.LEFT)

gomb_egyesult_kiralysag = tk.Button(gomb_keret, text='Egyesült Királyság', compound=tk.TOP)
gomb_egyesult_kiralysag.pack(side=tk.LEFT)

gomb_magyarorszag = tk.Button(gomb_keret, text='Magyarország', compound=tk.TOP)
gomb_magyarorszag.pack(side=tk.LEFT)

gomb_usa = tk.Button(gomb_keret, text='Németország', compound=tk.TOP)
gomb_usa.pack(side=tk.LEFT)

# Szövegmező és Térkép keret létrehozása
keret = tk.Frame(ablak)
keret.pack()

# Szövegmező létrehozása
adatok_cimke = tk.Label(keret, text='', width=30, height=10, anchor=tk.W, padx=10)

adatok_cimke.pack(side=tk.LEFT)

# Térkép címke létrehozása
terkep_cimke = tk.Label(keret, padx=10)
terkep_cimke.pack(side=tk.LEFT)

# Zászlók hozzáadása a gombokhoz
zaszlo_ausztria = ImageTk.PhotoImage(Image.open('AT.GIF').resize((180, 120)))
zaszlo_franciaorszag = ImageTk.PhotoImage(Image.open('FR.GIF').resize((180, 120)))
zaszlo_egyesult_kiralysag = ImageTk.PhotoImage(Image.open('GB.GIF').resize((180, 120)))
zaszlo_magyarorszag = ImageTk.PhotoImage(Image.open('HU.GIF').resize((180, 120)))
zaszlo_usa = ImageTk.PhotoImage(Image.open('N.png').resize((180, 120)))

gomb_ausztria.config(image=zaszlo_ausztria, command=lambda: mutasd_orszag_adatokat('Ausztria'))
gomb_franciaorszag.config(image=zaszlo_franciaorszag, command=lambda: mutasd_orszag_adatokat('Franciaország'))
gomb_egyesult_kiralysag.config(image=zaszlo_egyesult_kiralysag, command=lambda: mutasd_orszag_adatokat('Egyesült Királyság'))
gomb_magyarorszag.config(image=zaszlo_magyarorszag, command=lambda: mutasd_orszag_adatokat('Magyarország'))
gomb_usa.config(image=zaszlo_usa, command=lambda: mutasd_orszag_adatokat('Németország'))

# Kilépés gomb
kilepes_gomb = tk.Button(ablak, text='Kilépés', command=ablak.quit)
kilepes_gomb.pack(side=tk.BOTTOM, fill=tk.X)


# Ablak megjelenítése
ablak.mainloop()