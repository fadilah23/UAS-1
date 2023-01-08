
while True:
    print("=================")
    print("====Data Menu====")
    print("=================")
    print()
    print("a. Tambah Data")
    print("b. Ubah Data")
    print("c. Hapus Data")
    print("d. Cari Data")
    print("e. Cetak Semua Data")
    print("f. Keluar")
    print()
    Menu = input("Silakan Pilih Menu = ")

    if Menu == 'a':
        from view.input_nilai import masukan_data
        masukan_data()

    elif Menu == 'b':
        from view.input_nilai import cari_ubah
        cari_ubah()

    elif Menu == 'c':
        from view.input_nilai import cari_hapus
        cari_hapus()

    elif Menu == 'd':
        from model.daftar_nilai import cari_data
        cari_data()

    elif Menu == 'e':
        from view.view_nilai import cetak
        cetak()

    elif Menu == 'f':
        print(" Sekian & Terima Kasih Telah Belajar Program Ini!!!")
        break

    else:
        print("Masukan Pilihan menu yang benar ")
