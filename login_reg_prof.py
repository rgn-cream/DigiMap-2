import json
import os
import time

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

def validasi_tanggal_lahir(tanggal):
    try:
        # Pisahkan input
        hari, bulan, tahun = map(int, tanggal.split("-"))

        # Cek rentang nilai
        if 1 <= hari <= 31 and 1 <= bulan <= 12 and len(str(tahun)) == 4:
            return True
    except:
        pass  # Abaikan kesalahan jika input tidak sesuai
    return False
# Data pengguna (diambil dari file JSON)
data_pengguna = muat_data()

# Fungsi untuk menambahkan profil pengguna baru
def register():
    print("="*70)
    print("Form Register User DigiMap")
    print("="*70)

    username = input("Masukkan username: ")

    # Memastikan username belum terpakai
    if username in data_pengguna["users"]:
        print("Username sudah ada. Silakan pilih username lain.")
        return

    password = input("Masukkan password: ")
    nama = input("Masukkan nama: ")
    NIM = input("Masukkan NIM: ")
    kelas = input("Masukkan kelas: ")

    while True:
        tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY): ")
        if validasi_tanggal_lahir(tanggal_lahir):
            break
        print("Format tanggal lahir tidak valid. Gunakan format DD-MM-YYYY.")

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

    print("="*70)
    print("Profil berhasil ditambahkan!")
    print("="*70)

# Fungsi untuk menampilkan data profil pengguna
def tampilkan_profil(profil):
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
    print("="*70)
    print("LOGIN")
    print("="*70)
    print("Selamat Datang Kembali di DigiMap! Silahkan Masukkan Kredensial disini")
    print("-"*70)
    username = input("Masukkan Username   : ")
    password = input("Masukkan Password   : ")

    if username in data_pengguna["users"] and data_pengguna["users"][username]["password"] == password:
        print("="*70)
        print("Login Berhasil!")
        print("="*70)
        print("Tampilkan Profil Anda (Y/N)")
        tampilan = input("Y/N: ")
        if tampilan.lower() == "y":
            print("DEBUG: Data pengguna setelah login:", data_pengguna["users"][username])
        elif tampilan.lower() == "n":
            print("Anda akan kembali ke halaman utama")
        else:
            print("Pilihan Anda tidak tersedia")
        
    else:
        print("="*70)
        print("Username, NIM, atau Password tidak Valid!")
        print("="*70)
    
        opsi = input("Coba lagi?(Y/N) ")
        if opsi.lower() == "y":
            os.system("cls")
            login_pengguna()
        elif opsi.lower() == "n":
            time.sleep(2)
            print("Anda akan kembali ke halaman utama")
            #HALAMAN UTAMA
        else:
            print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
            time.sleep(2)
            os.system("cls")
            menu_pengguna()

# Fungsi untuk submenu login pengguna
def menu_pengguna():
    while True:
        print("\n=== Login Pengguna ===")
        print("1. Login")
        print("2. Sign Up / Register")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            print("Anda akan beralih ke form login, mohon tunggu sebentar")
            time.sleep(2)
            os.system("cls")
            login_pengguna()
            break
        elif pilihan == "2":
            print("Anda akan beralih ke form register, mohon tunggu sebentar")
            time.sleep(2)
            os.system("cls")
            register()
            time.sleep(2)
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi login tamu
def login_tamu():
    print("=== Login Tamu ===")
    print("Halo, Tamu! Anda login sebagai pengguna tanpa profil.")
    print("Sebagai tamu, anda tidak dapat melihat jadwal penggunaan kelas")

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
            print("Anda akan masuk sebagai admin, mohon tunggu sbeentar")
            time.sleep(2)
            os.system("cls")
            login_admin()
        elif pilihan == "2":
            print("Anda akan dialihkan ke menu pengguna, mohon tunggu sebentar")
            time.sleep(2)
            os.system("cls")
            menu_pengguna()
        elif pilihan == "3":
            print("Anda akan masuk sebagai tamu")
            time.sleep(2)
            os.system("cls")
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
