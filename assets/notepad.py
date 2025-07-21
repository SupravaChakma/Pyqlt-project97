import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter,QTextEdit, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon,QAction,QFileSystemModel
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon("assets/notepad.jpeg"))
        self.setGeometry(100, 100, 900, 450)
        
        
        # Add a status bar as footer
        self.status = self.statusBar()
        #self.status.showMessage("This is the footer text.")
        
        # Create main widgets
        self.querytext_input = QTextEdit()

        # Setup main layout
        splitter = QSplitter(Qt.Orientation.Vertical)

        panel = QWidget()
        layout = QVBoxLayout(panel)
        layout.addWidget(self.querytext_input)
        splitter.addWidget(panel)
        
        splitter.setSizes([300, 900])
        self.setCentralWidget(splitter)
     
        self._create_actions()
        self._create_menu()

    def _create_actions(self):
        self.new_action = QAction("New", self)
        self.new_action.triggered.connect(self.new_file)
        
        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.save_file)
        

    def _create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")
        file_menu.addAction(self.new_action)
        
        actions_menu = menubar.addMenu("&Open")
        actions_menu.addAction(self.open_action)
        
        about_menu = menubar.addMenu("&Save")
        about_menu.addAction(self.save_action)

    def new_file(self):
        self.querytext_input()
        self.setWindowTitle("Untitled - Notepad")

    def open_file(self):
        self.querytext_input()
        self.setWindowTitle("Untitled - Notepad")
    
    def save_file(self):
        self.querytext_input = None
        self.setWindowTitle("Untitled - Notepad")
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())