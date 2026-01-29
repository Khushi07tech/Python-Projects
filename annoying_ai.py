import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import random
from annoying_gpt_responses import annoying_gpt_responses

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle ("AnnoyingGPT")
        self.setGeometry (450, 100, 500, 500)

        self.response = annoying_gpt_responses
        central_widget = QWidget(self)
        self.setCentralWidget (central_widget)
        self.button = QPushButton ("What's AI", central_widget)
        self.label = QLabel ("You tap, I answer!", central_widget)
        self.initUI()

        label1 = QLabel ("AnnoyingGPT", central_widget)
        label1.setAlignment(Qt.AlignCenter)
        label1.setGeometry(0, 20, 500, 80)
        label1.setFont(QFont("Times New Roman", 50))
        label1.setStyleSheet("font-weight: bold;")

        label2 = QLabel ("(aka primitive ChatGPT)", central_widget)
        label2.setAlignment(Qt.AlignCenter)
        label2.setGeometry(0, 90, 500, 40)
        label2.setFont(QFont("Arial", 10))
        label2.setStyleSheet("font-style: italic;")

    def initUI (self):
        self.button.setGeometry (150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect (self.on_click)

        self.label.setGeometry (50, 320, 400, 60)
        self.label.setStyleSheet("font-size: 15px;")

    def on_click (self):
        print ("Button Clicked!")
        response = random.choice (self.response)
        self.label.setText (response)
        self.button.setText ("Ask again")
        self.button.setDisabled (False)

def main ():
    app = QApplication(sys.argv)
    windows = MainWindow()
    windows.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main ()