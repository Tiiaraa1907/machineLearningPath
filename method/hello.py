# Define a function
def one():
    print("Hello, World!")

nama = "Dicoding"



# MENAMBAHKAN KELAS
class Reviewer:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
    def review(self):
        print("Reviewer " + self.nama + " bertanggung jawab di kelas " + self.kelas)

        # KALO KELAS, HARUS PAKAI SELF, ITU BUKAN IDENTITAS FUNGSI,, ITU KETENTUAN KALAU MAU NAMBAHI KELAS