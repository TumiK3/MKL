from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
class FinalWin(QWidget):
  def __init__(self):
    super().__init__()
    self.set_appear()
    self.initUI()
    self.show()

  def __init__(self,exp):
    self.exp = exp

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

app = QApplication([])
fw = FinalWin()
app.exec_()
