from PyQt6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout
from PyQt6.QtGui import QFont

class ViewMembers_Dialog(object):
    def viewMembers_Ui(self, Dialog):
        Dialog.setObjectName("Form")
        Dialog.resize(650, 450)
        Dialog.setWindowTitle("View Members")
        self.centralWidget = QWidget(Dialog)
        self.centralWidget.setObjectName("centralWidget")
        Dialog.setCentralWidget(self.centralWidget)

        self.vBox = QVBoxLayout(self.centralWidget)
        self.vBox.setObjectName("vBox")

        self.table_viewMembers = QTableWidget(self.centralWidget)
        self.table_viewMembers.setObjectName("table_viewMembers")
        self.table_viewMembers.setRowCount(0)
        self.table_viewMembers.setColumnCount(4)
        font = QFont()
        font.setPointSize(12)
        self.table_viewMembers.setFont(font)
        self.table_viewMembers.setStyleSheet("QTableWidget{\n""\n""background-color:rgb(218, 218, 218)\n""\n""}")
        self.table_viewMembers.setHorizontalHeaderItem(0, QTableWidgetItem("ID"))
        self.table_viewMembers.setHorizontalHeaderItem(1, QTableWidgetItem("Name"))
        self.table_viewMembers.setHorizontalHeaderItem(2, QTableWidgetItem("Mobile"))
        self.table_viewMembers.setHorizontalHeaderItem(3, QTableWidgetItem("Email"))
        self.vBox.addWidget(self.table_viewMembers)

        self.pushButton_viewMembers = QPushButton(self.centralWidget)
        self.pushButton_viewMembers.setObjectName("pushButton_viewMembers")
        self.pushButton_viewMembers.setText("View Members")
        font = QFont()
        font.setPointSize(12)
        self.pushButton_viewMembers.setFont(font)
        self.pushButton_viewMembers.setStyleSheet("QPushButton{\n""\n""background-color:rgb(218, 218, 218)\n""\n""}")
        self.vBox.addWidget(self.pushButton_viewMembers)

