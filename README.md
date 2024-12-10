## Nama    :Mochamad Nabil Kurnia
## Kelas   :TI.24.A4
## NIM     : 312410307
## Matkul  : Bahasa Pemrograman


# Latihan 1

![Screenshot 2024-12-10 185634](https://github.com/user-attachments/assets/6b28317a-58a9-4786-94ba-2d0bf4a5ee20)

kode program
## data/mahasiswa.py
```python
class DaftarNilaiMahasiswa:
    def __init__(self):
        # Inisialisasi data mahasiswa
        self.daftar_nilai_mahasiswa = {}

    def tambah_data(self):
        print("\nTambahkan Data:")
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        try:
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
        except ValueError:
            print("Harap masukkan angka yang valid.")
            return 

        self.daftar_nilai_mahasiswa[nama] = (nim, tugas, uts, uas)
        print(f"Data {nama} berhasil ditambahkan.")

    def hapus_data(self):
        nama = input("Masukkan Nama: ")
        if nama in self.daftar_nilai_mahasiswa:
            del self.daftar_nilai_mahasiswa[nama]
            print(f"Data {nama} telah dihapus.")
        else:
            print(f"Data {nama} tidak ditemukan.")

    def ubah_data(self):
        nama = input("Masukkan Nama: ")
        if nama in self.daftar_nilai_mahasiswa:
            try:
                tugas_baru = float(input(f"Masukkan nilai tugas baru untuk {nama}: "))
                uts_baru = float(input(f"Masukkan nilai UTS baru untuk {nama}: "))
                uas_baru = float(input(f"Masukkan nilai UAS baru untuk {nama}: "))
            except ValueError:
                print("Harap masukkan angka yang valid.")
                return

            nim = self.daftar_nilai_mahasiswa[nama][0]  # Ambil NIM yang sudah ada
            self.daftar_nilai_mahasiswa[nama] = (nim, tugas_baru, uts_baru, uas_baru)
            print(f"Data {nama} berhasil diubah.")
        else:
            print(f"Data {nama} tidak ditemukan.")
````

Class DaftarNilaiMahasiswa:

__init__: Menyimpan data mahasiswa dalam bentuk dictionary.
tambah_data(): Menambahkan data baru berdasarkan input pengguna.
tampilkan_data(): Menampilkan semua data mahasiswa dalam format tabel sederhana.
hapus_data(): Menghapus data mahasiswa berdasarkan nama.
ubah_data(): Mengubah nilai tugas, UTS, dan UAS mahasiswa.

## view/input.from
```python
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
````

## view/mahasiswa.py
```python
class ViewMahasiswa:
    def tampilkan_data(daftar_nilai_mahasiswa):
        if not daftar_nilai_mahasiswa:
            print("\nTidak ada data untuk ditampilkan.")
            return

        print("\nDaftar Nilai Mahasiswa:")
        print("Nama\t\tNIM\t\tTugas\tUTS\tUAS")
        for nama, (nim, tugas, uts, uas) in daftar_nilai_mahasiswa.items():
            print(f"{nama}\t{nim}\t{tugas}\t{uts}\t{uas}")

    def tampilkan_pesan(pesan):
        print(pesan)
````

## main.py
```python
from data.mahasiswa import DaftarNilaiMahasiswa

# Inisialisasi objek
daftar_nilai = DaftarNilaiMahasiswa()

while True:
    print("\nMenu:")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Hapus data")
    print("4. Ubah data")
    print("5. Keluar")

    pilihan = input("Masukkan angka (1-5): ")

    if pilihan == "1":
        daftar_nilai.tambah_data()
    elif pilihan == "2":
        if not daftar_nilai.daftar_nilai_mahasiswa:
            print("Belum ada data.")
        else:
            print("\nDaftar Nilai Mahasiswa:")
            for nama, (nim, tugas, uts, uas) in daftar_nilai.daftar_nilai_mahasiswa.items():
                print(f"Nama: {nama}, NIM: {nim}, Tugas: {tugas}, UTS: {uts}, UAS: {uas}")
    elif pilihan == "3":
        daftar_nilai.hapus_data()
    elif pilihan == "4":
        daftar_nilai.ubah_data()
    elif pilihan == "5":
        break
    else:
        print("Pilihan tidak valid.")
````

# hasil program
![Screenshot 2024-12-10 195609](https://github.com/user-attachments/assets/0acb6f52-9a1e-4bde-812d-a93ded8d8564)![Screenshot 2024-12-10 185634](https://github.com/user-attachments/assets/c235b96e-f667-4085-a0a7-3e5a13f22097)

![Screenshot 2024-12-10 202118](https://github.com/user-attachments/assets/6eef21f8-7287-4b45-9e0c-70973508e741)

![Screenshot 2024-12-10 202131](https://github.com/user-attachments/assets/fc02533c-5307-49bf-9c03-65b23dd84493)


