#Q Dialog buat menampilkan window
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.uic import loadUi 
from rumus import rumus

#untuk menampung dan mengatur tampilan pada sebuah class
class reducingBalance(QDialog):
    def __init__(self):
        super(reducingBalance, self).__init__()
        loadUi('template/RB.ui', self)
        self.btn_Hitung.clicked.connect(self.prosesHitung)
        self.Rumus = rumus()


    def prosesHitung(self):
        print("TEST")
        data = {"harga": int(self.le_Harga.text()),
                "nilaiResidu": int(self.le_Nilai.text()),
                "rate": int(self.le_Rate.text())}
        self.le_Hasil.setText(str(self.Rumus.reducingBalance(data)))

