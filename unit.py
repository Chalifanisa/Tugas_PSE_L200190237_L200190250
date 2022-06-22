#Q Dialog buat menampilkan window
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.uic import loadUi
from main import home 
from rumus import rumus

#untuk menampung dan mengatur tampilan pada sebuah class
class unitActivity(QDialog):
    def __init__(self):
        super(unitActivity, self).__init__()
        loadUi('template/UOA.ui', self)
        self.btn_Hitung.clicked.connect(self.prosesHitung)
        self.Rumus = rumus()

    def prosesHitung(self):
        print("TEST")
        data = {"harga": int(self.le_Harga.text()),
                "nilaiResidu": int(self.le_Nilai.text()),
                "pemakaian": int(self.le_Pemakaian.text()),
                "kapasitas": int(self.le_Kapasitas.text())}
        self.le_Hasil.setText(str(self.Rumus.unitOfActivity(data)))
