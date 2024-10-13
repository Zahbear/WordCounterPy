# word_counter_gui.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QTextEdit, QMessageBox
from shared_functions import display_file_contents, load_file_contents, analyze_word_count  # Import from shared_functions

class WordCounterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.file_contents = None  # Variable to store file contents

    def init_ui(self):
        self.setWindowTitle('Word Counter with GUI Menu')

        # Setting UI window side
        self.resize(800, 600)

        # Create buttons
        self.presentation_button = QPushButton('1. Presentation', self)
        self.load_file_button = QPushButton('2. Load File', self)
        self.analyze_button = QPushButton('3. Analyze Word Count', self)
        self.exit_button = QPushButton('0. Exit', self)

        # Connect buttons to their functions
        self.presentation_button.clicked.connect(self.display_presentation)
        self.load_file_button.clicked.connect(self.load_file)
        self.analyze_button.clicked.connect(self.analyze_word_count)
        self.exit_button.clicked.connect(self.exit_application)

        # Create a text area for displaying content
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)

        # Arrange widgets using a vertical layout
        layout = QVBoxLayout()
        layout.addWidget(self.presentation_button)
        layout.addWidget(self.load_file_button)
        layout.addWidget(self.analyze_button)
        layout.addWidget(self.exit_button)
        layout.addWidget(self.text_area)

        self.setLayout(layout)

    def display_presentation(self):
        contents = display_file_contents('.version.txt')  # Use the existing function
        self.text_area.setPlainText(contents)

    def load_file(self):
        # Open file dialog and load contents
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt);;All Files (*)', options=options)
        if filename:
            self.file_contents = load_file_contents(filename)  # Storing contents in the instance variable
            if self.file_contents is not None:
                self.text_area.setPlainText(f"File '{filename}' loaded successfully. Can be analyzed.")
            else:
                QMessageBox.critical(self, "Error", "Could not load file contents.")

    def analyze_word_count(self):
        if self.file_contents is None:
            # Display a dialo box asking if they want to add a file
            reply = QMessageBox.question(self, 'No File Loaded', 
                                            "No file is loaded, do you want to load a file?", 
                                            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.load_file()  # Open file dialog
            elif reply == QMessageBox.No:
                
                # Use default 'input.txt'
                QMessageBox.information(self, "Default File",
                                            "No file selected. Using default 'input.txt' file.")
                self.file_contents = load_file_contents('input.txt')

        if self.file_contents is not None:
            result = analyze_word_count(self.file_contents)  # Passing file contents for analysis
            self.text_area.setPlainText(f"Analysis Result:\n{result}")  # Display the analysis result
        else: 
            QMessageBox.warning(self, "Warning", "No file loaded for analysis.")

    def exit_application(self):
        QApplication.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WordCounterApp()
    window.show()
    sys.exit(app.exec_())
