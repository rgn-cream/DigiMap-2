def login():
    if username in user_data and NIM == user_data[username]["NIM"] and password == user_data[username]["password"]:
        print("="*70)
        print("Login Berhasil!")
        print("="*70)
    else:
        print("="*70)
        print("Username, NIM, atau Password tidak Valid!")
        print("="*70)

user_data   = {
        "fjribgs"       : {"NIM": "2403807", "password": "admin123"},
        "sayangallah"   : {"NIM": "2401208", "password": "admin123"}
} 

print("="*70)
print("Selamat Datang di DigiMap! Silahkan Masukkan Kredensial disini")
print("="*70)
username    = input("Masukkan Username disini   : ")
NIM         = input("Masukkan NIM disini        : ")
password    = input("Masukkan Password disini   : ")

login()
