from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


#def interfejs()
	#self.setLayout(uklatT)
	koniecBtn.clicked.connect(self.koniec)


def koniec(self):
        self.close()

def closeEvent(self, event):

        odp = QMessageBox.question(
            self, 'Komunikat',
            "Czy na pewno koniec?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()