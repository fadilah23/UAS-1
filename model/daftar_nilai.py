
data = {}

def tambah_data(nama, nim, tugas, uts, uas, akhir):
    data[nama] = nama, nim, tugas, uts, uas, akhir

def hapus_data(nama):
    if nama in data.keys():
        del data[nama]
        print(f'Data Nama {nama} dihapus!!!')
        return True
    else:
        print(f'Data Nama {nama} Tidak Ditemukan!!!')
        return False

def ubah_data(nama):
    if nama in data.keys():
        del data[nama]


def cari_data():
    from view.view_nilai import cari
    cari(input("  Nama yang akan di Cari = "))