#Nama   : Azriel Rico Salim
#Nim    : 210511122
#Kelas  : K1


#pastikan modul playsound sudah terinstall
from playsound import playsound
class Hewan:
    suara = "gaada.wav"
    def mainkan_suara(self):
        playsound(self.suara)

class Anjing(Hewan):
    suara = "anjing.wav"

#instansiasi
anjing=Anjing()

#contoh pemanggilan
anjing.mainkan_suara()


#apa bila terjadi error coba upgrade/downgrade ke module playsound versi 1.2.2
