class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
        
    def info(self):
        print(f"Nama: {self.nama}\nNPM: {self.npm}")
        
mahasiswaB = Mahasiswa("Ahmad", "123456789")
mahasiswaB.info()