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

def analyze_word_count(text):
    # This matches strings to detect componded words using special symbols (-, ', `, @)
    word_pattern = r'\b\w+(?:[-\'`@]\w+)*\b'

    # Use pattern to find all words in the text
    words = re.findall(word_pattern, text.lower()) # converts to lowercase 

    # Count word occurerences
    word_count = Counter(words)

    # Sort the word count dictionary by frequency, descending, and alphabetically for ties
    sorted_word_count = dict(sorted(word_count.items(), key=lambda item: (-item[1], item[0])))

    return sorted_word_count

def OLDnalyze_word_count(contents):
    if contents is None:
        return "No contents to analyze."

    # Regex again to split by word boundaries, ignoring punctuation
    words = re.findall(r'\b\w+\b', contents.lower())  # Finds all alphanumeric strings, ignoring symbols
    word_count = len(words)
    word_occurrences = {}

    # Count occurrences of each word
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    # Format result and output
    result = f"Total words: {word_count}, Unique words: {len(word_occurrences)}\n\nWord Occurrences:\n"
    for word, count in word_occurrences.items():
        result += f"{word}: {count}\n"

    return result