from profil_pengguna import tambah_profil
from search_jadwal.search import cari_jadwal

current_user = {"username": None}

def tampilkan_menu():
    """Fungsi untuk menampilkan menu utama."""
    print("\n=== Selamat Datang di DIGIMAP ===")
    print("Silakan pilih menu berikut:")
    print("1. Login")
    print("2. Register")
    print("3. Profil Pengguna")
    print("4. Cari Jadwal Kuliah")
    print("5. Tampilan Map")
    print("6. Logout")
    print("7. Keluar")

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
                tambah_profil()
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
                (current_user)
                print("\n[INFO] Anda telah logout.")
            else:
                print("\n[ERROR] Anda belum login.")
        
        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan DIGIMAP. Sampai jumpa!")
            break
        
        else:
            print("\n[ERROR] Pilihan tidak valid. Silakan coba lagi!")

if __name__ == "__main__":
    main()
