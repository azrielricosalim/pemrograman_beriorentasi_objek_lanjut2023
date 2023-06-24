class Hewan:

    def __init__(self, jenis):
        self.jenis = jenis

    def display_info(self):
        print(f"Jenis hewan: {self.jenis}")
    
class Mamalia(Hewan):
    def __init__(self, jenis, nama):
        super().__init__(jenis)
        self.nama = nama

    def display_info(self):
        super().display_info()
        print(f"Nama mamalia: {self.nama}")

class Karnivora(Hewan):

    def __init__(self, jenis, makanan):
        super().__init__(jenis)
        self.makanan = makanan

    def display_info(self):
        super().display_info()
        print(f"Jenis makanan: {self.makanan}")

class Singa(Mamalia, Karnivora):
    def __init__(self, jenis, nama, makanan):
        Mamalia.__init__(self, jenis, nama)
        Karnivora.__init__(self, jenis, makanan)

    def display_info(self):
        super().display_info()
        print(f"Jenis hewan: {self.jenis}")
        print(f"Nama Mamalia: {self.nama}")
        print(f"Jenis Makanan: {self.makanan}")

# contoh penggunaan
Singa = Singa("Mamalia", "Singa", "Daging")
singa.display_info()
