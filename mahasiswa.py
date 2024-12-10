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
