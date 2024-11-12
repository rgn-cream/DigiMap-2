profil_pengguna = {
    "nama": "Nama Pengguna",
    "NIM": "123456789",
    "kelas": "TI-1A",
    "tanggal_lahir": "01-01-2000",
    "no_telepon": "081234567890",
    "email": "email@domain.com"
}

def tampilkan_profil():
    print("=== Profil Pengguna ===")
    print(f"Nama: {profil_pengguna['nama']}")
    print(f"NIM: {profil_pengguna['NIM']}")
    print(f"Kelas: {profil_pengguna['kelas']}")
    print(f"Tanggal Lahir: {profil_pengguna['tanggal_lahir']}")
    print(f"No Telepon: {profil_pengguna['no_telepon']}")
    print(f"Email: {profil_pengguna['email']}")


tampilkan_profil()
