import json
import os

# Nama file untuk database JSON
FILE_DATABASE = "data_login.json"

# Fungsi untuk memuat data dari file JSON
def muat_data():
    if os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, "r") as file:
            return json.load(file)
    return {"users": {}, "admin": {"username": "admin", "password": "admin123"}}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(FILE_DATABASE, "w") as file:
        json.dump(data, file, indent=4)

# Data pengguna (diambil dari file JSON)
data_pengguna = muat_data()

# Fungsi untuk menambahkan profil pengguna baru
def tambah_profil():
    username = input("Masukkan username: ")

    # Memastikan username belum terpakai
    if username in data_pengguna["users"]:
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
    data_pengguna["users"][username] = {
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

# Fungsi login admin
def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")

    # Verifikasi login admin
    if username == data_pengguna["admin"]["username"] and password == data_pengguna["admin"]["password"]:
        print("Login Admin berhasil!")
    else:
        print("Username atau password admin salah.")

# Fungsi login pengguna
def login_pengguna():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek apakah username dan password cocok
    if username in data_pengguna["users"] and data_pengguna["users"][username]["password"] == password:
        print("Login berhasil!")
        tampilkan_data_pengguna(data_pengguna["users"][username]["profil"])
    else:
        print("Username atau password salah.")

# Fungsi untuk submenu login pengguna
def menu_pengguna():
    while True:
        print("\n=== Login Pengguna ===")
        print("1. Login")
        print("2. Sign Up / Register")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            login_pengguna()
            break
        elif pilihan == "2":
            tambah_profil()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi login tamu
def login_tamu():
    print("=== Login Tamu ===")
    print("Halo, Tamu! Anda login sebagai pengguna tanpa profil.")

# Menu utama
def main():
    while True:
        print("\n" + "=" * 40)
        print(" Menu Utama ")
        print("=" * 40)
        print("1. Login Admin")
        print("2. Login Pengguna")
        print("3. Login Tamu")
        print("4. Keluar")
        print("=" * 40)

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            login_admin()
        elif pilihan == "2":
            menu_pengguna()
        elif pilihan == "3":
            login_tamu()
        elif pilihan == "4":
            print("Terima kasih, sampai bertemu kembali :D ")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Jalankan program utama
if __name__ == "__main__":
    simpan_data(data_pengguna) 
    main()
