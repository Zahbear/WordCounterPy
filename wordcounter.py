# wordcounter.py

import sys
import os
from PyQt5.QtWidgets import QApplication  # Import QApplication here
from word_counter_gui import WordCounterApp  # Import the GUI
from shared_functions import display_file_contents, load_file_contents, analyze_word_count  # Import from shared_functions

file_contents = None

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Presentation")
        print("2. Load File")
        print("3. Analyze Word Count")
        print("0. Exit")
        choice = input("Choose an option: ")
        handle_menu_choice(choice)

def handle_menu_choice(choice):
    if choice == "1":
        display_presentation()
    elif choice == "2":
        file_path = load_file()
        file_contents = load_file_contents(file_path)
    elif choice == "3":
        analyze_word_count()
    elif choice == "0":
        exit_application()
    else:
        print("Invalid choice. Please try again.")

def display_presentation():
    print(display_file_contents('.version.txt')) # Display Presentation + version

def exit_application():
    print("Exiting application")
    exit()

def launch_gui():
    app = QApplication(sys.argv)  # Create the QApplication instance
    window = WordCounterApp()  # Create the GUI instance
    window.show()
    sys.exit(app.exec_())  # Start the event loop

def load_file():
    global file_contents  # Using the global variable
    file_path = input("Enter the path of the file (leave empty for default directory): ")

    if not file_path:  # if no input, default to the current directory
        file_path = os.path.join(os.getcwd(), 'input.txt')

    file_contents = load_file_contents(file_path)  # Call shared function
    if file_contents is not None:
        print(f"File '{file_path}' loaded successfully.")
    else:
        print(f"File not found: {file_path}")

    return file_path 

def analyze_word_count():
    if file_contents is not None:
        # Perform analysis on file_contents here
        print("Analyzing contents...")
        # Analysis logic here
    else:
        print("No file loaded for analysis.")             

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        launch_gui()
    else:
        main_menu()  # Run console version if no argument is passed