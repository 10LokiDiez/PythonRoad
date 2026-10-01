from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFontDatabase, QFont
import sys

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.label1 = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()
        
    def initUI(self):
        self.setGeometry(600,400,300,100)
        
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        self.setLayout(vbox)
        
        self.label1.setAlignment(Qt.AlignCenter)
        
        self.label1.setStyleSheet("""
                                  font-size: 150px;
                                  color: hsl(111,100%, 50%);
                                  """)
        self.setStyleSheet("background-color:black;")
        
        font_id = QFontDatabase.addApplicationFont(r"CURSO\PyQtCourse\last_proyrcts\digital_clock\DS-DIGIT.TTF")
        font_fam = QFontDatabase.applicationFontFamilies(font_id)[0]
        myfont = QFont(font_fam, 150)
        self.label1.setFont(myfont)
        
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        
    def update_time(self):
        timee = QTime.currentTime().toString("hh:mm:ss AP")
        self.label1.setText(timee)

        
    
def main():
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())
    timer()


if __name__ == "__main__":
    main()
    