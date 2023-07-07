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
        'Amerikai Egyesült Államok': {
            'főváros': 'Washington',
            'terület': '9 826 675 km²',
            'népesség': '331 002 651',
            'zászló': 'USA.GIF'
        }
    }

    adatok_cimke.config(
        text=f'Ország: {orszag}\nFőváros: {orszag_adatok[orszag]["főváros"]}\nTerület: {orszag_adatok[orszag]["terület"]}\nNépesség: {orszag_adatok[orszag]["népesség"]}')

    # Zászló megjelenítése
    zaszlo_fajlnev = orszag_adatok[orszag]['zászló']
    zaszlo_kep = Image.open(zaszlo_fajlnev)
    zaszlo_kep = zaszlo_kep.resize((180, 120))
    zaszlo_tk = ImageTk.PhotoImage(zaszlo_kep)
    zaszlo_cimke.config(image=zaszlo_tk)
    zaszlo_cimke.image = zaszlo_tk


# Ablak létrehozása
ablak = tk.Tk()
ablak.title('Földrajzi adatok')
ablak.geometry('400x400')

# Zászló cimke
zaszlo_cimke = tk.Label(ablak)
zaszlo_cimke.pack()

# Gombok létrehozása
gomb_ausztria = tk.Button(ablak, text='Ausztria', compound=tk.BOTTOM,
                          command=lambda: mutasd_orszag_adatokat('Ausztria'))
gomb_ausztria.pack()

gomb_franciaorszag = tk.Button(ablak, text='Franciaország', compound=tk.BOTTOM,
                               command=lambda: mutasd_orszag_adatokat('Franciaország'))
gomb_franciaorszag.pack()

gomb_egyesult_kiralysag = tk.Button(ablak, text='Egyesült Királyság', compound=tk.BOTTOM,
                                    command=lambda: mutasd_orszag_adatokat('Egyesült Királyság'))
gomb_egyesult_kiralysag.pack()

gomb_magyarorszag = tk.Button(ablak, text='Magyarország', compound=tk.BOTTOM,
                              command=lambda: mutasd_orszag_adatokat('Magyarország'))
gomb_magyarorszag.pack()

gomb_usa = tk.Button(ablak, text='Amerikai Egyesült Államok', compound=tk.BOTTOM,
                     command=lambda: mutasd_orszag_adatokat('Amerikai Egyesült Államok'))
gomb_usa.pack()

# Címke adataink megjelenítéséhez
adatok_cimke = tk.Label(ablak, text='')
adatok_cimke.pack()

# Kilépés gomb
kilepes_gomb = tk.Button(ablak, text='Kilépés', command=ablak.quit)
kilepes_gomb.pack()

# Ablak megjelenítése
ablak.mainloop()
