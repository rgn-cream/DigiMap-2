import os, time

def register():
    print("="*50)
    print("Form Register User DIGIMAP <3 ")
    print("="*50)
    nama = input("Masukkan Nama Anda : ")
    username = input("Masukkan Username Anda : ")
    password = input("Masukkan password : ")
    nim = input("Masukkan NIM : ")
    simpan(nama,username,password,nim)
    print("\nYeay! Data Berhasil Disimpan <3")
    opsi = input("Apakah anda ingin kembali ke menu utama?(Y/N)")
    if opsi.lower() == "y":
        print("\nAnda akan dialihkan ke menu utama, mohon tunggu sebentar")
        time.sleep(2)
        os.system("cls")
        pilih()
    elif opsi.lower() == "n":
        time.sleep(2)
        print("\nYaudah kalo gamau, Terimakasih telah melakukan Registrasi di DIGIMAP wofyu <3")
    else :
        print("\nMohon maaf pilihan anda tidak tersedia. Anda akan dialihkan ke menu utama")
        time.sleep(2)
        os.system("cls")
        mulai()

def simpan (nama,username,password,nim):
    file = open("D:\DIGIMAP\DataReg.txt","a")
    file.write("\n"+nama+","+username+","+password+","+nim)

def mulai ():
    print("Selamat Datang di DIGIMAP! \nSilakan Masukan Kata (Reg) Untuk Register User Baru | (Login) Untuk Login User")
    pilih()

def pilih():
    opsi = input("Masukkan kata (Reg) atau (Login) atau (Exit) : ")
    if opsi.lower() == "reg" :
        print("Anda memilih Form Registrasi User \nSilakan tunggu sebentar, anda akan di alihkan ke formn registrasi")
        time.sleep(2)
        os.system("cls")
        register()
    elif opsi.lower() == "login" :
        print("Anda memilih Form Login User \nSilakan tunggu sebentar, anda akan di alihkan ke formn login")
        time.sleep(2)
        os.system("cls")
    elif opsi.lower() == "exit" :
        print("Anda telah memilih exit program DIGIMAP")
        time.sleep(2)
        os.system("cls")
        print("Terimakasih telah menggunakan DIGIMAP, see you")
        time.sleep(2)
        exit()
    else: 
        print("Mohn maaf pilihan anda tidak tersedia")
        time.sleep(2)
        os.system("cls")
        mulai()
mulai()