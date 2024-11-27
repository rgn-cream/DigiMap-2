import os, time, json

def load_data():
    if os.path.exists(""): 
        file = open("")
        data = json.load(file)
        file.close()
        return data 
    else:
        return{}

def login_admin(): 
    print("="*70)
    print("LOGIN")
    print("="*70)
    print("Selamat Datang Kembali di DigiMap! Silahkan Masukkan Kredensial disini")
    print("-"*70)
    username = input("Masukkan Username   : ")
    password = input("Masukkan Password   : ")

    data = load_data()
    user_data = data.get(username)

    if  user_data["password"] == password:
        time.sleep(2)
        print("="*70)
        print("Login Berhasil!")
        print("Anda berhasil login sebagai admin")
        print("="*70)
        
    else:
        print("="*70)
        print("Password tidak Valid!")
        print("="*70)
    
        opsi = input("Coba lagi?(Y/N) ")
        if opsi.lower() == "y":
            os.system("cls")
            login_admin()
        elif opsi.lower() == "n":
            time.sleep(2)
            print("Anda akan kembali ke halaman utama")
            #HALAMAN UTAMA
        else:
            print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
            time.sleep(2)
            os.system("cls")

            