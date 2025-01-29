from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTimer

class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title) 
        self.resize(win_width, win_height)  
        self.move(win_x, win_y) 

    def initUI(self):
        
        self.btn1 = QPushButton('Start') 
        self.timer = QTimer(self)  
        
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        
        self.l_line.addWidget(self.btn1)
        self.r_line.addWidget(self.timer)
        
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        
        self.setLayout(self.h_line)

    def connects(self):
       
        self.btn1.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        self.fw = FinalWin()
        
    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss"))
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString("hh:mm:ss")[6:8])
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        if innt(time.toString('hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStyleSheet("color: rgb(0,255,0)")
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
            
def connects(self):
    self.btn_next.clicked.connect(self.next_click)
    self.btn_test1.clicked.connect(self.timer_test)
    self.btn_test2.clicked.connect(self.timer_sits)
    self.btn_test3.clicked.connect(self.timer_final)

app = QApplication([])
tw = TestWin()
app.exec_()
