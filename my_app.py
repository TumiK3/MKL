from instr import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class Experiment():
  def __init__(self, age, test1, test2, test3):
    self.age = age
    self.t1 = test1
    self.t2 = test2
    self.t3 = test3
  
class MainWin(QWidget):
  
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
    self.hello_text = QLabel(txt_hello)
    self.instruction = QLabel(txt_instruction)
    self.button = QPushButton(txt_next)
    
    self.layout = QVBoxLayout()
    self.hello_text.addWidget(self.layout)
    self.instruction.addWidget(self.layout)
    self.button.addWidget(self.layout)
    
    self.setLayout(self.layout)
    
  def connects(self):
    self.button_next.clicked.connect(self.next_click)
    
  def next_click(self):
    self.hide()
    self.exp = Experiment(self.line_age.text(),self.line_test1.text(),
                          self.line_test2.text(),self.line_test3.text())
    self.tw =FinalWin(self.exp)
    self.tw = TestWin()
    
app = QApplication([])
mw= MainWin()
app.exec_()
