from model.daftar_nilai import tambah_data, hapus_data, ubah_data

def masukan_data():
    print("|=========================|")
    print("|==== Data Mahasiswa ==== |")
    print("|=========================|")
    print()
    nama = input(" Nama = ")
    nim = int(input(" NIM = "))
    tugas = int(input(" Nilai Tugas = "))
    uts = int(input(" Nilai UTS = "))
    uas = int(input(" Nilai UAS = "))
    akhir = float((0.30 * tugas) + (0.35 * uts) + (0.35 * uas))
    tambah_data(nama,nim,tugas,uts,uas,akhir)

def cari_hapus():
    hapus_data(input("Nama yang ingin di Hapus = "))

def cari_ubah():
    ubah_data(input("Nama Data yang ingin di Ubah = "))

    print("|============================|")
    print("|==== Data yang Di Ubah ==== |")
    print("|============================|")
    print()
    nama = input(" Nama = ")
    nim = int(input(" NIM = "))
    tugas = int(input(" Nilai Tugas = "))
    uts = int(input(" Nilai UTS = "))
    uas = int(input(" Nilai UAS = "))
    akhir = float((0.30 * tugas) + (0.35 * uts) + (0.35 * uas))
    tambah_data(nama, nim, tugas, uts, uas, akhir)

