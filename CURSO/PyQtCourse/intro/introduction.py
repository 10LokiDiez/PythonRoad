import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #METODO PARA ESTABLECER TITULO
        self.setWindowTitle("Mi primer GUI")
        # DEFINIR GEOMETRIA X,Y, WEIGHT,HEIGHT
        self.setGeometry(700,300, 500 , 500)
        # ESTABLECER EL ICONO
        self.setWindowIcon(QIcon(r"C:\Users\sidim\Escritorio\Programacion IV\CURSO\PyQtCourse\intro\favicon.jpg"))
    
def main():
    #Estudiar sys.argv
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()