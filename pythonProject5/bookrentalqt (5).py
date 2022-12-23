import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5 import Qt
from PyQt5.QtCore import pyqtSlot
import csv
from PyQt5.QtCore import QDate, Qt
now = QDate.currentDate()
to = QDate.currentDate().addDays(7)
form_widget = uic.loadUiType('borrow.ui')[0]

class Rental_page(QWidget, form_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        f = open('cheomdan.csv', 'rt', encoding='UTF8')  # 읽어올 파일.
        self.rdr = csv.reader(f)
        self.csv_list = []
        for line in self.rdr:
            self.csv_list.append(line)
        f.close()
        # print(self.csv_list)
        self.YH_reset.clicked.connect(self.clear)
        self.YH_search.clicked.connect(lambda:self.song())
        # self.YH_rent.clicked.connect(self.Information_event)              # 대여 알림창 일단 보류
        self.YH_lineEdit.textChanged.connect(self.lineeditTextFunction)
        self.YH_lineEdit.returnPressed.connect(self.printTextFunction)
        self.YH_main.setColumnWidth(0, 40)
        self.YH_main.setColumnWidth(1, 80)
        self.YH_main.setColumnWidth(2, 300)
        self.YH_main.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.YH_main.selectionModel().selectedRows()
        self.YH_main.cellClicked.connect(self.CellValue)
        self.YH_rent.clicked.connect(self.Bookrental)


    def CellValue(self,row,column):
        item = self.YH_main.item(row, column)
        value = item.text()
        label_string = str(value)
        self.YH_label2.setText(label_string)  # 셀의 내용 가져오기
        b = self.testList[row]
        self.b = b

    def Bookrental(self):  # 도서 대여 csv 추가
        f = open('bookrental.csv', 'a', newline = '\n', encoding='utf-8')
        csv_writer = csv.writer(f)
        self.b.append(now.toString(Qt.ISODate))  # 대출일 추가
        self.b.append(to.toString(Qt.ISODate))   # 반납일 추가
        self.b.append('loginpage.id')            # 아이디 추가
        csv_writer.writerow(self.b)
        f.close()

    def lineeditTextFunction(self) :                                   # 도서명 검색하기위해 사용하는 함수
        self.YH_lineEdit.setText(self.YH_lineEdit.text())              # lineEdit에 입력할수 있도록

    def printTextFunction(self) :                                      # LineEdit에서 Return키(Enter키)가 눌렸을 때 기능 실행.
        print(self.YH_lineEdit.text())

    def clear(self):                                                   # 초기화 버튼과 연결해서 초기화 버튼 눌렀으때 테이블위젯에 나온 자료 전부 제거하는 함수.
        self.YH_main.clearContents()

    # def Information_event(self):                                      # 도서 대출할때 사용할 함수.
    #     buttonReply = QMessageBox.information(                        # 메세지 박스를 통해서 알림창 생성하기  yes와 cancel로 대출 할지 여부 파악하기.
    #         self, '도서 대여 시스템', '도서를 대여하시겠습니까?',
    #         QMessageBox.Yes | QMessageBox.Cancel  )
    #
    #     if buttonReply == QMessageBox.Yes:
    #         print('도서를 대여합니다.')
    #     elif buttonReply == QMessageBox.Cancel:
    #         print('취소하셨습니다.')

    def song(self):  # 수정중
        self.YH_main.clearContents()  # 처음에 테이블 위쳇 초기화 시키고 시작.
        testList = []  # 빈리스트를 생성하기.(검색창에 검색하면 빈리스트에 추가하기위해서)
        test = self.YH_lineEdit.text()  # 검색창에 검색하면 그 검색한게 test안으로 들어가게힘.
        for line in self.csv_list:
            if test in line[5] or test in line[4]:
                if '도서명' in line[5]:
                    continue
                testList.append(line)

        self.YH_main.setRowCount(len(testList))
        Row = 0
        # implist = ['Why 한국사. 20, 신분과 직업','(1·2학년)동시','Why 세계사. 7, 동아시아 전통사회의 발전','Why 한국사. 1, 나라의 시작','Why 한국사. 2, 삼국의 경쟁'
        #            ,'Why 한국사. 3, 고려시대','Why 한국사. 4, 조선전기','Why 한국사. 5, 조선후기']
        for k in testList:
            self.YH_main.setItem(Row, 0, QTableWidgetItem(k[0]))  # 연번
            self.YH_main.setItem(Row, 1, QTableWidgetItem(k[1]))  # 도서관 이름
            self.YH_main.setItem(Row, 2, QTableWidgetItem(k[4]))  # 도서명
            self.YH_main.setItem(Row, 3, QTableWidgetItem(k[5]))  # 지은이
            self.YH_main.setItem(Row, 4, QTableWidgetItem(k[3]))  # 등록번호

            for i in range(len(self.bookrental)):
                if self.bookrental[i] in k[4]:
                    self.YH_main.setItem(Row, 5, QTableWidgetItem('X'))
                    break

                elif self.bookrental[i] not in k[4]:
                    self.YH_main.setItem(Row, 5, QTableWidgetItem('O'))
                    continue

            Row += 1

if __name__ == "__main__" :
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = Rental_page()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(768)
    widget.setFixedWidth(1024)
    widget.show()
    app.exec_()



