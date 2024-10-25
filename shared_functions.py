# shared_functions.py

import re
import os
from collections import Counter
import sys
from PyQt5.QtWidgets import QApplication

word_count_result = {}
result_limit = 20
file_contents = None

def analyze_word_count_submenu(file_contents, word_count_result, result_limit, current_format):
    global word_count_result, result_limit, current_format, file_contents

    # Check if a file is selected
    if file_contents is None:
        print("No file selected! Select a file now? (y - select file ; else - default input.txt)")
        choice = input().strip().lower()

        if choice == "y":
            file_contents = load_file_contents(input("Enter file path: "))
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
                return file_contents, word_count # Return the state

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
            display_file_contents(file_contents)
        elif choice == "2":
            print_word_count_results(word_count, result_limit, current_format) # Call the function to print results based on current format
        elif choice == "3":
            format_word_count_results()  # Call the format submenu
        elif choice == "4":
            result_limit = set_result_limit()
            word_count = analyze_word_count(file_contents, result_limit)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")
    return file_contents, word_count


def print_word_count_results(word_count, result_limit, format_type):
    # Prints word count results based on the current format.
    if format_type == 'raw':
        for word, count in word_count.items():
            print(f"{word}: {count}")
    elif format_type == 'table':
        formatted_result = format_word_count_result(word_count)
        print(formatted_result)

def format_word_count_results():
    # Provides format submenu to choose display format.
    while True:
        print("\nChoose result format:")
        print("1. Raw (word: count)")
        print("2. Table")
        print("0. Back")
        choice = input("Select a format: ")
        
        if choice == "1":
            return "raw"
        elif choice == "2":
            return "table"
        elif choice == "0":
            return None
        else:
            print("Invalid choice, try again.")

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents  # Return the contents instead of printing them
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def load_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()  # Return contents for later analysis
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)

def analyze_word_count(text, sort_by='frequency', limit=20):
    # Analyze word counts in a given text with optional sorting and limit parameters.
    
    # Args:
    #    text (str): The input text to analyze.
    #    sort_by (str): The sorting criteria, either 'frequency' or 'alphabetical'.
    #    limit (int): Maximum number of results to return.

    #Returns:
    #    dict: A dictionary of word counts, limited and sorted by the specified criteria.
    #
    # Match words with potential compound symbols (hyphens, apostrophes, etc.)
    word_pattern = r'\b\w+(?:[-\'`@]\w+)*\b'
    words = re.findall(word_pattern, text.lower())
    word_count = Counter(words)

    # Sort based on the specified criteria
    if sort_by == 'alphabetical':
        sorted_word_count = dict(sorted(word_count.items()))
    else:
        sorted_word_count = dict(sorted(word_count.items(), key=lambda item: (-item[1], item[0])))

    # Apply the result limit
    limited_word_count = dict(list(sorted_word_count.items())[:limit])
    return limited_word_count

def format_word_count_result(word_count):
    #Format the word count results for display.
    
    #Args:
    #    word_count (dict): A dictionary of word counts.

    #Returns:
    #   str: A formatted string representing the word count results.
    if not word_count:
        return "No words to display."

    max_word_length = max(len(word) for word in word_count.keys()) + 2
    result = f"{'Word'.ljust(max_word_length)}| Count\n"
    result += "-" * (max_word_length + 8) + "\n"

    for word, count in word_count.items():
        result += f"{word.ljust(max_word_length)}| {count}\n"

    return result

def set_result_limit():
    # Sets result limit for word count display.
    try:
        new_limit = input("Enter a new limit (e.g., 5, 7, 100): ")
        if not new_limit.strip():
            raise ValueError
        new_limit = int(new_limit)
        if new_limit < 1:
            raise ValueError
        return new_limit
    except ValueError:
        print("Invalid limit; setting limit to default of 20.")
        return 20

def exit_application(app_type="CLI"):
    #Exit the application, determining behavior based on app type (CLI or GUI).
    
    #Args:
    #    app_type (str): 'CLI' or 'GUI' to specify the application type.
    
    if app_type == "GUI":
        QApplication.quit()
    else:
        sys.exit()