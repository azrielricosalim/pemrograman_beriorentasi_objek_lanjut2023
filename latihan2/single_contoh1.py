class Hewan:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bergerak(self):
        print(self.nama, "Berlari")

class Kucing(Hewan):
    def __init__(self, nama, umur, jenis_bulu):
        super().__init__(nama, umur)
        self.jenis_bulu = jenis_bulu

    def bersuara(self):
        print("Meow meow!")

kucing = Kucing("Unyil", 1, "Himalayan")
kucing.bergerak() 
kucing.bersuara()  