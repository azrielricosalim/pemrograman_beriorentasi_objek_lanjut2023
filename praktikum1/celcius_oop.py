#NAMA   : AZRIEL RICO SALIM
#NIM    : 210511122
#KELAS  : K1

class Celcius:
    def __init__(self, celcius):
        self.celcius=celcius

    def fahrenheit(self):
        F = (self.celcius * 9/5) + 32
        return F

    def kelvin(self):
        K = self.celcius + 273.15
        return K

    def reamur(self):
        R = self.celcius * 4/5
        return R

c = float(input("Masukan Nilai Celcius:"))
A = Celcius(c)
fahrenheit = A.fahrenheit()
kelvin = A.kelvin()
reamur = A.reamur()
print("Fahrenheit adalah",fahrenheit)
print("Kelvin adalah",kelvin)
print("Reamur adalah",reamur)