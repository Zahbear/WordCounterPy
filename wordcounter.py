# wordcounter.py

import sys
from PyQt5.QtWidgets import QApplication  # Import QApplication here
from word_counter_gui import WordCounterApp  # Import the GUI
from shared_functions import display_file_contents, load_file, analyze_word_count  # Import from shared_functions

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
        load_file()
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


#    file_path = input("Enter the path of the file: ")
#    try:
#        with open(file_path, 'r') as file:
#            print(f"File {file_path} loaded successfully.")
#            # Store contents for analysis later
#    except FileNotFoundError:
#        print(f"File not found: {file_path}")

#def read_file(file_path):
#    try:
#        with open(file_path, 'r') as file:
#            content = file.read()
#            return content
#    except Exception as e:
#        print(f"Error reading file: {e}")
#        return None

#def count_words(content):
#    words = content.split()
#    word_count = {}
#    for word in words:
#        word = word.lower().strip(",.!?\"'")  # Normalize and strip punctuation
#        word_count[word] = word_count.get(word, 0) + 1
#    return word_count

#def display_word_count(word_count):
#    for word, count in word_count.items():
#        print(f"{word}: {count}")



if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        launch_gui()
    else:
        main_menu()  # Run console version if no argument is passed