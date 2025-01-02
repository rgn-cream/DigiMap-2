import json, os

FILE_DATABASE = "data_login.json"

def muat_data():
    if os.path.exists(FILE_DATABASE):
        with open(FILE_DATABASE, "r") as file:
            return json.load(file)
    return {"users": {}, "admin": {"username": "admin", "password": "admin123"}}

# Fungsi untuk menyimpan data ke file JSON
def simpan_data(data):
    with open(FILE_DATABASE, "w") as file:
        json.dump(data, file, indent=4)

def validasi_tanggal_lahir(tanggal):
    try:
        if not isinstance(tanggal, str):
            return False
        if len(tanggal) != 10 or tanggal[2] != "-" or tanggal[5] != "-":
            return False
        hari, bulan, tahun = tanggal.split("-")
        if not (hari.isdigit() and bulan.isdigit() and tahun.isdigit()):
            return False
        hari, bulan, tahun = int(hari), int(bulan), int(tahun)
        if not (1 <= hari <= 31 and 1 <= bulan <= 12 and len(str(tahun)) == 4):
            return False
        if bulan in [4, 6, 9, 11] and hari > 30:
            return False
        if bulan == 2:
            if (tahun % 4 == 0 and (tahun % 100 != 0 or tahun % 400 == 0)):
                if hari > 29:
                    return False
            else:
                if hari > 28:
                    return False
        return True
    except:
        return False

data_pengguna = muat_data()

