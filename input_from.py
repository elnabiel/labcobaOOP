class InputForm:
    def input_data():
        print("\nTambahkan Data:")
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        try:
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
        except ValueError:
            print("Harap masukkan angka yang valid.")
            return None
        return nama, nim, tugas, uts, uas

    def input_ubah_data():
        print("\nUbah Data:")
        nama = input("Masukkan Nama: ")
        try:
            tugas_baru = float(input("Nilai Tugas Baru: "))
            uts_baru = float(input("Nilai UTS Baru: "))
            uas_baru = float(input("Nilai UAS Baru: "))
        except ValueError:
            print("Harap masukkan angka yang valid.")
            return None
        return nama, tugas_baru, uts_baru, uas_baru

    def input_hapus_data():
        print("\nHapus Data:")
        return input("Masukkan Nama: ")
