import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("LINE EDITS")
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()
        
    def initUI(self):
        self.line_edit.setGeometry(10,10,250,40)
        self.line_edit.setStyleSheet("font-size:25px;"
                                     "font-family:Arial;")
        self.line_edit.setPlaceholderText("Ingresa tu nombre")
        
        self.button.setGeometry(270,10,100,40)
        self.button.setStyleSheet("font-size:25px;"
                                  "font-family:Arial;")
        
        self.button.clicked.connect(self.submit)

    def submit(self):
        print(f"El texto escrito es {self.line_edit.text()}")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()