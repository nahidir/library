from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QFont

class Member_Dialog(object):

    def member_Ui(self, Dialog):
        Dialog.setObjectName("Form")
        Dialog.resize(400, 380)
        Dialog.setWindowTitle("Add Member")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName("centralWidget")
        Dialog.setCentralWidget(self.centralWidget)
        self.vBox = QVBoxLayout(self.centralWidget)
        self.vBox.setObjectName("vBox")

        self.lineEdit_id = QLineEdit(self.centralWidget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_id.setPlaceholderText("Please Enter Member ID")
        self.lineEdit_id.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_id.setFont(font)
        self.vBox.addWidget(self.lineEdit_id)

        self.lineEdit_name = QLineEdit(self.centralWidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_name.setPlaceholderText("Please Enter Member Name")
        self.lineEdit_name.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.vBox.addWidget(self.lineEdit_name)

        self.lineEdit_mobile = QLineEdit(self.centralWidget)
        self.lineEdit_mobile.setObjectName("lineEdit_mobile")
        self.lineEdit_mobile.setPlaceholderText("Please Enter Member Mobile")
        self.lineEdit_mobile.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_mobile.setFont(font)
        self.vBox.addWidget(self.lineEdit_mobile)

        self.lineEdit_email = QLineEdit(self.centralWidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_email.setPlaceholderText("Please Enter Member Email")
        self.lineEdit_email.setMaximumSize(390, 40)
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_email.setFont(font)
        self.vBox.addWidget(self.lineEdit_email)

        self.pushButton_inserMember = QPushButton(self.centralWidget)
        self.pushButton_inserMember.setObjectName("pushButton_insertMember")
        self.pushButton_inserMember.setText("Insert Member")
        font = QFont()
        font.setPointSize(14)
        self.pushButton_inserMember.setFont(font)
        self.pushButton_inserMember.setMaximumSize(130, 30)
        self.pushButton_inserMember.setStyleSheet(
            "QPushButton{\n""\n""background-color: grey;\n""color: white\n""\n""\n""}")
        self.vBox.addWidget(self.pushButton_inserMember)

        self.label_member = QLabel(self.centralWidget)
        self.label_member.setObjectName("label_member")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_member.setFont(font)
        self.vBox.addWidget(self.label_member)










