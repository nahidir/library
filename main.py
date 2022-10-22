
import sys
from PyQt6.QtWidgets import QApplication
from LibrarySystem import Library_system

app = QApplication(sys.argv)
library = Library_system()

sys.exit(app.exec())
