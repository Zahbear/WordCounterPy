# wordcounter.py

import sys
import os
from PyQt5.QtWidgets import QApplication  # Import QApplication here
from word_counter_gui import WordCounterApp  # Import the GUI
from shared_functions import display_file_contents, load_file_contents, analyze_word_count, format_word_count_result  # Import from shared_functions

file_contents = None
word_count_result = None # Store word count result
result_limit = 20

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
        analyze_word_count_submenu()
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
    if file_contents:
        print(f"File '{file_path}' loaded successfully.")
    else:
        print(f"File not found: {file_path}")

def analyze_word_count_submenu():
    global word_count_result, result_limit

    if file_contents is None:
        load_file()

    if file_contents is None:
        print("No file loaded for analysis.")
        return

    while True:
        print("\nAnalyze File Submenu:")
        print("1. Print file contents")
        print("2. Print word count result")
        print("3. Format results")
        print("4. Set result limit (current: {})".format(result_limit))
        print("5. Return to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\nFile Contents:")
            print(file_contents)
        elif choice == "2":
            word_count_result = analyze_word_count(file_contents, result_limit)
            formatted_result = format_word_count_result(word_count_result)  # Here we format the result
            print("\nWord Count Result (Top {}):".format(result_limit))
            print(formatted_result)  # Display formatted result as table hopefully
        elif choice == "3":
            if word_count_result:
                formatted_result = format_word_count_result(word_count_result)
                print("\nFormatted Word Count Result:")
                print(formatted_result)
            else:
                print("No word count result to format.")
        elif choice == "4":
            result_limit = int(input("Enter the new result limit (e.g., 5, 10, 20): "))
            print(f"Result limit set to {result_limit}.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        launch_gui()
    else:
        main_menu()  # Run console version if no argument is passed