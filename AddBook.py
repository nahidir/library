from PyQt6.QtWidgets import QWidget, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
import  mysql.connector as mc

class Book_Dialog(object):
     def book_Ui(self, Dialog ):
        Dialog.setObjectName("Form")
        Dialog.resize(400,380)
        Dialog.setWindowTitle("Add Book")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName("centralWidget")
        Dialog.setCentralWidget(self.centralWidget)
        self.vBox = QVBoxLayout(self.centralWidget)
        self.vBox.setObjectName("vBox")

        self.lineEdit_title = QLineEdit(self.centralWidget)
        self.lineEdit_title.setObjectName("lineEdt_title")
        self.lineEdit_title.setPlaceholderText("Please Enter Title")
        self.lineEdit_title.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_title.setFont(font)
        self.vBox.addWidget(self.lineEdit_title)

        self.lineEdit_id = QLineEdit(self.centralWidget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_id.setPlaceholderText("Please Enter ID")
        self.lineEdit_id.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.vBox.addWidget(self.lineEdit_id)

        self.lineEdit_author = QLineEdit(self.centralWidget)
        self.lineEdit_author.setObjectName("lineEdit_dialog")
        self.lineEdit_author.setPlaceholderText("Please Enter Author")
        self.lineEdit_author.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_author.setFont(font)
        self.vBox.addWidget(self.lineEdit_author)

        self.lineEdit_publisher = QLineEdit(self.centralWidget)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.lineEdit_publisher.setPlaceholderText("Please Enter Publisher")
        self.lineEdit_publisher.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_publisher.setFont(font)
        self.vBox.addWidget(self.lineEdit_publisher)

        self.pushButton_inserBook = QPushButton(self.centralWidget)
        self.pushButton_inserBook.setObjectName("pushButton_insertBook")
        self.pushButton_inserBook.setText("Insert Book")
        font = QFont()
        font.setPointSize(14)
        self.pushButton_inserBook.setFont(font)
        self.pushButton_inserBook.setMaximumSize(110, 30)
        self.pushButton_inserBook.setStyleSheet("QPushButton{\n""\n""background-color: grey;\n""color: white\n""\n""\n""}")
        self.vBox.addWidget(self.pushButton_inserBook)
        self.pushButton_inserBook.clicked.connect(self.insert_book)

        self.label_result = QLabel(self.centralWidget)
        self.label_result.setObjectName("label_result")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_result.setFont(font)
        self.vBox.addWidget(self.label_result)

     def insert_book(self):
        try:
           my_db = mc.connect(
              host="localhost",
              user="root",
              password="",
              database = "library"
           )
           title = self.lineEdit_title.text()
           id = self.lineEdit_id.text()
           author = self.lineEdit_author.text()
           publisher = self.lineEdit_publisher.text()
           if title=="" or id=="" or author=="" or publisher=="":
              self.label_result.text("Please fill the filed")
              self.label_result.setStyleSheet("color: red")
              return
           myCursor = my_db.cursor()
           query = "INSERT INTO tbl_library(title, id, author, publisher) VALUES(%s, %s, %s, %s)"
           values = (title, id, author, publisher)
           myCursor.execute(query, values)
           my_db.commit()
           self.label_result.text("data addes successfully")
           self.label_result.setStyleSheet("color: green")

        except mc.Error as e:
            self.label_result.text("not Correct")
            self.label_result.setStyleSheet("color: red")
