# shared_functions.py

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            return contents  # Return the contents instead of printing them
    except FileNotFoundError:
        return f"Error: The file '{filename}' does not exist."
    except Exception as e:
        return f"An error occurred: {e}"

def load_file():
    print("Loading file")  # Implement actual loading logic as needed

def analyze_word_count():
    print("Analyzing file")  # Implement actual analysis logic as needed

