import json

def cari_jadwal(jadwal):
    print("\n==========Pencarian Jadwal Kelas==========")

   # Meminta input hari
    while True:
        hari = input("\nMasukkan hari: ").capitalize().strip()
        if not hari:
            print("Error: Hari tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break  # Keluar dari loop jika input valid

    # Meminta input jurusan
    while True:
        jurusan = input("\nMasukkan jurusan: ").upper().strip()
        if not jurusan:
            print("Error: Jurusan tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break  # Keluar dari loop jika input valid

    # Meminta input kelas
    while True:
        kelas = input("\nMasukkan kelas: ").upper().strip()
        if not kelas:
            print("Error: Kelas tidak boleh kosong. Silakan masukkan lagi.")
        else:
            break  # Keluar dari loop jika input valid

    hasil = []
    for hari_kuliah, jadwal_harian in jadwal.items():
        if hari and hari_kuliah != hari:
            continue
        for mata_kuliah in jadwal_harian:
            # Filter berdasarkan jurusan
            if jurusan and mata_kuliah.get("jurusan", "").upper() != jurusan:
                continue
            # Filter berdasarkan kelas
            if kelas and mata_kuliah.get("kelas", "").upper() != kelas:
                continue

            # Tambahkan data ke hasil jika cocok
            hasil.append({
                "hari": hari_kuliah,
                "waktu_mulai": mata_kuliah["waktu_mulai"],
                "waktu_selesai": mata_kuliah["waktu_selesai"],
                "jurusan": mata_kuliah.get("jurusan", ""),
                "kelas": mata_kuliah["kelas"],
                "kode_mk": mata_kuliah["kode_mk"],
                "nama_mk": mata_kuliah["nama_mk"],
                "sks": mata_kuliah["sks"],
                "dosen": mata_kuliah["dosen"],
                "ruang": mata_kuliah["ruang"]
            })

# Tampilkan hasil
    print("")
    if hasil:
        # Header tabel
        print(f"{'No':<4}{'Hari':<12}{'Waktu Mulai':<15}{'Waktu Selesai':<15}{'Jurusan':<12}{'Kelas':<12}{'Kode MK':<10}{'Nama MK':<25}{'SKS':<5}{'Dosen':<40}{'Ruang':<15}")
        print("=" * 160)
        for idx, jadwal_item in enumerate(hasil):
            dosen = ", ".join(jadwal_item["dosen"]) if isinstance(jadwal_item["dosen"], list) else jadwal_item["dosen"]
            print(f"{idx + 1:<4}{jadwal_item['hari']:<12}{jadwal_item['waktu_mulai']:<15}{jadwal_item['waktu_selesai']:<15}{jadwal_item['jurusan']:<12}{jadwal_item['kelas']:<12}{jadwal_item['kode_mk']:<10}{jadwal_item['nama_mk']:<25}{jadwal_item['sks']:<5}{dosen:<40}{jadwal_item['ruang']:<15}")
    else:
        print("\nTidak ada jadwal yang sesuai dengan kriteria pencarian.\n")
    
# Fungsi untuk membaca data dari file JSON
def load_jadwal_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Penggunaan
if __name__ == "__main__":
    jadwal_kuliah = load_jadwal_from_json('data_jadwal.json')
    cari_jadwal(jadwal_kuliah)