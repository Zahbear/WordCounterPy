# shared_functions.py

import re
from collections import Counter

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

def analyze_word_count(text, limit=20):
    # This matches strings to detect componded words using special symbols (-, ', `, @)
    word_pattern = r'\b\w+(?:[-\'`@]\w+)*\b'

    # Use pattern to find all words in the text
    words = re.findall(word_pattern, text.lower()) # converts to lowercase 

    # Count word occurerences
    word_count = Counter(words)

    # Sort the word count dictionary by frequency, descending, and alphabetically for ties
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: (-item[1], item[0])))

    # Apply limit to result if needed
    limited_word_count = dict(list(sorted_word_count.items())[:limit])

    return limited_word_count

def format_word_count_result(word_count):
    if not word_count:
        return "No words to display."

    # Find the longest word for column width
    max_word_length = max(len(word) for word in word_count.keys()) + 2 # Adding 2 spaces for padding

    # Prepare formatted result as a two-column table
    result = f"{'Word'.ljust(max_word_length)}| Count\n"
    result += "-" * (max_word_length + 8) + "\n" # Adding a separator line

    for word, count in word_count.items():
        result += f"{word.ljust(max_word_length)}| {count}\n"

    return result
