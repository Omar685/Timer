"""
Auther: Omar Mohammed
Github: https://github.com/Omar685
copyright ©
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt

class TimerApp(QWidget):
  def __init__(self):
    super().__init__()

    self.minutes = 90
    self.seconds = 0

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_timer)
    self.total_seconds = 5400  # 90 minutes * 60 seconds
    self.remaining_seconds = self.total_seconds

    self.initUI()

  def initUI(self):
    self.setWindowTitle('Timer')
    self.setGeometry(100, 100, 200, 100)
    self.setStyleSheet("background-color: #000000; color: #ffffff;")

    # إعداد واجهة المستخدم
    self.layout = QVBoxLayout()

    self.time_label = QLabel(f'{str(self.minutes)}:{str(self.seconds)}0', self)
    self.time_label.setAlignment(Qt.AlignCenter)
    self.time_label.setStyleSheet("font-size: 80px;")
    self.layout.addWidget(self.time_label)

    self.setLayout(self.layout)

    self.resize(700, 500)

    # إعداد المؤقت
    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_timer)

        

  def start_timer(self):
    if not self.timer.isActive():
      self.total_seconds = self.minutes * 60 + self.seconds
      self.update_label()
      self.timer.start(1000)  # 1 second interval


  def stop_timer(self):
    self.timer.stop()
  
  def update_timer(self):
    if self.remaining_seconds > 0:
      self.remaining_seconds -= 1
      self.update_label()
    else:
      self.timer.stop()
      self.time_label.setText("Finshed")

  def update_label(self):
    minutes = self.remaining_seconds // 60
    seconds = self.remaining_seconds % 60
    self.time_label.setText(f'{minutes:02}:{seconds:02}')
  
  def reset_timer(self):
    self.timer.stop()
    self.remaining_seconds = self.total_seconds
    self.update_label()
  
  def break_timer(self):
    if not self.timer.isActive():
      self.remaining_seconds = 1800  # 30 minutes * 60 seconds
      self.update_label()
      self.timer.start(1000)  # 1 second interval

  
  def color_white(self):
    self.setStyleSheet("background-color: #ffffff; color: #000000;")
  def color_black(self):
    self.setStyleSheet("background-color: #000000; color: #ffffff;")
    

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
      self.start_timer()
    elif event.key() == Qt.Key.Key_Tab:
      self.stop_timer()
    elif event.key() == Qt.Key.Key_Escape:
      sys.exit()
    elif event.key() == Qt.Key.Key_F11:
      if self.isFullScreen():
        self.showNormal()
      else:
        self.showFullScreen()
    elif event.key() == Qt.Key.Key_R:
      self.reset_timer()
    elif event.key() == Qt.Key.Key_B:
      self.break_timer()
    elif event.key() == Qt.Key.Key_Alt:
      self.color_white()
    elif event.key() == Qt.Key.Key_Shift:
      self.color_black()
            
        

if __name__ == '__main__':
  app = QApplication(sys.argv)
  timer_app = TimerApp()
  timer_app.showFullScreen()
  sys.exit(app.exec_())