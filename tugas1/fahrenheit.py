#NAMA   : AZRIEL RICO SALIM
#NIM    : 210511122
#KELAS  : K1

def Fahrenheit(C):
    F = (9/5*C)+32
    return F

print("Konversi Suhu dari Celcius")
print("==========================")
C = float(input("masukkan suhu dalam Celcius:"))
F = Fahrenheit(C)
print("celcius",str(C))
print("-------------")
print("Konversi ke Fahrenheit -", F)