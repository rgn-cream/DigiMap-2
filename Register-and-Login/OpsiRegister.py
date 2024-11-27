import os, time, json

def load_data():
    if os.path.exists("D:\\DIGIMAP\\Register-and-Login\\Data.json"): 
        file = open("D:\\DIGIMAP\\Register-and-Login\\Data.json")
        data = json.load(file)
        file.close()
        return data 
    else:
        return{}
    
def save_data(data):
    with open("D:\\DIGIMAP\\Register-and-Login\\Data.json", "w") as file:
        json.dump(data, file, indent=4)
    
def login_user(): 
    print("="*70)
    print("LOGIN")
    print("="*70)
    print("Selamat Datang Kembali di DigiMap! Silahkan Masukkan Kredensial disini")
    print("-"*70)
    username = input("Masukkan Username   : ")
    nim = input("Masukkan NIM        : ")
    password = input("Masukkan Password   : ")

    data = load_data()
    user_data = data.get(username)

    if user_data and user_data["NIM"] == nim and user_data["password"] == password:
        time.sleep(2)
        print("="*70)
        print("Login Berhasil!")
        print("="*70)
        
    else:
        print("="*70)
        print("Username, NIM, atau Password tidak Valid!")
        print("="*70)
    
        opsi = input("Coba lagi?(Y/N) ")
        if opsi.lower() == "y":
            os.system("cls")
            login_user()
        elif opsi.lower() == "n":
            time.sleep(2)
            print("Anda akan kembali ke halaman utama")
            #HALAMAN UTAMA
        else:
            print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
            time.sleep(2)
            os.system("cls")
            mulai()

    tampilkan_profil()


def register():
    print("="*70)
    print("Form Register User DigiMap")
    print("="*70)
    nama = input("Masukkan Nama Anda : ")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan password : ")
    nim = input("Masukkan NIM : ")
    kelas = input("Masukkan kelas : ")
    ttl = input("Masukkan tanggal lahir (tgl-bulan-tahun) : ")
    email = input("Masukkan email : ")

    data = load_data()
    
    if username in data:
        print("\nUsername sudah terdaftar, silakan gunakan username lain.")
        return

    data[username] = {
        "nama": nama,
        "NIM": nim,
        "password": password,
        "Kelas": kelas, 
        "TTL": ttl,
        "email":email
    }

    save_data(data)
    print("\nData Berhasil Disimpan")

    tampilkan_profil()

def load_profil():
    with open("D:\\DIGIMAP\\Register-and-Login\\Data.json", "r") as file:
        data = json.load(file)
    return data

def tampilkan_profil():
    print("Tampilkan Profil Anda (Y/N)")
    tampilan = input ("Y/N: ")
    if tampilan.lower() == "y":
        get_profil()
    elif tampilan.lower() == "n" :
        print("Anda akan kembali ke halaman utama")
    else:
        print("Pilihan anda tidak tersedia")

def get_profil():  
    profil = load_profil 
    print("=== Profil Pengguna ===")
    print(f"Nama: {profil['nama']}")
    print(f"Username: {profil['username']}")
    print(f"NIM: {profil['nim']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['ttl']}")
    print(f"Email: {profil['email']}")
    mulai()

def mulai():
    print("="*70)
    print("Selamat Datang di DIGIMAP!")
    print("="*70)
    print("\n Apakah anda sudah mempunyai akun?")

    akun = input ("Y/N : ")
    
    if akun.lower() == "y":
        os.system("cls")
        login_user()
    elif akun.lower() == "n":
        os.system("cls")
        print("="*70)
        print("Buat akun ? ")
        print("="*70)
        print ("1. Buat akun (Registrasi)")
        print ("2. Lanjutkan sebagai tamu")
        pilih()
    else:
        print ("Pilihan Anda Tidak Tersedia")

def pilih():
    opsi = input("Silahkan pilih (1/2): ")
    if opsi.lower() == "1":
        print("Anda memilih Form Registrasi User \nSilakan tunggu sebentar, anda akan dialihkan ke form registrasi")
        time.sleep(2)
        os.system("cls")
        register()
    elif opsi.lower() == "2":
        print("Anda akan dialihkan ke halaman utama")
        time.sleep(2)
        os.system("cls")
        print("Sebagai tamu, mohon maaf anda tidak dapat melihat jadwal ruangan")
        time.sleep(2)
        exit()
    else:
        print("Mohon maaf pilihan anda tidak tersedia")
        time.sleep(2)
        os.system("cls")
        mulai()
mulai()



