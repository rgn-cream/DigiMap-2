import json
import os

# Nama file untuk database JSON
FILE_DATABASE = "data_pengguna.json"

# Fungsi untuk memuat data dari file JSON
def muat_data():
    if os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, "r") as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(FILE_DATABASE, "w") as file:
        json.dump(data, file, indent=4)

# Data pengguna (diambil dari file JSON)
data_pengguna = muat_data()

# Fungsi untuk menambahkan profil baru
def tambah_profil():
    username = input("Masukkan username: ")

    # Memastikan username belum terpakai
    if username in data_pengguna:
        print("Username sudah ada. Silakan pilih username lain.")
        return

    password = input("Masukkan password: ")
    nama = input("Masukkan nama: ")
    NIM = input("Masukkan NIM: ")
    kelas = input("Masukkan kelas: ")
    tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY): ")
    no_telepon = input("Masukkan no telepon: ")
    email = input("Masukkan email: ")

    # Menyimpan data ke dalam dictionary
    data_pengguna[username] = {
        "password": password,
        "profil": {
            "nama": nama,
            "NIM": NIM,
            "kelas": kelas,
            "tanggal_lahir": tanggal_lahir,
            "no_telepon": no_telepon,
            "email": email
        }
    }
    simpan_data(data_pengguna)  # Simpan data ke file JSON
    print("Profil berhasil ditambahkan!")

# Fungsi untuk menampilkan data profil pengguna
def tampilkan_data_pengguna(profil):
    print("=== Profil Pengguna ===")
    print(f"Nama: {profil['nama']}")
    print(f"NIM: {profil['NIM']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['tanggal_lahir']}")
    print(f"No Telepon: {profil['no_telepon']}")
    print(f"Email: {profil['email']}")

# Fungsi login dan tampilkan profil
def tampilkan_profil():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek apakah username dan password cocok
    if username in data_pengguna and data_pengguna[username]["password"] == password:
        print("Login berhasil!")
        tampilkan_data_pengguna(data_pengguna[username]["profil"])
    else:
        print("Username atau password salah.")

# Menu utama
def main():
    while True:
        print("=" * 40)
        print(" Menu ")
        print("=" * 40)
        print("1. Tambah Profil Baru ")
        print("2. Tampilkan Profil")
        print("3. Keluar")
        print("=" * 40)

        pilihan = input("Pilih opsi (1/2/3): ")
        print("=" * 40)

        if pilihan == "1":
            tambah_profil()
        elif pilihan == "2":
            tampilkan_profil()
        elif pilihan == "3":
            print("Terima kasih, sampai bertemu kembali :D ")
            break
        else:
            print("Error, silahkan coba lagi.")

# Jalankan program utama
main()
