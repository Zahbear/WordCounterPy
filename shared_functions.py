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

def load_file_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()  # Return contents for later analysis
    except FileNotFoundError:
        return None
    except Exception as e:
        return str(e)

def analyze_word_count():
    print("Analyzing file")  # Implement actual analysis logic as needed

