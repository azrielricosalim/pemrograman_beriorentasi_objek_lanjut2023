#Nama   : Sandy Dwi Julian
#Kelas  : K1
#NIM    : 210511033

class TabungMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, jari, tinggi):
            return 2 * 22/7 * jari * (jari + tinggi)
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari, tinggi):
            return 22/7 * jari * jari * tinggi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=TabungMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(50, 25)
C = A.volume(50, 25)
print('Luas Permukaan Tabung:',B)
print('Volume Tabung:',C)