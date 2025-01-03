import json, os
from datetime import datetime

FILE_DATABASE = "data_login.json"

def muat_data():
    if os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, "r") as file:
            return json.load(file)
    #return {"users": {}, "admin": {"username": "admin", "password": "admin123"}}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(FILE_DATABASE, "w") as file:
        json.dump(data, file, indent=4)

#Fungsi validasi tanggal lahir
def validasi_tanggal_lahir(tanggal):
    try:
        datetime.strptime(tanggal, "%d-%m-%Y")
        return True
    except ValueError:
        return False

data_pengguna = muat_data()

