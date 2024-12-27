import os, time, json
from fungsi import muat_data, simpan_data, validasi_tanggal_lahir, data_pengguna
from Profil_pengguna import tampilkan_profil, edit_profil
from admin import login_admin
from search import cari_jadwal
from denah import tampilkan_denah

#PENGGUNA====================================================================================================================================================================================
# Fungsi untuk menambahkan profil pengguna baru
def register():
    print("="*70)
    print("Form Register User DigiDenah")
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
            opsiRegister = str(input("Apakah anda ingin melakukan register? (Y/N): "))
            if opsiRegister.lower == "y":
                print("Anda akan di alihkan ke halaman register")
                time.sleep(2)
                os.system("cls")
                register()
            else:
                login_pengguna2()
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
    else:
        print("="*70)
        print("Username dan Password tidak Valid!")
        print("="*70)
        
        print("Tampilkan Profil Anda (Y/N)")
        tampilan = input("Y/N: ")
        if tampilan.lower() == "y":
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            
            profil = data_pengguna["users"][username]["profil"]
            
            tampilkan_profil(profil)
            while True:
                print("\nPilih opsi:")
                print("1. Edit Profil")
                print("2. Kembali ke Menu Utama")
                pilihan = input("Pilih opsi (1/2): ").strip()

                if pilihan == "1":
                    edit_profil(profil, username)
                    tampilkan_profil(profil)
                elif pilihan == "2":
                    menu_pengguna()
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                time.sleep(2)

        elif tampilan.lower() == "n":
            print("Anda akan dialihkan ke halaman menu utama")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            menu_pengguna()
        else:
            print("Pilihan Anda tidak tersedia. Silakan masukkan Y atau N.")

def login_pengguna2():
    login_pengguna()

def logout():
    print("\nAnda akan logout dari sesi saat ini...")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    print("Anda telah berhasil logout!\n")
    main()

# Fungsi untuk submenu login pengguna
def menu_login_pengguna():
    while True:
        print("\n")
        print("="*70)
        print("Menu Login Pengguna")
        print("="*70)
        print("1. Login")
        print("2. Sign Up / Register")
        pilihan = input("Pilih opsi (1/2/3): ")

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
        elif pilihan == "3":
            login_tamu()
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def load_jadwal_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def menu_pengguna():
    while True:
        print("===Menu Pengguna===")
        print("1. Lihat Denah")
        print("2. Cari Jadwal Kelas")
        print("3. Lihat Profil")
        print("4. Logout")

        opsi = int(input("Pilih opsi (1/2/3/4): "))
        if opsi == 1: 
            print("Denah UPI Cibiru")
            tampilkan_denah()
            print("Denah telah dibuat dan disimpan sebagai 'upi_cibiru.html'")
            continue
        elif opsi == 2:
            # Memuat jadwal dari file JSON
            jadwal = load_jadwal_from_json('data_jadwal.json')  
            cari_jadwal(jadwal)  
        elif opsi == 3:
            tampilkan_profil()    
        elif opsi == 4:
            logout()
            break
        else: 
            print("Pilihan tidak valid. Pastikan memilih (1/2/3/4)")

#TAMU=============================================================================================================================================================================================
def login_tamu():
    print("="*70)
    print("Tamu")
    print("="*70)
    print("Halo, Tamu! Anda login sebagai pengguna tanpa profil.")
    menu_tamu()

def masuk_tamu():
    print("\n")
    print("-"*70)
    print("Apakah anda ingin melakukan melakukan login atau register?")
    print("-"*70)
    pilihan = input("Pilih opsi (Y/N): ")
    if pilihan.lower() == "y":
        menu_login_pengguna()
    if pilihan.lower() == "n":
        print("Anda akan kembali ke menu")
        time.sleep(2)
        os.system("cls")
        menu_tamu()

def menu_tamu():
    print("\n")
    print("-"*70)
    print("Menu tamu")
    print("-"*70)
    print("1. Lihat Denah")
    print("2. Cari Jadwal Kelas")
    print("3. Lihat Profil")

    opsi = int(input("Pilih opsi (1/2/3/4): "))
    if opsi == 1: 
        print("Denah UPI Cibiru")
        tampilkan_denah()
        print("Denah telah dibuat dan disimpan sebagai 'upi_cibiru.html'")
    elif opsi == 2:
        print("\nAnda tidak dapat melihat jadwal. Silahkan melakukan login terlebih dahulu")
        masuk_tamu()
    elif opsi == 3:
        print("Profil tidak tersedia")
        masuk_tamu()
    elif opsi == 4:
        logout()
    else: 
        print("Pilihan tidak valid. Pastikan memilih (1/2/3/4)")

# Menu utama=====================================================================================================================================================================================
def main():
    while True:
        print("\n" + "=" * 40)
        print("Masuk sebagai")
        print("=" * 40)
        print("1. Admin")
        print("2. Pengguna")
        print("3. Tamu")
        print("4. Keluar")
        print("=" * 40)

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            print("Anda akan masuk sebagai admin, mohon tunggu sebentar")
            time.sleep(2)
            os.system("cls")
            login_admin()
        elif pilihan == "2":
            print("Anda akan dialihkan ke menu pengguna, mohon tunggu sebentar")
            time.sleep(2)
            os.system("cls")
            menu_login_pengguna()
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

main()
