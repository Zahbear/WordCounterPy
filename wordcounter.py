# wordcounter.py

import sys
import os
from word_counter_gui import WordCounterApp  # Import the GUI
from shared_functions import (
    display_file_contents, 
    load_file_contents, analyze_word_count, 
    analyze_word_count_submenu, 
    format_word_count_result, print_word_count_results,
    format_word_count_results, set_result_limit, exit_application
) # Import from shared_functions

file_contents = None
word_count_result = {} # Store word count result
result_limit = 20 # Default result limit
current_format = "table" # Default format

os.system('clear')
print("Word Counter Py v1.3.2 (terminal)")

def print_divider():
    print ("-" * 40)

def main_menu():
    while True:
        print_divider()
        print("\nMain Menu:")
        print("1. About")
        print("2. Load File")
        print("3. Analyze Word Count")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print_divider()
            display_about()
        elif choice == "2":
            print_divider()
            load_file()
        elif choice == "3":
            print_divider()
            analyze_word_count_cli()
        elif choice == "0":
            print_divider()
            exit_application()
        else:
            print("Invalid choice. Please try again.")

def display_about():
    contents = display_file_contents('.version.txt') # Display About + version
    print(contents)

def launch_gui():
    app = QApplication(sys.argv)  # Create the QApplication instance
    window = WordCounterApp()  # Create the GUI instance
    window.show()
    sys.exit(app.exec_())  # Start the event loop

def load_file():
    global file_contents
    file_path = input("Enter the file path:")
    file_contents = load_file_contents(filename)
    if file_contents:
        print(f"File `{filename}` loaded successfully. Ready for analysis.")
    else:
        pritn("Could not load file contents")

def analyze_word_count_cli():
    global file_contents, word_count_result, result_limit, current_format
    if file_contents is None:
        print("No file is loaded. Using default 'input.txt' file.")
        file_contents = load_file_contents('input.txt')
    if file_contents:
        word_count = analyze_word_count(file_contents)
        file_contents, word_count_result = analyze_word_count_submenu(file_contents, word_count_result, result_limit, current_format)
    else:
        print("No file loaded for analysis.")

def format_word_count_results():
    global word_count_result, current_format

    if not word_count_result:
        print("No word count result to format.")
        return

    while True:
        print("\nFormat Word Count Results Submenu:")
        print("1. Alphabetical")
        print("2. Reverse Alphabetical")
        print("3. Most Occurrences")
        print("4. Least Occurrences")
        print("0. Return to Analyze submenu")
        choice = input("Choose a format: ")

        if choice == "1":
            current_format = "a-z"
            print_divider() 
            print("Results will be sorted alphabetically.")
            return
        elif choice == "2":
            current_format = "z-a"
            print_divider()
            print("Results will be sorted in reverse alphabetical order.")
            return
        elif choice == "3":
            current_format = "most"
            print_divider()
            print("Results will be sorted by most occurrences.")
            return
        elif choice == "4":
            current_format = "least"
            print_divider()
            print("Results will be sorted by least occurrences.")
            return
        elif choice == "0":
            return

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        launch_gui()
    else:
        main_menu()  # Run console version if no argument is passed