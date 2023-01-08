from model.daftar_nilai import data
from tabulate import tabulate

def cetak( ):
    print(tabulate(data.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"], tablefmt="heavy_grid"))

def cari(nama):
    cari_data = {}
    for key, value in data.items():
        if nama in value:
            cari_data[key] = value

    print(tabulate(cari_data.values(), headers=["NAMA", "NIM", "TUGAS", "UTS", "UAS", "AKHIR"], tablefmt="heavy_grid"))

