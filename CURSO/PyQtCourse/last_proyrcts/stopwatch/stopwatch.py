import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QLabel,QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0,0,0)
        self.label1 = QLabel("00:00:00.00", self)
        self.startbutton = QPushButton("Start", self)
        self.stopbutton = QPushButton("Stop", self)
        self.resetbutton = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.setWindowTitle("Stop Watch")
        self.initUI()
    
    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        self.setLayout(vbox)
        
        self.label1.setAlignment(Qt.AlignCenter)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.startbutton)
        hbox.addWidget(self.stopbutton)
        hbox.addWidget(self.resetbutton)
        vbox.addLayout(hbox)
        
        self.setStyleSheet("""
            QPushButton, Qlabel{
                font-family: Calibri;
                padding:20px;
                font-weight:bold;
            }
            QPushButton{
                font-size:30px;
            }                   
            QLabel{
                font-size:120px;
                background-color: #c9f5f4;
                border-radius: 20px;
            }
                           
        """)
        
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)
        self.resetbutton.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_display)
        
    def start(self):
        self.timer.start(10)
    
    def stop(self):
        self.timer.stop()
        
    def reset(self):
        self.timer.stop()
        self.time = QTime(0,0,0,0)
        self.label1.setText(self.format_time(self.time))
    
    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milli = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milli:02}"
    
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.label1.setText(self.format_time(self.time))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())