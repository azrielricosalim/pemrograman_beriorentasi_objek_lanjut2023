try:
    data = int(input("Masukkan angka awal :"))
    pembagi = data / int(input("Masukkan angka pembagi :"))
except ZeroDivisionError:
    print("Terjadi kesalahan, pembagian tidak boleh nol!")