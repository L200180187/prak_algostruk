class Manusia(object):
    """class 'Manusia' dengan inisiasi 'nama'"""
    keadaan = "lapar"
    def __init__(self, nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salam, namaku ",self.nama)
    def makan(self, s):
        print("Saya baru saja makan ", s)
        self.keadaan = 'kenyang'
    def olahraga(self, k):
        print("Saya baru saja latihan ", k)
        self.keadaan = 'lapar'
    def mengalikanDenganDua(self, n):
        return n * 2

class Mahasiswa(Manusia):
    """Class Mahasiswa yang dibangun dari class Manusia."""
    def __init__(self, nama, NIM, kota, us):
        """Metode inisiasi ini menutupi metode inisiasi di class Manusia"""
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + ' tiap bulannya.'
        return s
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku
    def makan(self, s):
        """Metode ini menutupi metode 'makan'-nya class manusia.
           Mahasiswa kalau makan sambil belajar."""
        print("Saya baru saja makan", s, "Sambil belajar.")
        self.keadaan = 'kenyang'
#no2
#a
    def ambilKotaTinggal(self):
        return self.kotaTinggal
#b
    def perbaruiKotaTinggal(self, ubah):
        self.kotaTinggal = ubah
#c
    def TambahUangSaku(self, tambah):
        self.uangSaku += tambah
#no3
print("Masukkan Data Mahasiswa Disini :")
a = input("Nama      : ")
b = input("NIM       : ")
c = input("Asal      : ")
d = input("Uang Saku : ")
maha = Mahasiswa(a, b, c, d)
print("""Silahkan Ketik 'maha.instruksi' untuk menjalankan program yang
kalian inginkan.""")

#no4
  listKuliah = []
  def ambilKuliah(self, kuliah):
        self.listKuliah.append(kuliah)
#no5
  def hapusKuliah(self, hapus): 
        self.listKuliah.remove(hapus)
#no6
class SiswaSMA(Manusia):
    def __init__(self, nama, sekolah, alamat, uangSaku):
        self.nama = nama
        self.sekolah = sekolah
        self.uangSaku = uangSaku
        self.alamat = alamat
    def __str__(self):
        a = 'Nama      : ' + str(self.nama) + '\n' \
            + 'Sekolah      : ' + str(self.sekolah) + '\n' \
            + 'Uang Saku : ' + str(self.uangSaku)  + '\n' \
            + 'Alamat    : ' + str(self.alamat)
            
        return a
       
     


