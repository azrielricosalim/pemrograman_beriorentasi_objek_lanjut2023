#NAMA   : AZRIEL RICO SALIM
#NIM    : 210511122
#KELAS  : K1

def Kelvin(C):
    K = C + 273
    return K

print("Konversi Suhu dari Celcius")
print("==========================")
C = float(input("masukkan suhu dalam Celcius:"))
K = Kelvin(C)
print("celcius",str(C))
print("-------------")
print("Konversi ke Kelvin -", K)