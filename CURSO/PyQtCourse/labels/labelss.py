import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.setWindowTitle("PROGRAMA LABELS")
        
        letra = QLabel("Hola, como estas?", self)
        letra.setFont(QFont("Times new roman", 30))
        letra.setGeometry(0,0,500,100)
        #Es como un CSS
        letra.setStyleSheet("color: #8d42f5;"
                            "background-color: #fcf9f0;"
                            "font-weight: bold;"
                            "font-style: italic;")
        
        #letra.setAlignment(Qt.AlignTop) #AlignBottom AlignRight, AlignLeft
        #letra.setAlignment(Qt.AlignVCenter)
        #letra.setAlignment(Qt.AlignHCenter)
        #letra.setAlignment(Qt.AlignCenter) # CENTER Y CENTER
        letra.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
    
if __name__ == "__main__":
    main()