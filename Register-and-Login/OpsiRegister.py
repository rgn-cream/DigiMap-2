import os, time, json

def load_data():
    if os.path.exists("D:\DIGIMAP\Register-and-Login\Data.json"): 
        file = open("D:\DIGIMAP\Register-and-Login\Data.json")
        data = json.load(file)
        file.close()
        return data 
    else:
        return{}
    
def save_data(data):
    with open("D:\DIGIMAP\Register-and-Login\Data.json", "w") as file:
        json.dump(data, file, indent=4)

def login(): 
    print("="*70)
    print("Selamat Datang di DigiMap! Silahkan Masukkan Kredensial disini")
    print("="*70)
    username = input("Masukkan Username disini   : ")
    nim = input("Masukkan NIM disini        : ")
    password = input("Masukkan Password disini   : ")

    data = load_data()
    user_data = data.get(username)

    if user_data and user_data["NIM"] == nim and user_data["password"] == password:
        print("="*70)
        print("Login Berhasil!")
        print("="*70)
    else:
        print("="*70)
        print("Username, NIM, atau Password tidak Valid!")
        print("="*70)
        
    opsi = input("Apakah anda ingin kembali ke menu utama?(Y/N) ")
    if opsi.lower() == "y":
        print("\nAnda akan dialihkan ke menu utama, mohon tunggu sebentar")
        time.sleep(2)
        os.system("cls")
        pilih()
    elif opsi.lower() == "n":
        time.sleep(2)
        print("\nYaudah kalo gamau, Terimakasih telah melakukan Registrasi di DIGIMAP wofyu <3")
    else:
        print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
        time.sleep(2)
        os.system("cls")
        mulai()


def register():
    print("="*70)
    print("Form Register User DIGIMAP <3 ")
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
    print("\nYeay! Data Berhasil Disimpan <3")

    opsi = input("Apakah anda ingin kembali ke menu utama?(Y/N) ")
    if opsi.lower() == "y":
        print("\nAnda akan dialihkan ke menu utama, mohon tunggu sebentar")
        time.sleep(2)
        os.system("cls")
        pilih()
    elif opsi.lower() == "n":
        time.sleep(2)
        print("\nYaudah kalo gamau, Terimakasih telah melakukan Registrasi di DIGIMAP wofyu <3")
    else:
        print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
        time.sleep(2)
        os.system("cls")
        mulai()

def tampilkan_profil(profil):
    print("=== Profil Pengguna ===")
    print(f"Nama: {profil['nama']}")
    print(f"Username: {profil['username']}")
    print(f"NIM: {profil['nim']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['ttl']}")
    print(f"Email: {profil['email']}")
    mulai()

def mulai():
    print("Selamat Datang di DIGIMAP! \nSilakan Masukan Kata (Reg) Untuk Register User Baru | (Login) Untuk Login User")
    pilih()

def pilih():
    opsi = input("Masukkan kata (Reg) atau (Login) atau (Exit) : ")
    if opsi.lower() == "reg":
        print("Anda memilih Form Registrasi User \nSilakan tunggu sebentar, anda akan dialihkan ke form registrasi")
        time.sleep(2)
        os.system("cls")
        register()
    elif opsi.lower() == "login":
        print("Anda memilih Form Login User \nSilakan tunggu sebentar, anda akan dialihkan ke form login")
        time.sleep(2)
        os.system("cls")
        login()
    elif opsi.lower() == "profil":
        print("Anda memilih profil User \nSilakan tunggu sebentar, anda akan dialihkan ke profil pengguna")
        time.sleep(2)
        os.system("cls")
        tampilkan_profil()
    elif opsi.lower() == "exit":
        print("Anda telah memilih exit program DIGIMAP")
        time.sleep(2)
        os.system("cls")
        print("Terimakasih telah menggunakan DIGIMAP, see you")
        time.sleep(2)
        exit()
    else:
        print("Mohon maaf pilihan anda tidak tersedia")
        time.sleep(2)
        os.system("cls")
        mulai()
mulai()


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
            register()
        elif pilihan == "2":
            tampilkan_profil()
        elif pilihan == "3":
            print("Terima kasih, sampai bertemu kembali :D ")
            break
        else:
            print("Error, silahkan coba lagi.")
            
main()