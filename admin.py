jadwal_list = []

# Variabel untuk mengatur ID auto-increment mulai dari 1
id_counter = 1

# Fungsi untuk menambah jadwal kuliah
def tambah_jadwal(jadwal_list):
    global id_counter
    print("\nMenambahkan Jadwal Kuliah:")
    
    # Mengambil input dari pengguna
    hari = input("Hari: ")
    waktu_mulai = input("Waktu Mulai (format HH:MM): ")
    waktu_selesai = input("Waktu Selesai (format HH:MM): ")
    kelas = input("Kelas (format: RPL 1B): ")
    kode_mk = input("Kode Mata Kuliah (format MK01): ")
    nama_mk = input("Nama Mata Kuliah: ")
    sks = int(input("Jumlah SKS: "))
    dosen = input("Nama dosen: ")
    ruang = input("Ruang: ")

    # Menyimpan jadwal dalam dictionary dengan ID auto-increment
    jadwal = {
        "id": id_counter,
        "hari": hari,
        "waktu_mulai": waktu_mulai,
        "waktu_selesai": waktu_selesai,
        "kelas": kelas,
        "kode_mk": kode_mk,
        "nama_mk": nama_mk,
        "sks": sks,
        "dosen": dosen,
        "ruang": ruang
    }

    # Menambahkan jadwal ke list
    jadwal_list.append(jadwal)
    
    # Meningkatkan counter ID untuk jadwal berikutnya
    id_counter += 1
    print("Jadwal berhasil ditambahkan!")

# Fungsi untuk menampilkan semua jadwal
def tampilkan_jadwal(jadwal_list):
    if not jadwal_list:
        print("Tidak ada jadwal yang tersedia.")
        return
    print("\nDaftar Jadwal Kuliah:")
    for jadwal in jadwal_list:
        print(f"ID: {jadwal['id']}, Hari: {jadwal['hari']}, Waktu: {jadwal['waktu_mulai']} - {jadwal['waktu_selesai']}, Mata Kuliah: {jadwal['nama_mk']}")

# Fungsi untuk mengupdate jadwal berdasarkan ID
def update_jadwal(jadwal_list):
    jadwal_id = int(input("\nMasukkan ID jadwal yang ingin diubah: "))
    jadwal = next((item for item in jadwal_list if item['id'] == jadwal_id), None)
    
    if jadwal is None:
        print("Jadwal dengan ID tersebut tidak ditemukan!")
        return
    
    print("Mengubah Jadwal Kuliah:")
    jadwal['hari'] = input(f"Hari ({jadwal['hari']}): ") or jadwal['hari']
    jadwal['waktu_mulai'] = input(f"Waktu Mulai ({jadwal['waktu_mulai']}): ") or jadwal['waktu_mulai']
    jadwal['waktu_selesai'] = input(f"Waktu Selesai ({jadwal['waktu_selesai']}): ") or jadwal['waktu_selesai']
    jadwal['kelas'] = input(f"Kelas ({jadwal['kelas']}): ") or jadwal['kelas']
    jadwal['kode_mk'] = input(f"Kode Mata Kuliah ({jadwal['kode_mk']}): ") or jadwal['kode_mk']
    jadwal['nama_mk'] = input(f"Nama Mata Kuliah ({jadwal['nama_mk']}): ") or jadwal['nama_mk']
    jadwal['sks'] = int(input(f"Jumlah SKS ({jadwal['sks']}): ") or jadwal['sks'])
    jadwal['dosen'] = input(f"Nama Dosen ({jadwal['dosen']}): ") or jadwal['dosen']
    jadwal['ruang'] = input(f"Ruang ({jadwal['ruang']}): ") or jadwal['ruang']
    
    print("Jadwal berhasil diubah!")

# Fungsi untuk menghapus jadwal berdasarkan ID
def hapus_jadwal(jadwal_list):
    jadwal_id = int(input("\nMasukkan ID jadwal yang ingin dihapus: "))
    jadwal = next((item for item in jadwal_list if item['id'] == jadwal_id), None)
    
    if jadwal is None:
        print("Jadwal dengan ID tersebut tidak ditemukan!")
        return
    
    jadwal_list.remove(jadwal)
    print("Jadwal berhasil dihapus!")

# Menu untuk operasi CRUD
def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Tambah Jadwal")
        print("2. Tampilkan Jadwal")
        print("3. Update Jadwal")
        print("4. Hapus Jadwal")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_jadwal(jadwal_list)
        elif pilihan == "2":
            tampilkan_jadwal(jadwal_list)
        elif pilihan == "3":
            update_jadwal(jadwal_list)
        elif pilihan == "4":
            hapus_jadwal(jadwal_list)
        elif pilihan == "5":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    menu()
