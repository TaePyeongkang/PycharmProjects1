from PyQt5 import QtCore, QtWidgets


class MainForm(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.show()

    def closeEvent(self, event):
        message = QtWidgets.QMessageBox.question(self, "Question", "Are you sure you want to quit?")
        if message == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainForm()
    sys.exit(app.exec_())
