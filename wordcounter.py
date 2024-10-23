# wordcounter.py

import sys
import os
from PyQt5.QtWidgets import QApplication  # Import QApplication here
from word_counter_gui import WordCounterApp  # Import the GUI
from shared_functions import display_file_contents, load_file_contents, analyze_word_count, format_word_count_result  # Import from shared_functions

file_contents = None
word_count_result = None # Store word count result
result_limit = 20 # Default result limit
current_format = "most" # Default format

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
        handle_menu_choice(choice)

def handle_menu_choice(choice):
    if choice == "1":
        print_divider()
        display_about()
    elif choice == "2":
        print_divider()
        load_file()
    elif choice == "3":
        print_divider()
        analyze_word_count_submenu()
    elif choice == "0":
        print_divider()
        exit_application()
    else:
        print("Invalid choice. Please try again.")

def display_about():
    print(display_file_contents('.version.txt')) # Display About + version

def exit_application():
    print("Exiting application")
    exit()

def launch_gui():
    app = QApplication(sys.argv)  # Create the QApplication instance
    window = WordCounterApp()  # Create the GUI instance
    window.show()
    sys.exit(app.exec_())  # Start the event loop

def load_file():
    global file_contents, word_count_result
    file_path = input("Enter the path of the file (leave empty for default directory): ")

    if not file_path:  # if no input, default to the current directory
        file_path = os.path.join(os.getcwd(), 'input.txt')
    
    file_contents = load_file_contents(file_path)  # Call shared function

    if file_contents:
        word_count_result = analyze_word_count(file_contents, result_limit)  # Save result here
        print(f"File '{file_path}' loaded successfully. Word count analyzed.")
    else:
        print(f"File not found: {file_path}")
        file_contents = None  # Ensure file_contents is set to None if loading fails


def analyze_word_count_submenu():
    global word_count_result, result_limit, current_format, file_contents

    # Check if a file is selected
    if file_contents is None:
        print("No file selected! Select a file now? (y - select file ; else - default input.txt)")
        choice = input().strip().lower()

        if choice == "y":
            load_file()
        else:
            file_path = os.path.join(os.getcwd(), 'input.txt')
            file_contents = load_file_contents(file_path)
            if file_contents:
                print(f"Default file '{file_path}' selected")
                word_count_result = analyze_word_count(file_contents, result_limit)  # Analyze when default selected
            else:
                print(f"File not found: {file_path}")  # This case is already handled
                file_contents = None  # Ensure it is set to None
                return


    if file_contents is None:
        print("No file loaded for analysis. Please analyze the file.")
        return

    while True:
        print_divider()
        print("\nAnalyze File Submenu:")
        print(f"1. Print file contents")
        print(f"2. Print Results (Top {result_limit}, {current_format})")  # Changed from "Print raw word count result"
        print("3. Format results")
        print(f"4. Set result limit")
        print("0. Return to main menu")
        choice = input("Choose an option: ")

        if choice == "1":
            print_divider()
            print("\nFile Contents:")
            print(file_contents)
        elif choice == "2":
            print_divider()

#            word_count_result = analyze_word_count(file_contents, result_limit)
#            print(f"\nWord Count Result (Top {result_limit}):")
#            for word, count in word_count_result.items():
#                print(f"{word}: {count}")  # Display the word count without formatting

            print_word_count_results() # Call the function to print results based on current format

        elif choice == "3":
            print_divider()
            format_word_count_results()  # Call the format submenu
        elif choice == "4":
            print_divider()
            try:
                new_limit = input("Enter a new limit (e.g., 5, 7, 100): ")
                if not new_limit.strip():
                    raise ValueError
                new_limit = int(new_limit)
                if new_limit < 1:
                    raise ValueError

                result_limit = new_limit
                print(f"Result limit set to {result_limit}.")
            except ValueError:
                print("No valid limit selected; Setting limit to default.")
                result_limit = 20
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def print_word_count_results():
    global word_count_result, result_limit, current_format

    if not word_count_result:
        print("No word count result to display.")
        return

    # Sort based on current format
    if current_format == "a-z":
        sorted_result = sorted(word_count_result.items(), key=lambda x: x[0])  # Alphabetical order
        print("\nWord Count (Alphabetical Order):")
    elif current_format == "z-a":
        sorted_result = sorted(word_count_result.items(), key=lambda x: x[0], reverse=True)  # Reverse alphabetical
        print("\nWord Count (Reverse Alphabetical Order):")
    elif current_format == "most":
        sorted_result = sorted(word_count_result.items(), key=lambda x: x[1], reverse=True)  # Most occurrences
        print("\nWord Count (Most Occurrences):")
    elif current_format == "least":
        sorted_result = sorted(word_count_result.items(), key=lambda x: x[1])  # Least occurrences
        print("\nWord Count (Least Occurrences):")
    else:  # current_format == "raw"
        sorted_result = word_count_result.items()
        print("\nRaw Word Count Result:")

    # Print the sorted result limited to the result_limit
    for word, count in list(sorted_result)[:result_limit]:  # Limit to result_limit
        print(f"{word}: {count}")



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
            print("\nResults will be sorted alphabetically.")
        elif choice == "2":
            current_format = "z-a"
            print("\nResults will be sorted in reverse alphabetical order.")
        elif choice == "3":
            current_format = "most"
            print("\nResults will be sorted by most occurrences.")
        elif choice == "4":
            current_format = "least"
            print("\nResults will be sorted by least occurrences.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--gui':
        launch_gui()
    else:
        main_menu()  # Run console version if no argument is passed