import json
import os
import time

FILE_DATABASE = "data_login.json"

# Fungsi untuk memuat data dari file JSON
def muat_data():
    if os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, "r") as file:
            return json.load(file)
    #return {"users": {}, "admin": {"username": "admin", "password": "admin123"}}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(FILE_DATABASE, "w") as file:
        json.dump(data, file, indent=4)

def validasi_tanggal_lahir(tanggal):
    try:
        if not isinstance(tanggal, str):
            return False
        if len(tanggal) != 10 or tanggal[2] != "-" or tanggal[5] != "-":
            return False
        hari, bulan, tahun = tanggal.split("-")
        if not (hari.isdigit() and bulan.isdigit() and tahun.isdigit()):
            return False
        hari, bulan, tahun = int(hari), int(bulan), int(tahun)
        if not (1 <= hari <= 31 and 1 <= bulan <= 12 and len(str(tahun)) == 4):
            return False
        if bulan in [4, 6, 9, 11] and hari > 30:
            return False
        if bulan == 2:
            if (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
                if hari > 29:
                    return False
            else:
                if hari > 28:
                    return False
        return True
    except:
        return False

data_pengguna = muat_data()

# Fungsi untuk menambahkan profil pengguna baru
def register():
    print("="*70)
    print("Form Register User DigiMap")
    print("="*70)

    while True:
        username = input("Masukkan username: ").strip()
        if username in data_pengguna.get("users", {}):
            print("Username sudah ada. Silakan masukkan username lain.")
            continue
        elif not username:
            print("Username tidak boleh kosong.")
            continue
        elif len(username) > 15:
            print("Username maksimal terdiri dari 15 karakter.")
            continue
        break

    while True:
        password = input("Masukkan password (8 karakter): ").strip()
        if not password:
            print("Password tidak boleh kosong.")
            continue
        elif len(password) < 8:
            print("Password harus terdiri dari 8 karakter")
            continue 

        has_letter = False
        has_digit = False
        
        for char in password:
            if char.isalpha():
                has_letter = True
            elif char.isdigit():
                has_digit = True
        
        if not has_letter or not has_digit:
            print("Password harus terdiri atas huruf dan angka.")
            continue
        
        break

    while True:
        nama = input("Masukkan nama: ").strip()
        if not nama:
            print("Nama tidak boleh kosong.")
            continue
        elif len(nama) > 20:
            print("Nama maksimal terdiri dari 20 karakter.")
            continue
        elif not all(c.isalpha() or c.isspace() for c in nama):
            print("Nama harus berupa huruf.")
            continue
        break

    while True:
        NIM = input("Masukkan NIM (7 digit): ").strip()
        if not NIM:
            print("NIM tidak boleh kosong.")
            continue
        elif not NIM.isdigit() or len(NIM) != 7:
            print("NIM harus berupa angka 7 digit.")
            continue
        elif NIM in data_pengguna.get("NIM", {}):
            print("NIM sudah terdaftar, pastikan NIM yang Anda masukkan sudah tepat.")
            continue
        break

    while True:
        kelas = input("Masukkan kelas (contoh: RPL 1B): ").strip()
        if not kelas:
            print("Kelas tidak boleh kosong.")
            continue
        try:
            bagian = kelas.split()
            if len(bagian) != 2:
                raise ValueError
            program, subkelas = bagian
            if program.upper() not in ["RPL", "TEKKOM", "PGPAUD", "PGSD", "PMM"]:
                raise ValueError
            if program.upper() == "RPL" or program.upper() == "TEKKOM":
                if subkelas[:-1].isdigit() and int(subkelas[:-1]) in range(1, 8) and subkelas[-1].upper() in ["A", "B", "C"]:
                    break
                else:
                    raise ValueError
            else:
                if subkelas[:-1].isdigit() and int(subkelas[:-1]) in range(1, 8) and subkelas[-1].upper() in ["A", "B", "C", "D", "E", "F"]:
                    break
                else:
                    raise ValueError
        except ValueError:
            print("Kelas tidak valid. Pastikan format dan program sesuai dengan aturan.")
            continue

    while True:
        tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY): ").strip()
        if not validasi_tanggal_lahir(tanggal_lahir):
            print("Format tanggal lahir tidak valid. Gunakan format DD-MM-YYYY.")
            continue
        break

    while True:
        no_telepon = input("Masukkan no telepon (10-13 digit): ").strip()
        if not no_telepon:
            print("Nomor telepon tidak boleh kosong.")
            continue
        elif not no_telepon.isdigit() or not (10 <= len(no_telepon) <= 13):
            print("Nomor telepon harus berupa angka dengan panjang 10-13 digit.")
            continue
        break

    while True:
        email = input("Masukkan email (ex:nama@gmail.com/@upi.edu): ").strip()
        
        if not email:
            print("Email tidak boleh kosong.")
            continue
        elif email.count("@gmail.com") != 1 and email.count("@upi.edu") != 1:
            print("Format email tidak valid. Pastikan email yang dimasukkan sesuai dengan format @gmail.com atau @upi.edu.")
            continue
        
        # Memastikan hanya satu dari dua domain yang ada
        if email.count("@gmail.com") > 1 or email.count("@upi.edu") > 1:
            print("Format email tidak valid. Pastikan email yang dimasukkan hanya memiliki satu domain.")
            continue 
        break

    # Simpan data pengguna
    data_pengguna.setdefault("users", {})[username] = {
        "password": password,
        "profil": {
            "nama": nama,
            "NIM": NIM,
            "kelas": kelas,
            "tanggal_lahir": tanggal_lahir,
            "no_telepon": no_telepon,
            "email": email,
        },
    }
    simpan_data(data_pengguna)

    print("=" * 70)
    print("Profil berhasil ditambahkan!")
    print("=" * 70)

    print("\nAnda akan beralih ke halaman login. Mohon tunggu sebentar...")
    time.sleep(2)
    os.system("cls")
    login_pengguna()

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

    # Load data pengguna dari file JSON
    data_pengguna = muat_data()

    while True:
        username = input("Masukkan Username   : ")
        if username not in data_pengguna["users"]:
            print("Username tidak tersedia")
            print("Anda akan di alihkan ke halaman register")
            time.sleep(2)
            os.system("cls")
            register()
            continue
        break 

    while True: 
        password = input("Masukkan Password   : ")
        if data_pengguna["users"][username]["password"] != password:
            print("Password anda salah. Pastikan password yang dimasukkan sesuai")
            continue
        break

    if username in data_pengguna["users"] and data_pengguna["users"][username]["password"] == password:
        print("="*70)
        print("Login Berhasil!")
        print("="*70)
        
        print("Tampilkan Profil Anda (Y/N)")
        tampilan = input("Y/N: ")
        if tampilan.lower() == "y":
            time.sleep(2)
            os.system("cls")
            os.system("cls" if os.name == "nt" else "clear")
            tampilkan_profil(data_pengguna["users"][username]["profil"])
            time.sleep(2)
        elif tampilan.lower() == "n":
            print("Anda akan kembali ke halaman utama")
            menu_pengguna()
        else:
            print("Pilihan Anda tidak tersedia. Silakan masukkan Y atau N.")

        
    else:
        print("="*70)
        print("Username dan Password tidak Valid!")
        print("="*70)

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
            time.sleep(2)
        elif pilihan == "4":
            print("Terima kasih, sampai bertemu kembali :D ")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

main()
