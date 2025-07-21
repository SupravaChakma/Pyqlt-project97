import sys
import re
import pandas as pd
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTreeView, QTableView, QLineEdit,QTextEdit
from PyQt6.QtGui import  QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Explorer - For Personal (Non-Commercial) Use Only!")
        self.setWindowIcon(QIcon("assets/dfsql_icon.png"))
        self.setGeometry(100, 100, 900, 450)
        
        # Add a status bar as footer
        self.status = self.statusBar()
        #self.status.showMessage("This is the footer text.")
        
        # Create main widgets
        self.tree_view = QTreeView()
        self.query_input = QLineEdit()
        self.query_input.setText("database explorer")
        self.query_input.setReadOnly(True)
        self.querytext_input = QTextEdit()
        self.result_table = QTableView()
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        # Set the central widget of the Window.
        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())