# Data profil pengguna 
data_pengguna = {}

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
    print("Profil berhasil ditambahkan!")

# Fungsi untuk menampilkan data profil pengguna
def tampilkan_profil(profil):
    print("=== Profil Pengguna ===")
    print(f"Nama: {profil['nama']}")
    print(f"NIM: {profil['NIM']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['tanggal_lahir']}")
    print(f"No Telepon: {profil['no_telepon']}")
    print(f"Email: {profil['email']}")

# Fungsi login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Cek apakah username dan password cocok
    if username in data_pengguna and data_pengguna[username]["password"] == password:
        print("Login berhasil!")
        tampilkan_profil(data_pengguna[username]["profil"])
    else:
        print("Username atau password salah.")

# Menu utama
def main():
    while True:
        print("="*40)
        print(" Menu ")
        print("="*40)
        print("1. Tambah Profil Baru ")
        print("2. Tampilkan Profil")
        print("3. Keluar")
        print("="*40)
        
        pilihan = input("Pilih opsi (1/2/3): ")
        print("="*40)

        if pilihan == "1":
            tambah_profil()
        elif pilihan == "2":
            login()
        elif pilihan == "3":
            print("Terima kasih, sampai bertemu kembali :D ")
            break
        else:
            print("Error, silahkan coba lagi.")
            
main()
