from fungsi import simpan_data, validasi_tanggal_lahir, data_pengguna
from fungsi import muat_data

def tampilkan_profil(profil):
    print("="*70)
    print("Profil Pengguna".center(70))
    print("="*70)
    print(f"Nama: {profil['nama']}")
    print(f"NIM: {profil['NIM']}")
    print(f"Jurusan: {profil['jurusan']}")
    print(f"Kelas: {profil['kelas']}")
    print(f"Tanggal Lahir: {profil['tanggal_lahir']}")
    print(f"No Telepon: {profil['no_telepon']}")
    print(f"Email: {profil['email']}")

def edit_profil(profil, username):
    print("\n=== Edit Profil Pengguna ===")
    while True:
        print("\nPilih bagian profil yang ingin Anda edit:")
        print("1. Nama")
        print("2. NIM")
        print("3. Jurusan")
        print("4. Kelas")
        print("5. Tanggal Lahir")
        print("6. No Telepon")
        print("7. Email")
        print("8. Selesai")
        pilihan = input("Masukkan pilihan (1-7): ").strip()

        if pilihan == "1":
            while True:
                nama = input("Masukkan nama baru: ").strip()
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
            profil["nama"] = nama

        elif pilihan == "2":
            while True:
                NIM = input("Masukkan NIM baru (7 digit): ").strip()
                if not NIM.isdigit() or len(NIM) != 7:
                    print("NIM harus berupa angka 7 digit.")
                    continue
                break
            profil["NIM"] = NIM

        elif pilihan == "3":
            # Daftar jurusan yang valid
            jurusan_valid = ["RPL", "TEKKOM", "PGPAUD", "PGSD", "PMM"]
            while True:
                jurusan = input("Masukkan jurusan (contoh: RPL): ").upper().strip()
                
                # Validasi input
                if not jurusan:
                    print("Error: Jurusan tidak boleh kosong. Silakan masukkan lagi.")
                elif jurusan not in jurusan_valid:
                    print("Error: Jurusan tidak valid. Harap masukkan salah satu dari: RPL, TEKKOM, PGPAUD, PGSD, PMM.")
                else:
                    break 
            profil["jurusan"] = jurusan

        elif pilihan == "4":
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
                profil["jurusan"] = jurusan

        elif pilihan == "5":
            while True:
                tanggal_lahir = input("Masukkan tanggal lahir baru (DD-MM-YYYY): ").strip()
                if not validasi_tanggal_lahir(tanggal_lahir):
                    print("Format tanggal lahir tidak valid. Gunakan format DD-MM-YYYY.")
                    continue
                break
            profil["tanggal_lahir"] = tanggal_lahir

        elif pilihan == "6":
            while True:
                no_telepon = input("Masukkan no telepon baru (10-13 digit): ").strip()
                if not no_telepon.isdigit() or not (10 <= len(no_telepon) <= 13):
                    print("Nomor telepon harus berupa angka dengan panjang 10-13 digit.")
                    continue
                break
            profil["no_telepon"] = no_telepon

        elif pilihan == "7":
            while True:
                email = input("Masukkan email baru (ex: nama@gmail.com/@upi.edu): ").strip()
                if not email:
                    print("Email tidak boleh kosong.")
                    continue
                elif email.count("@gmail.com") != 1 and email.count("@upi.edu") != 1:
                    print("Format email tidak valid. Gunakan @gmail.com atau @upi.edu.")
                    continue
                break
            profil["email"] = email

        elif pilihan == "8":
            print("Perubahan profil berhasil disimpan!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        data_pengguna["users"][username]["profil"] = profil
        simpan_data(data_pengguna)
        print("Perubahan berhasil disimpan!")

    while True:
        lihat_profil = input("Apakah Anda ingin melihat profil yang diperbarui? (Y/N): ").strip().lower()
        if lihat_profil == "y":
            tampilkan_profil(profil)
            break
        elif lihat_profil == "n":
            print("Anda kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Masukkan Y atau N.")
