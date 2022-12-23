import sys
import csv
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("booksearch.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class BooksearchClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        # ui 불러오기, 객체 생성
        self.setupUi(self)
        f = open('jangdeok.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        self.csv_list = []
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        f = open('cheomdan.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        f = open('singa.csv', 'rt', encoding='cp949')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        f = open('taleflower.csv', 'rt', encoding='cp949')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        f = open('Rent_list.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        self.bookrental = []
        for line in self.rdr:
            self.bookrental.append(line)
        f.close()
        # stack의 페이지를 첫번째 페이지로 고정한다
        self.stackedWidget.setCurrentIndex(0)
        # 버튼의 클릭이벤트와 함수를 연결해준다
        self.btn_search.clicked.connect(self.MoveBooklistpage)
        self.btn_back_search.clicked.connect(self.MoveSearchpage)
        self.btn_main.clicked.connect(self.MoveMainPage)
        self.btn_main2.clicked.connect(self.MoveMainPage)
        self.btn_search.clicked.connect(self.searchlist)
        self.bookname.textChanged.connect(self.booknameTextFunction)
        self.bookname.returnPressed.connect(self.printTextFunction)
        self.bookpublisher.textChanged.connect(self.bookpublisherTextFunction)
        self.bookpublisher.returnPressed.connect(self.printTextFunction)
        self.bookwriter.textChanged.connect(self.bookwriterTextFunction)
        self.bookwriter.returnPressed.connect(self.printTextFunction)


    def MoveBooklistpage(self):
        self.stackedWidget.setCurrentIndex(1)

    def MoveSearchpage(self):
        self.stackedWidget.setCurrentIndex(0)

    def MoveMainPage(self):
        # print("btn_Firstpage clicked")
        self.parent().setCurrentIndex(0)

    def booknameTextFunction(self):
        self.bookname.setText(self.bookname.text())

    def bookpublisherTextFunction(self):
        self.bookpublisher.setText(self.bookpublisher.text())

    def bookwriterTextFunction(self):
        self.bookwriter.setText(self.bookwriter.text())

    def printTextFunction(self):
        print(self.bookname.text())
        print(self.bookpublisher.text())
        print(self.bookwriter.text())

    def searchlist(self):
        book = []
        bookname = self.bookname.text()
        bookpublisher = self.bookpublisher.text()
        bookwriter = self.bookwriter.text()

        for line in self.csv_list:
            if '도서명' == line[4]:
                continue
            elif bookname in line[4] and bookpublisher in line[6] and bookwriter in line[5]:
                book.append(line)

        self.booksearchlist.setRowCount(len(book))
        Row = 0
        # Row = Row - 1
        for x in book:
            self.booksearchlist.setItem(Row, 0, QTableWidgetItem(x[0]))    # 연번
            self.booksearchlist.setItem(Row, 1, QTableWidgetItem(x[4]))    # 제목
            self.booksearchlist.setItem(Row, 2, QTableWidgetItem(x[5]))    # 저자
            self.booksearchlist.setItem(Row, 3, QTableWidgetItem(x[6]))    # 출판사
            self.booksearchlist.setItem(Row, 4, QTableWidgetItem(x[1]))    # 소장도서관
            self.booksearchlist.setItem(Row, 5, QTableWidgetItem(x[3]))    # 등록번호
            self.booksearchlist.setItem(Row, 6, QTableWidgetItem(x[8]))    # 청구기호
            self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출가능'))
            self.booksearchlist.setItem(Row, 8, QTableWidgetItem('-'))

            for i in range(len(self.bookrental)):
                if self.bookrental[i][4] in x[4]:
                    self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출불가능'))
                    self.booksearchlist.setItem(Row, 8, QTableWidgetItem(self.bookrental[i][11]))
                    break
                elif self.bookrental[i][1] != x[1]:
                    self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출불가능(타도서관)'))
                elif self.bookrental[i][4] not in x[4]:
                    self.booksearchlist.setItem(Row, 7, QTableWidgetItem('대출가능'))
                    continue

            Row = Row + 1

if __name__ == "__main__" :
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = BooksearchClass()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()









