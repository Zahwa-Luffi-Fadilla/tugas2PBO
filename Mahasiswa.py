from datetime import date

class Mahasiswa:
    def __init__(self, nama, nim, tanggal_lahir, alamat, tahun_masuk,):
        self.nama = nama
        self.nim = nim
        self.tanggal_lahir = tanggal_lahir
        self.alamat = alamat
        self.tahun_masuk = tahun_masuk
        

    # Getter
    def get_nama(self):
        return self.nama
    def get_nim(self):
        return self.nim

    def get_tahun_masuk(self):
        return self.tahun_masuk

    # Setter
    def set_tahun_masuk(self, tahun_baru):
        if tahun_baru <= date.today().year:
            self.tahun_masuk = tahun_baru
        else:
            print("Tahun masuk tidak valid!")

    def tampilkan_data(self):
        print("=== Data Mahasiswa ===")
        print("Nama          :", self.nama)
        print("NIM           :", self.nim)
        print("Tanggal Lahir :", self.tanggal_lahir)
        print("Alamat       :", self.alamat)
        print("Tahun Masuk   :", self.tahun_masuk)


    def hitung_umur(self):
        today = date.today()
        umur = today.year - self.tanggal_lahir.year
        if (today.month, today.day) < (self.tanggal_lahir.month, self.tanggal_lahir.day):
            umur -= 1
        return umur


# Contoh penggunaan
mhs1 = Mahasiswa(
    "Zahwa Luffi Fadilla",
    "12550120278",
    date(2006, 6, 11),
    "jalan Buluh Cina",
    2025
)

mhs1.tampilkan_data()
print("Umur:", mhs1.hitung_umur(), "tahun")

# Menggunakan setter
mhs1.set_tahun_masuk(2025)

# Menggunakan getter
print("Tahun Masuk (Getter):", mhs1.get_tahun_masuk())