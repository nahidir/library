import sys
from PyQt6.QtWidgets import QMainWindow, QDialog, QApplication
from AddBook import Book_Dialog
from MainGui import Ui_MainWindow
from AddMember import Member_Dialog
from ViewBooks import ViewBooks_Dialog
from ViewMembers import ViewMembers_Dialog

class Library_system(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setup_Ui(self)
        self.show()

        self.button_addBook.clicked.connect(self.add_book)
        self.button_addMember.clicked.connect(self.add_member)
        self.button_viewBooks.clicked.connect(self.view_books)
        self.button_viewMembers.clicked.connect(self.view_members)



    def add_book(self):

        self.window_book = QMainWindow()
        ui = Book_Dialog()
        ui.book_Ui(self.window_book)
        self.window_book.show()


    def add_member(self):
        self.window_member = QMainWindow()
        ui = Member_Dialog()
        ui.member_Ui(self.window_member)
        self.window_member.show()

    def view_books(self):
         self.window_viewBooks = QMainWindow()
         ui = ViewBooks_Dialog()
         ui.viewBooks_Ui(self.window_viewBooks)
         self.window_viewBooks.show()

    def view_members(self):
        self.window_viewMembers = QMainWindow()
        ui = ViewMembers_Dialog()
        ui.viewMembers_Ui(self.window_viewMembers)
        self.window_viewMembers.show()
