import tkinter as tk
from PIL import ImageTk, Image

orszag_adatok = {
    'Ausztria': {
        'főváros': 'Bécs',
        'terület': '83 879 km²',
        'népesség': '8 900 000',
        'zászló': 'AT.GIF',
        'térkép': 'at_t.png',
        'térkép_méret': (400, 270)
    },
    'Franciaország': {
        'főváros': 'Párizs',
        'terület': '551 695 km²',
        'népesség': '67 410 000',
        'zászló': 'FR.GIF',
        'térkép': 'fr_t.png',
        'térkép_méret': (400, 270)
    },
    'Egyesült Királyság': {
        'főváros': 'London',
        'terület': '242 500 km²',
        'népesség': '66 040 229',
        'zászló': 'GB.GIF',
        'térkép': 'gb_t.png',
        'térkép_méret': (400, 270)
    },
    'Magyarország': {
        'főváros': 'Budapest',
        'terület': '93 030 km²',
        'népesség': '9 769 000',
        'zászló': 'HU.GIF',
        'térkép': 'hu_t.png',
        'térkép_méret': (400, 270)
    },
    'Németország': {
        'főváros': 'Berlin',
        'terület': '357 022 km²',
        'népesség': '83 149 300 fő',
        'zászló': 'N.png',
        'térkép': 'de_t.png',
        'térkép_méret': (250, 270)
    }
}


def mutasd_orszag_adatokat(orszag):
    fovezetek = ['Főváros:', 'Terület:', 'Népesség:']
    ertekek = [orszag_adatok[orszag]["főváros"], orszag_adatok[orszag]["terület"], orszag_adatok[orszag]["népesség"]]
    adatok = [f"{cim:<10} {ertek}" for cim, ertek in zip(fovezetek, ertekek)]
    adatok_cimke.config(text='\n'.join(adatok))

    kep = ImageTk.PhotoImage(Image.open(orszag_adatok[orszag]['térkép']).resize(orszag_adatok[orszag]['térkép_méret']))
    terkep_cimke.config(image=kep)
    terkep_cimke.image = kep


# Ablak létrehozása
ablak = tk.Tk()
ablak.title('Földrajzi adatok')

# Felső keret a gomboknak
gomb_keret = tk.Frame(ablak)
gomb_keret.pack()

# Gombok létrehozása és elhelyezése
gombok = []
for orszag in ['Ausztria', 'Franciaország', 'Egyesült Királyság', 'Magyarország', 'Németország']:
    zaszlo_kep = ImageTk.PhotoImage(Image.open(orszag_adatok[orszag]['zászló']).resize((60, 40)))
    gomb = tk.Button(gomb_keret, text=orszag, compound=tk.TOP, image=zaszlo_kep,
                     command=lambda o=orszag: mutasd_orszag_adatokat(o), activebackground="grey")
    gomb.pack(side=tk.LEFT)
    gomb.image = zaszlo_kep
    gombok.append(gomb)

# Szövegmező és Térkép keret létrehozása
keret = tk.Frame(ablak)
keret.pack()

# Szövegmező létrehozása
adatok_cimke = tk.Label(keret, text='', width=30, height=10, anchor=tk.W, padx=10, justify=tk.LEFT)
adatok_cimke.pack(side=tk.LEFT)

# Térkép címke létrehozása
terkep_cimke = tk.Label(keret, padx=10)
terkep_cimke.pack(side=tk.LEFT)

# Kilépés gomb
kilepes_gomb = tk.Button(ablak, text='Kilépés', command=ablak.quit)
kilepes_gomb.pack(side=tk.BOTTOM, fill=tk.X)

# Ablak megjelenítése
ablak.mainloop()
