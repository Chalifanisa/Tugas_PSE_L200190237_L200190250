#Q Dialog buat menampilkan window
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget
from PyQt5.uic import loadUi 
from PyQt5.QtCore import QSize

#untuk menampung dan mengatur tampilan pada sebuah class
from straightLine import straightLine
from sumOfFactor import sumOf as sumOfFactor
from reducing import reducingBalance
from unit import unitActivity



class home(QDialog):
    def __init__(self):
        super(home, self).__init__()
        loadUi('template/Home.ui', self)
        # Buat Signal, untuk membuat Event
        self.lbl_SL.mousePressEvent = self.SLWindow
        self.lbl_SOTY.mousePressEvent = self.SOTYWindow
        self.lbl_RB.mousePressEvent = self.RBWindow
        self.lbl_UOA.mousePressEvent = self.UOAWindow

    # Stright Line
    def SLWindow(self,event):
        # print("SL BTN RUN")
        StrighLine = straightLine()
        layout.addWidget(StrighLine)
        layout.setCurrentIndex(layout.currentIndex()+1)
        layout.show()

    def SOTYWindow(self,event):
        SumOfFactor = sumOfFactor()
        layout.addWidget(SumOfFactor)
        layout.setCurrentIndex(layout.currentIndex() + 1)
        layout.show()

    def RBWindow(self,event):
        reducing = reducingBalance()
        layout.addWidget(reducing)
        layout.setCurrentIndex(layout.currentIndex() + 1)
        layout.show()

    def UOAWindow(self,event):
        UnitActivity = unitActivity()
        layout.addWidget(UnitActivity)
        layout.setCurrentIndex(layout.currentIndex() + 1)
        layout.show()


#untuk menjalankan applikasi
app = QApplication([])
Home = home()

#menampung tampilan pada tumpukan
layout = QStackedWidget()

#untuk meletakan tumpukan
layout.addWidget(Home)

#untuk menetapkan ukuran window
layout.setFixedSize(QSize(800, 500))

#untuk memunculkan tampilan
layout.show()

#untuk menjalankan applikasi
app.exec()
