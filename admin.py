import json

# Fungsi untuk membaca data dari file JSON
def baca_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error dalam membaca file JSON.")
        return {}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
def tampilkan_jadwal(hari, jadwal):
    print(f"\nJadwal untuk {hari}:")
    print(f"{'No':<4}{'Hari':<12}{'Waktu Mulai':<15}{'Waktu Selesai':<15}{'Jurusan':<12}{'Kelas':<12}{'Kode MK':<10}{'Nama MK':<25}{'SKS':<5}{'Dosen':<40}{'Ruang':<15}")
    print("=" * 160)
    for idx, item in enumerate(jadwal):
        dosen = ", ".join(item["dosen"]) if isinstance(item["dosen"], list) else item["dosen"]
        print(f"{idx + 1:<4}{hari:<12}{item['waktu_mulai']:<15}{item['waktu_selesai']:<15}{item['jurusan']:<12}{item['kelas']:<12}{item['kode_mk']:<10}{item['nama_mk']:<25}{item['sks']:<5}{dosen:<40}{item['ruang']:<15}")

# Fungsi untuk menambahkan jadwal baru
def tambah_jadwal(file_path):
    data_jadwal = baca_data(file_path)

    # Meminta input hari
    while True:
        hari = input("Masukkan hari (misal: Senin, Selasa, dst.): ").capitalize().strip()
        if not hari:
            print("Error: Hari tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input waktu mulai
    while True:
        waktu_mulai = input("Masukkan waktu mulai (misal: 13:00): ").strip()
        if not waktu_mulai:
            print("Error: Waktu mulai tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input waktu selesai
    while True:
        waktu_selesai = input("Masukkan waktu selesai (misal: 14:40): ").strip()
        if not waktu_selesai:
            print("Error: Waktu selesai tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input jurusan
    while True:
        jurusan = input("Masukkan jurusan: ").strip()
        if not jurusan:
            print("Error: Jurusan tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input kelas
    while True:
        kelas = input("Masukkan kelas: ").strip()
        if not kelas:
            print("Error: Kelas tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input kode mata kuliah
    while True:
        kode_mk = input("Masukkan kode mata kuliah: ").strip()
        if not kode_mk:
            print("Error: Kode mata kuliah tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input nama mata kuliah
    while True:
        nama_mk = input("Masukkan nama mata kuliah: ").strip()
        if not nama_mk:
            print("Error: Nama mata kuliah tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input SKS
    while True:
        sks = input("Masukkan SKS: ").strip()
        if not sks:
            print("Error: SKS tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input dosen
    while True:
        dosen = input("Masukkan nama dosen (pisahkan dengan koma jika lebih dari satu): ").strip()
        if not dosen:
            print("Error: Nama dosen tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Meminta input ruang
    while True:
        ruang = input("Masukkan ruang: ").strip()
        if not ruang:
            print("Error: Ruang tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break

    # Membuat entri jadwal baru
    jadwal_baru = {
        "waktu_mulai": waktu_mulai,
        "waktu_selesai": waktu_selesai,
        "jurusan": jurusan,
        "kelas": kelas,
        "kode_mk": kode_mk,
        "nama_mk": nama_mk,
        "sks": sks,
        "dosen": [dosen.strip() for dosen in dosen.split(',')],
        "ruang": ruang
    }

    # Menambahkan jadwal baru ke dalam data
    if hari not in data_jadwal:
        data_jadwal[hari] = []
    data_jadwal[hari].append(jadwal_baru)

    # Menyimpan data kembali ke file JSON
    simpan_data(file_path, data_jadwal)
    print("Jadwal berhasil ditambahkan!")

# Fungsi untuk mengedit jadwal
def edit_jadwal(file_path):
    data_jadwal = baca_data(file_path)

    # Meminta input hari
    hari = input("Masukkan hari yang ingin diedit: ").capitalize().strip()
    if hari not in data_jadwal:
        print("Error: Hari tidak ditemukan.")
        return

    # Menampilkan jadwal yang ada dalam format tabel
    tampilkan_jadwal(hari, data_jadwal[hari])

    # Meminta input nomor jadwal yang ingin diedit
    while True:
        try:
            nomor = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1
            if 0 <= nomor < len(data_jadwal[hari]):
                break
            else:
                print("Error: Nomor tidak valid. Silakan masukkan lagi.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")

    # Meminta input baru untuk jadwal yang dipilih
    jadwal_edit = data_jadwal[hari][nomor]
    print("Masukkan data baru (tekan Enter untuk tetap menggunakan data lama):")

    for key in jadwal_edit.keys():
        new_value = input(f"{key.capitalize()} [{jadwal_edit[key]}]: ").strip()
        if new_value:
            if key == "dosen":
                new_value = [dosen.strip() for dosen in new_value.split(',')]
            jadwal_edit[key] = new_value

    # Menyimpan data kembali ke file JSON
    simpan_data(file_path, data_jadwal)
    print("Jadwal berhasil diedit!")

# Fungsi untuk menghapus jadwal
def hapus_jadwal(file_path):
    data_jadwal = baca_data(file_path)

    # Meminta input hari
    hari = input("Masukkan hari yang ingin dihapus jadwalnya: ").capitalize().strip()
    if hari not in data_jadwal:
        print("Error: Hari tidak ditemukan.")
        return

    # Menampilkan jadwal yang ada dalam format tabel
    tampilkan_jadwal(hari, data_jadwal[hari])

    # Meminta input nomor jadwal yang ingin dihapus
    while True:
        try:
            nomor = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
            if 0 <= nomor < len(data_jadwal[hari]):
                break
            else:
                print("Error: Nomor tidak valid. Silakan masukkan lagi.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")

    # Menghapus jadwal yang dipilih
    del data_jadwal[hari][nomor]

    # Menghapus entri hari jika tidak ada jadwal tersisa
    if not data_jadwal[hari]:
        del data_jadwal[hari]

    # Menyimpan data kembali ke file JSON
    simpan_data(file_path, data_jadwal)
    print("Jadwal berhasil dihapus!")

# Fungsi utama untuk menampilkan menu
def menu_admin(file_path):
    while True:
        print("\nMenu:")
        print("1. Tambah Jadwal")
        print("2. Edit Jadwal")
        print("3. Hapus Jadwal")
        print("4. Keluar")
        
        pilihan = input("Pilih tindakan (1-4): ").strip()
        
        if pilihan == '1':
            tambah_jadwal(file_path)
        elif pilihan == '2':
            edit_jadwal(file_path)
        elif pilihan == '3':
            hapus_jadwal(file_path)
        elif pilihan == '4':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Harap pilih antara 1- 4.")

# Memanggil fungsi menu()
file_path = 'data_jadwal.json'
menu_admin(file_path)