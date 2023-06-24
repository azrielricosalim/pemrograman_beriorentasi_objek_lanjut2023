class Hewan:

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")

class Reptil:

    def __init__(self, jenis, habitat):
        self.jenis = jenis
        self.habitat = habitat

    def display_info(self):
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")

class Amphibi:

    def __init__(self, metamorfosis, habitat):
        self.metamorfosis = metamorfosis
        self.habitat = habitat

    def display_info(self):
        print(f"Metamorfosis: {self.metamorfosis}")
        print(f"Habitat: {self.habitat}")

class Katak(Hewan, Reptil, Amphibi):

    def __init__(self, nama, umur, jenis, habitat, metamorfosis):
        Hewan.__init__(self, nama, umur)
        Reptil.__init__(self, jenis, habitat)
        Amphibi.__init__(self, metamorfosis, habitat)

    def display_info(self):
        super().display_info()
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur}")
        print(f"Jenis: {self.jenis}")
        print(f"Habitat: {self.habitat}")
        print(f"Metamorfosis: {self.metamorfosis}")

# contoh penggunaan
katakA = Katak("Katak hitam kuliah di UMC", 1, "Reptil-Amphibi", "Air dan darat", "lahiran")
katakA.display_info()