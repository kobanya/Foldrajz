import tkinter as tk
from PIL import ImageTk, Image

def mutasd_orszag_adatokat(orszag):
    orszag_adatok = {
        'Ausztria': {
            'főváros': 'Bécs',
            'terület': '83 879 km²',
            'népesség': '8 900 000',
            'zászló': 'AT.GIF',
            'térkép': 'at_t.png'
        },
        'Franciaország': {
            'főváros': 'Párizs',
            'terület': '551 695 km²',
            'népesség': '67 410 000',
            'zászló': 'FR.GIF',
            'térkép': 'fr_t.png'
        },
        'Egyesült Királyság': {
            'főváros': 'London',
            'terület': '242 500 km²',
            'népesség': '66 040 229',
            'zászló': 'GB.GIF',
            'térkép': 'gb_t.png'
        },
        'Magyarország': {
            'főváros': 'Budapest',
            'terület': '93 030 km²',
            'népesség': '9 769 000',
            'zászló': 'HU.GIF',
            'térkép': 'hu_t.png'
        },
        'Németország': {
            'főváros': 'Berlin',
            'terület': '357 022 km²',
            'népesség': '83 149 300 fő',
            'zászló': 'N.png',
            'térkép': 'de_t.png'
        }
    }

    adatok_cimke.config(text=f'Ország: {orszag}\nFőváros: {orszag_adatok[orszag]["főváros"]}\nTerület: {orszag_adatok[orszag]["terület"]}\nNépesség: {orszag_adatok[orszag]["népesség"]}')

    kep = ImageTk.PhotoImage(Image.open(orszag_adatok[orszag]['térkép']).resize((450, 270)))
    terkep_cimke.config(image=kep)
    terkep_cimke.image = kep  # Fontos, hogy elmentjük a referencia képet

# Ablak létrehozása
ablak = tk.Tk()
ablak.title('Földrajzi adatok')

# Felső keret a gomboknak
gomb_keret = tk.Frame(ablak)
gomb_keret.pack()

# Gombok létrehozása és elhelyezése
gomb_ausztria = tk.Button(gomb_keret, text='Ausztria', compound=tk.TOP, command=lambda: mutasd_orszag_adatokat('Ausztria'))
gomb_ausztria.pack(side=tk.LEFT)

gomb_franciaorszag = tk.Button(gomb_keret, text='Franciaország', compound=tk.TOP, command=lambda: mutasd_orszag_adatokat('Franciaország'))
gomb_franciaorszag.pack(side=tk.LEFT)

gomb_egyesult_kiralysag = tk.Button(gomb_keret, text='Egyesült Királyság', compound=tk.TOP, command=lambda: mutasd_orszag_adatokat('Egyesült Királyság'))
gomb_egyesult_kiralysag.pack(side=tk.LEFT)

gomb_magyarorszag = tk.Button(gomb_keret, text='Magyarország', compound=tk.TOP, command=lambda: mutasd_orszag_adatokat('Magyarország'))
gomb_magyarorszag.pack(side=tk.LEFT)

gomb_nemetorszag = tk.Button(gomb_keret, text='Németország', compound=tk.TOP, command=lambda: mutasd_orszag_adatokat('Németország'))
gomb_nemetorszag.pack(side=tk.LEFT)

# Szövegmező és Térkép keret létrehozása
keret = tk.Frame(ablak)
keret.pack()

# Szövegmező létrehozása
adatok_cimke = tk.Label(keret, text='', width=30, height=10, anchor=tk.W, padx=10)
adatok_cimke.pack(side=tk.LEFT)

# Térkép címke létrehozása
terkep_cimke = tk.Label(keret, padx=10)
terkep_cimke.pack(side=tk.LEFT)

# Kilépés gomb
kilepes_gomb = tk.Button(ablak, text='Kilépés', command=ablak.quit)
kilepes_gomb.pack(side=tk.BOTTOM, fill=tk.X)

# Ablak megjelenítése
ablak.mainloop()
