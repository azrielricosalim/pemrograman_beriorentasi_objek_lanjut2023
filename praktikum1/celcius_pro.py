#NAMA   : AZRIEL RICO SALIM
#NIM    : 210511122
#KELAS  : K1

class Celcius:
    def fahrenheit(celcius):
        F = (celcius * 9/5) + 32
        return F

    def kelvin(celcius):
        K = celcius + 273.15
        return K

    def reamur(celcius):
        R = celcius * 4/5
        return R

A = Celcius()
c = float(input("Masukan Nilai Celcius:")) 
fahrenheit = Celcius.fahrenheit(c)
kelvin = Celcius.kelvin(c)
reamur = Celcius.reamur(c)
print("Fahrenheit adalah",fahrenheit)
print("Kelvin adalah",kelvin)
print("Reamur adalah",reamur)