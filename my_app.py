from instr import *
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
  def connects(self):
    pass
