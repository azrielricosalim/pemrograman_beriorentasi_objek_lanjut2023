class Kendaraan:

    def __init__(self, jenis, merk, warna):
        self.jenis = jenis
        self.merk = merk
        self.warna = warna

    def berkendara(self):
        print("Kendaraan ini sedang melaju.")

class SepedaMotor(Kendaraan):

    def __init__(self, jenis, merk, warna, cc):
        super().__init__(jenis, merk, warna)
        self.cc = cc

    def belok(self):
        print("Sepeda motor ini sedang berbelok.")

motorA = SepedaMotor("Sepeda Motor", "Scoopy", "Hitam", 150)
motorA.berkendara() 
motorA.belok() 