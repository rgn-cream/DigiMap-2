from admin import menu_admin 
from Profil_pengguna import tampilkan_profil
from Profil_pengguna import tampilkan_profil
from search import cari_jadwal

current_user = {"username": None}

def tampilkan_menu():
    """Fungsi untuk menampilkan menu utama."""
    print("\n===== Selamat Datang di DIGIMAP =====")
    print("Silakan pilih menu berikut:")
    print("1. Login")
    print("2. Register")
    print("3. Profil Pengguna")
    print("4. Cari Jadwal Kuliah")
    print("5. Tampilan Map")
    print("6. Menu Admin")
    print("7. Logout")

def tampilkan_map():
    print("\n--- Tampilan Map ---")

def main():
    """Fungsi utama program."""
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-7): ").strip()

        if pilihan == "1":
            print("\n--- Login Pengguna ---")

        
        elif pilihan == "2":
            print("\n--- Register Pengguna Baru ---")

        elif pilihan == "3":
            if current_user["username"]:
                print("\n--- Menu Profil Pengguna ---")
                tampilkan_profil()
            else:
                print("\n[ERROR] Anda harus login terlebih dahulu untuk mengakses menu ini.")
        
        elif pilihan == "4":
            if current_user["username"]:
                print("\n--- Menu Pencarian Jadwal Kuliah ---")
                cari_jadwal()
            else:
                print("\n[ERROR] Anda harus login terlebih dahulu untuk mengakses menu ini.")
        
        elif pilihan == "5":
            print("\n--- Tampilan Map ---")
            tampilkan_map()
        
        elif pilihan == "6":
            if current_user["username"]:
                 ()  
            else:
                print("\n[ERROR] Anda harus login terlebih dahulu untuk mengakses menu ini.")
        
        elif pilihan == "7":
            if current_user["username"]:
                (current_user)
                print("\n[INFO] Anda telah logout.")
            else:
                print("\n[ERROR] Anda belum login.")
                
        else:
            print("\n[ERROR] Pilihan tidak valid. Silakan coba lagi!")

if __name__ == "__main__":
    main()

import os, time 
from login_reg_prof import login_admin
from login_reg_prof import menu_pengguna
from login_reg_prof import login_tamu
from login_reg_prof import login_pengguna
from login_reg_prof import register

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

if __name__ == "__main__":
    main()