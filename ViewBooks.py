from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QTableWidgetItem, QTableWidget
from PyQt6.QtGui import QFont

class ViewBooks_Dialog(object):
    def viewBooks_Ui(self, Dialog):
        Dialog.setObjectName("Form")
        Dialog.resize(650 , 450)
        Dialog.setWindowTitle("View Book")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName("centralWidget")
        Dialog.setCentralWidget(self.centralWidget)
        self.vBox = QVBoxLayout(self.centralWidget)
        self.vBox.setObjectName("vBox")

        self.table_viewBook = QTableWidget(self.centralWidget)
        self.table_viewBook.setObjectName("table_viewBook")
        font = QFont()
        font.setPointSize(12)
        self.table_viewBook.setFont(font)
        self.table_viewBook.setStyleSheet("QTableWidget{\n""\n""background-color:rgb(218, 218,218)\n""\n""}")
        self.table_viewBook.setRowCount(0)
        self.table_viewBook.setColumnCount(5)
        self.table_viewBook.setHorizontalHeaderItem(0 , QTableWidgetItem("Title"))
        self.table_viewBook.setHorizontalHeaderItem(1, QTableWidgetItem("ID"))
        self.table_viewBook.setHorizontalHeaderItem(2, QTableWidgetItem("Author"))
        self.table_viewBook.setHorizontalHeaderItem(3, QTableWidgetItem("Publisher"))
        self.table_viewBook.setHorizontalHeaderItem(4, QTableWidgetItem("Available"))
        self.vBox.addWidget(self.table_viewBook)

        self.pushButton_viewBook = QPushButton(self.centralWidget)
        self.pushButton_viewBook.setObjectName("pushButton_viewBook")
        self.pushButton_viewBook.setText("View Book")
        font = QFont()
        font.setPointSize(14)
        self.pushButton_viewBook.setFont(font)
        self.pushButton_viewBook.setStyleSheet("QPushButton{\n""\n""background-color:rgb(218, 218, 218)\n""\n""}")
        self.vBox.addWidget(self.pushButton_viewBook)


