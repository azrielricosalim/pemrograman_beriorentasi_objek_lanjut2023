data = {"Kucing": 11, "Singa": 22, "Jerapah": 43}
try:
    value = data["Ayam"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")