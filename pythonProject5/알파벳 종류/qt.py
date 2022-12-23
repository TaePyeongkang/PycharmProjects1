import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit,QMessageBox
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('ID',self)
        # label1.setAlignment(Qt.AlignHCenter)
        label1.move(20,50)

        label2 = QLabel('Password',self)
        # label2.setAlignment(Qt.AlignHCenter)
        label2.move(20, 100)

        label3 = QLabel('Password check',self)
        # label3.setAlignment(Qt.AlignHCenter)
        label3.move(20, 150)

        qle1 = QLineEdit(self)
        qle1.move(200,50)

        qle2 = QLineEdit(self)
        qle2.move(200, 100)

        qle3 = QLineEdit(self)
        qle3.move(200, 150)

        btn1 = QPushButton('가입', self)
        btn1.clicked.connect(self.complete)
        btn1.move(100,200)

        btn2 = QPushButton('취소', self)
        btn2.move(200, 200)

        self.setWindowTitle('QLabel')
        self.setGeometry(300,300,600,400)
        self.show()

    def complete(self):
        QMessageBox.information(self, '가입확인창', '가입되었습니다')
        # 어렵구먼,,


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())