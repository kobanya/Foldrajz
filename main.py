import tkinter as tk
from PIL import ImageTk, Image

def mutasd_orszag_adatokat(orszag):
    orszag_adatok = {
        'Ausztria': {
            'főváros': 'Bécs',
            'terület': '83 879 km²',
            'népesség': '8 900 000',
            'zászló': '/home/bela/Asztal/AT.GIF'
        },
        'Franciaország': {
            'főváros': 'Párizs',
            'terület': '551 695 km²',
            'népesség': '67 410 000',
            'zászló': '/home/bela/Asztal/FR.GIF'
        },
        'Egyesült Királyság': {
            'főváros': 'London',
            'terület': '242 500 km²',
            'népesség': '66 040 229',
            'zászló': '/home/bela/Asztal/GB.GIF'
        },
        'Magyarország': {
            'főváros': 'Budapest',
            'terület': '93 030 km²',
            'népesség': '9 769 000',
            'zászló': '/home/bela/Asztal/HU.GIF'
        },
        'Amerikai Egyesült Államok': {
            'főváros': 'Washington',
            'terület': '9 826 675 km²',
            'népesség': '331 002 651',
            'zászló': '/home/bela/Asztal/USA.GIF'
        }
    }

    adatok_cimke.config(text=f'Ország: {orszag}\nFőváros: {orszag_adatok[orszag]["főváros"]}\nTerület: {orszag_adatok[orszag]["terület"]}\nNépesség: {orszag_adatok[orszag]["népesség"]}')

# Ablak létrehozása
ablak = tk.Tk()
ablak.title('Földrajzi adatok')

# Gombok létrehozása és elhelyezése
gomb_ausztria = tk.Button(ablak, text='Ausztria', compound=tk.TOP)
gomb_ausztria.pack(side=tk.LEFT)

gomb_franciaorszag = tk.Button(ablak, text='Franciaország', compound=tk.TOP)
gomb_franciaorszag.pack(side=tk.LEFT)

gomb_egyesult_kiralysag = tk.Button(ablak, text='Egyesült Királyság', compound=tk.TOP)
gomb_egyesult_kiralysag.pack(side=tk.LEFT)

gomb_magyarorszag = tk.Button(ablak, text='Magyarország', compound=tk.TOP)
gomb_magyarorszag.pack(side=tk.LEFT)

gomb_usa = tk.Button(ablak, text='Amerikai Egyesült Államok', compound=tk.TOP)
gomb_usa.pack(side=tk.LEFT)

# Címke adataink megjelenítéséhez
adatok_cimke = tk.Label(ablak, text='')
adatok_cimke.pack()

# Zászlók hozzáadása a gombokhoz
zaszlo_ausztria = ImageTk.PhotoImage(Image.open('/home/bela/Asztal/AT.GIF').resize((180, 120)))
zaszlo_franciaorszag = ImageTk.PhotoImage(Image.open('/home/bela/Asztal/FR.GIF').resize((180, 120)))
zaszlo_egyesult_kiralysag = ImageTk.PhotoImage(Image.open('/home/bela/Asztal/GB.GIF').resize((180, 120)))
zaszlo_magyarorszag = ImageTk.PhotoImage(Image.open('/home/bela/Asztal/HU.GIF').resize((180, 120)))
zaszlo_usa = ImageTk.PhotoImage(Image.open('/home/bela/Asztal/USA.GIF').resize((180, 120)))

gomb_ausztria.config(image=zaszlo_ausztria, command=lambda: mutasd_orszag_adatokat('Ausztria'))
gomb_franciaorszag.config(image=zaszlo_franciaorszag, command=lambda: mutasd_orszag_adatokat('Franciaország'))
gomb_egyesult_kiralysag.config(image=zaszlo_egyesult_kiralysag, command=lambda: mutasd_orszag_adatokat('Egyesült Királyság'))
gomb_magyarorszag.config(image=zaszlo_magyarorszag, command=lambda: mutasd_orszag_adatokat('Magyarország'))
gomb_usa.config(image=zaszlo_usa, command=lambda: mutasd_orszag_adatokat('Amerikai Egyesült Államok'))

# Kilépés gomb
kilepes_gomb = tk.Button(ablak, text='Kilépés', command=ablak.quit)
kilepes_gomb.pack()

# Ablak megjelenítése
ablak.mainloop()