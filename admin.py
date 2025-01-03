import json, os, time
from fungsi import muat_data

def ulangiLoginAdmin():
    login_admin()

def login_admin():
    print("="*70)
    print("LOGIN ADMIN")
    print("="*70)
    
    data_admin = muat_data()
    while True:
        email = input("Masukkan email (ex: nama@gmail.com/@upi.edu): ").strip()
        if email != data_admin["admin"].get("email"):
            print("Email tidak valid, periksa kembali email yang dimasukkan.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            ulangiLoginAdmin()
            return
        elif not email:
            print("Email tidak boleh kosong.")
            print("Email tidak valid, periksa kembali email yang dimasukkan.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            ulangiLoginAdmin()
            continue
        elif email.count("@gmail.com") != 1 and email.count("@upi.edu") != 1:
            print("Format email tidak valid. Pastikan email yang dimasukkan sesuai dengan format @gmail.com atau @upi.edu.")
            print("Email tidak valid, periksa kembali email yang dimasukkan.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            ulangiLoginAdmin()
            continue
        elif email.count("@gmail.com") > 1 or email.count("@upi.edu") > 1:
            print("Format email tidak valid. Pastikan email yang dimasukkan hanya memiliki satu domain.")
            print("Email tidak valid, periksa kembali email yang dimasukkan.")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
            ulangiLoginAdmin()
            continue
        break

    kesempatan = 3
    while kesempatan > 0:
        password = input("Masukkan password (8 karakter): ").strip()
        if not password:
            print("Password tidak boleh kosong.")
        elif len(password) < 8:
            print("Password harus terdiri dari 8 karakter.")
        else:
            break
        kesempatan -= 1
        print(f"Anda memiliki {kesempatan} kesempatan lagi.")

    if email == data_admin["admin"]["email"] and password == data_admin["admin"]["password"]:
        print("Login Admin berhasil!")
        print("Anda akan memasuki menu admin. Mohon tunggu sebentar...")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")
        file_path = 'data_jadwal.json'
        menu_admin(file_path)
    else: 
        print("Kesempatan habis! Kembali ke menu awal.")
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")

        from login_menu import main
        main()


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
        dosen = ", ".join(item.get("dosen", ['Tidak ada dosen'])) if isinstance(item.get("dosen"), list) else item.get("dosen", 'Tidak ada dosen')
        jurusan = item.get('jurusan', 'Tidak ada jurusan')  
        kelas = item.get('kelas', 'Tidak ada kelas')
        kode_mk = item.get('kode_mk', 'Tidak ada kode MK')
        nama_mk = item.get('nama_mk', 'Tidak ada nama MK')
        sks = item.get('sks', '0')  # Menggunakan '0' sebagai default untuk SKS
        ruang = item.get('ruang', 'Tidak ada ruang')

        print(f"{idx + 1:<4}{hari:<12}{item.get('waktu_mulai', 'Tidak ada waktu mulai'):<15}{item.get('waktu_selesai', 'Tidak ada waktu selesai'):<15}{jurusan:<12}{kelas:<12}{kode_mk:<10}{nama_mk:<25}{sks:<5}{dosen:<40}{ruang:<15}")

# Fungsi untuk menambahkan jadwal baru
def tambah_jadwal(file_path):
    print("="*70)
    print("Tambah Jadwal")
    print("="*70)
    data_jadwal = baca_data(file_path)

    # Daftar hari yang valid
    hari_valid = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]

    while True:
        hari = input("Masukkan hari (contoh: Senin, Selasa, dst.): ").capitalize().strip()
        
        # Validasi input
        if not hari:
            print("Error: Hari tidak boleh kosong. Silakan masukkan lagi.")
        elif hari not in hari_valid:
            print("Error: Hari tidak valid. Harap masukkan hari dari Senin hingga Jumat.")
        else:
            break

    # Fungsi untuk mengonversi waktu ke menit
    def waktu_ke_menit(waktu):
        jam, menit = map(int, waktu.split(':'))
        return jam * 60 + menit

    # Meminta input waktu mulai
    while True:
        waktu_mulai = input("Masukkan waktu mulai (contoh: 13:00): ").strip()
        if ":" in waktu_mulai and all(part.isdigit() for part in waktu_mulai.split(":")) and len(waktu_mulai.split(":")) == 2:
            break
        print("Error: Format waktu tidak valid. Gunakan format HH:MM.")

    # Meminta input waktu selesai
    while True:
        waktu_selesai = input("Masukkan waktu selesai (contoh: 14:40): ").strip()
        if ":" in waktu_selesai and all(part.isdigit() for part in waktu_selesai.split(":")) and len(waktu_selesai.split(":")) == 2:
            if waktu_ke_menit(waktu_selesai) > waktu_ke_menit(waktu_mulai):
                break
            print("Error: Waktu selesai tidak boleh sebelum atau sama dengan waktu mulai.")
        else:
            print("Error: Format waktu tidak valid. Gunakan format HH:MM.")


    # Daftar jurusan yang valid
    jurusan_valid = ["RPL", "TEKKOM", "PGPAUD", "PGSD", "PMM"]

    # Meminta input jurusan
    while True:
        jurusan = input("Masukkan jurusan (contoh: RPL): ").upper().strip()
        
        # Validasi input
        if not jurusan:
            print("Error: Jurusan tidak boleh kosong. Silakan masukkan lagi.")
        elif jurusan not in jurusan_valid:
            print("Error: Jurusan tidak valid. Harap masukkan salah satu dari: RPL, TEKKOM, PGPAUD, PGSD, PMM.")
        else:
            break 

    # Daftar kelas valid berdasarkan jurusan
    if jurusan in ["PGSD"]:
        kelas_valid = ["A", "B", "C", "D", "E", "F"]
    else:
        kelas_valid = ["A", "B", "C"]

    # Meminta input kelas
    while True:
        kelas = input("Masukkan kelas (contoh: 1B): ").upper().strip()

        # Validasi input
        if not kelas:
            print("Error: Kelas tidak boleh kosong.")
        elif len(kelas) != 2 or not kelas[0].isdigit() or kelas[1] not in kelas_valid:
            print(f"Error: Kelas harus terdiri dari 1 digit diikuti oleh 1 huruf (contoh: 1B). Untuk jurusan {jurusan}, kelas yang valid adalah: {', '.join(kelas_valid)}.")
        else:
            break 

    # Meminta input kode mata kuliah
    while True:
        kode_mk = input("Masukkan kode mata kuliah (contoh: RL01): ").strip()
        
        # Validasi input
        if not kode_mk:
            print("Error: Kode mata kuliah tidak boleh kosong.")
        elif len(kode_mk) != 4 or not kode_mk[:2].isalpha() or not kode_mk[2:].isdigit():
            print("Error: Kode mata kuliah harus terdiri dari 2 huruf diikuti oleh 2 digit angka (contoh: RL01).")
        else:
            break

    # Meminta input nama mata kuliah
    while True:
        nama_mk = input("Masukkan nama mata kuliah: ").strip()
        
        # Validasi input
        if not nama_mk:
            print("Error: Nama mata kuliah tidak boleh kosong.")
        elif not nama_mk.replace(" ", "").isalpha():
            print("Error: Nama mata kuliah hanya boleh terdiri dari huruf dan spasi.")
        else:
            break  

    # Meminta input SKS
    while True:
        sks = input("Masukkan SKS (contoh: 2): ")
        if sks and sks.isdigit():
            sks_int = int(sks)  
            break
        print("Error: SKS tidak boleh kosong dan harus berupa angka bulat (integer). Silakan masukkan lagi.")
    
    # Meminta input dosen
    while True:
        dosen = input("Masukkan nama dosen (pisahkan dengan koma jika lebih dari satu): ").strip()
        
        # Validasi input
        if not dosen:
            print("Error: Nama dosen tidak boleh kosong. Silakan masukkan lagi.")
        elif any(char.isdigit() for char in dosen):
            print("Error: Nama dosen tidak boleh mengandung angka. Silakan masukkan lagi.")
        else:
            break

    # Meminta input ruang
    while True:
        ruang = input("Masukkan ruang (contoh: 20.4B.04.001): ").strip()
        
        # Validasi input
        if not ruang:
            print("Error: Ruang tidak boleh kosong.")
        elif len(ruang.split('.')) != 4 or not all(part.isalnum() for part in ruang.split('.')):
            print("Error: Format ruang tidak valid. Harap masukkan sesuai format (contoh: 20.4B.04.001).")
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
    print("Anda akan dialihkan ke menu utama") 
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk mengedit jadwal
def edit_jadwal(file_path):
    print("="*70)
    print("Edit Jadwal")
    print("="*70)

    data_jadwal = baca_data(file_path)

    while True:
        # Meminta input hari
        hari = input("Masukkan hari yang ingin diedit: ").capitalize().strip()
        if not hari:
            kembali = input("Input kosong. Apakah Anda ingin kembali ke menu admin? (y/n): ").strip().lower()
            if kembali == 'y':
                return  
            else:
                continue    
        if hari not in data_jadwal:
            print("Error: Hari tidak ditemukan.")
            continue            
        break

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

    # Fungsi untuk mengonversi waktu ke menit
    def waktu_ke_menit(waktu):
        jam, menit = map(int, waktu.split(':'))
        return jam * 60 + menit

    # Waktu Mulai
    while True:
        waktu_mulai = input(f"Waktu Mulai [{jadwal_edit['waktu_mulai']}]: ").strip()
        if not waktu_mulai:
            waktu_mulai = jadwal_edit['waktu_mulai']  # Tetap menggunakan data lama
            break
        elif not all(part.isdigit() for part in waktu_mulai.split(':')) or len(waktu_mulai.split(':')) != 2:
            print("Error: Waktu mulai harus dalam format HH:MM dan hanya boleh mengandung angka. Silakan masukkan lagi.")
        else:
            jadwal_edit['waktu_mulai'] = waktu_mulai
            break

    # Waktu Selesai
    while True:
        waktu_selesai = input(f"Waktu Selesai [{jadwal_edit['waktu_selesai']}]: ").strip()
        if not waktu_selesai:
            waktu_selesai = jadwal_edit['waktu_selesai']  # Tetap menggunakan data lama
            break
        elif not all(part.isdigit() for part in waktu_selesai.split(':')) or len(waktu_selesai.split(':')) != 2:
            print("Error: Waktu selesai harus dalam format HH:MM dan hanya boleh mengandung angka. Silakan masukkan lagi.")
        elif waktu_ke_menit(waktu_selesai) <= waktu_ke_menit(waktu_mulai):
            print("Error: Waktu selesai tidak boleh sebelum atau sama dengan waktu mulai.")
        else:
            jadwal_edit['waktu_selesai'] = waktu_selesai
            break

    # Jurusan
    jurusan_valid = ["RPL", "TEKKOM", "PGSD", "PMM"]
    while True:
        jurusan = input(f"Jurusan [{jadwal_edit['jurusan']}]: ").upper().strip()
        if not jurusan:
            jurusan = jadwal_edit['jurusan']  # Tetap menggunakan data lama
            break
        elif jurusan not in jurusan_valid:
            print("Error: Jurusan tidak valid. Harap masukkan salah satu dari: RPL, TEKKOM, PGPAUD, PGSD, PMM.")
        else:
            jadwal_edit['jurusan'] = jurusan
            break

    # Kelas
    if jadwal_edit['jurusan'] in ["PGSD"]:
        kelas_valid = ["A", "B", "C", "D", "E", "F"]
    else:
        kelas_valid = ["A", "B", "C"]

    while True:
        kelas = input(f"Kelas [{jadwal_edit['kelas']}]: ").upper().strip()
        if not kelas:
            kelas = jadwal_edit['kelas']  # Tetap menggunakan data lama
            break
        elif len(kelas) != 2 or not kelas[0].isdigit() or kelas[1] not in kelas_valid:
            print(f"Error: Kelas harus terdiri dari 1 digit diikuti oleh 1 huruf (contoh: 1B). Untuk jurusan {jadwal_edit['jurusan']}, kelas yang valid adalah: {', '.join(kelas_valid)}.")
        else:
            jadwal_edit['kelas'] = kelas
            break
        
    # Kode Mata Kuliah
    while True:
        kode_mk = input(f"Kode MK [{jadwal_edit['kode_mk']}]: ").strip()
        if not kode_mk:
            kode_mk = jadwal_edit['kode_mk']  # Tetap menggunakan data lama
            break
        elif len(kode_mk) != 4 or not kode_mk.isalnum():
            print("Error: Kode MK harus terdiri dari 4 karakter alfanumerik.")
        else:
            jadwal_edit['kode_mk'] = kode_mk
            break

    # Dosen
    while True:
        dosen = input(f"Dosen [{', '.join(jadwal_edit['dosen'])}]: ").strip()
        if not dosen:
            dosen = jadwal_edit['dosen']  # Tetap menggunakan data lama
            break
        elif any(char.isdigit() for char in dosen):
            print("Error: Nama dosen tidak boleh mengandung angka. Silakan masukkan lagi.")
        else:
            jadwal_edit['dosen'] = [dosen.strip() for dosen in dosen.split(',')]
            break

    # Ruangan
    while True:
        ruang = input(f"Ruang [{jadwal_edit['ruang']}]: ").strip()
        if not ruang:
            print("Menggunakan nilai ruangan sebelumnya.")
            break
        elif len(ruang.split('.')) != 4 or not all(part.isalnum() for part in ruang.split('.')):
            print("Error: Format ruang tidak valid. Harap masukkan sesuai format (contoh: 20.4B.04.001).")
        else:
            jadwal_edit['ruang'] = ruang  # Update nilai ruangan
            break

    # Simpan perubahan
    data_jadwal[hari][nomor] = jadwal_edit
    simpan_data(file_path, data_jadwal)
    print("Jadwal berhasil diperbarui.")

    print("Anda akan dialihkan ke menu utama")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi untuk menghapus jadwal
def hapus_jadwal(file_path):
    data_jadwal = baca_data(file_path)

    while True:
        # Meminta input hari
        hari = input("Masukkan hari yang ingin dihapus: ").capitalize().strip()
        if not hari:
            kembali = input("Input kosong. Apakah Anda ingin kembali ke menu admin? (y/n): ").strip().lower()
            if kembali == 'y':
                return  
            else:
                continue    
        if hari not in data_jadwal:
            print("Error: Hari tidak ditemukan.")
            continue            
        break

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

    print("Anda akan dialihkan ke menu utama")
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")

# Fungsi utama untuk menampilkan menu
def menu_admin(file_path):
    file_path = 'data_jadwal.json'
    while True:
        print("="*70)
        print("Menu:")
        print("="*70)
        print("1. Tambah Jadwal")
        print("2. Edit Jadwal")
        print("3. Hapus Jadwal")
        print("4. Keluar")
        
        pilihan = input("Pilih tindakan (1/2/3/4): ").strip()
        
        if pilihan == '1':
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(2)
            tambah_jadwal(file_path)
        elif pilihan == '2':
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(2)
            edit_jadwal(file_path)
        elif pilihan == '3':
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(2)
            hapus_jadwal(file_path)
        elif pilihan == '4':
            print("Terima kasih! Keluar dari program.")
            os.system("cls" if os.name == "nt" else "clear")
            time.sleep(2)
            break
        else:
            print("Pilihan tidak valid. Harap pilih antara 1- 4.")
    
