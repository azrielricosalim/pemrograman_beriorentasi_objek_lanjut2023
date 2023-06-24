#Nama   : Sandy Dwi Julian
#Kelas  : K1
#NIM    : 210511033

class KubusMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, sisi):
            return 6 * sisi * sisi
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, sisi):
            return sisi * sisi * sisi
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=KubusMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(45)
C = A.volume(45)
print('Luas Permukaan Kubus:',B)
print('Volume Kubus:',C)