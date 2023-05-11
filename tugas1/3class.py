#NAMA   : AZRIEL RICO SALIM
#NIM    : 210511122
#KELAS  : K1

def Fahrenheit(C):
    F = (9/5*C)+32
    return F

def Kelvin(C):
    K = C + 273,
    return K

def Reamur(C):
    R = 4/5 * C
    return R

print("Konversi Suhu dari Celcius")
print("==========================")
C = float(input("masukkan suhu dalam Celcius:"))
F = Fahrenheit(C)
K = Kelvin(C)
R = Reamur(C)
print("celcius",str(C))
print("-------------")
print("Konversi ke Fahrenheit -", F)
print("Konversi ke Kelvin -", K)
print("Konversi ke Reamur -",R)