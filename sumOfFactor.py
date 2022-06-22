#Q Dialog buat menampilkan window
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.uic import loadUi 
from PyQt5.QtCore import QSize
from rumus import rumus

#untuk menampung dan mengatur tampilan pada sebuah class
class sumOf(QDialog):
    def __init__(self):
        super(sumOf, self).__init__()
        loadUi('template/SOTY.ui', self)
        self.btn_Hitung.clicked.connect(self.prosesHitung)
        self.Rumus = rumus()

    def prosesHitung(self):
        print("TEST")
        data = {"harga": int(self.le_Harga.text()),
                "nilaiResidu": int(self.le_Nilai.text()),
                "usiaEkonomis": int(self.le_Usia.text())}
        self.le_Hasil.setText(str(self.Rumus.sumOfTheYear(data)))




