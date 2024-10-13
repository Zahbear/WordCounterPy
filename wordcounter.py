# wordcounter.py

def display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


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
    display_file_contents('.version.txt') # Display Presentation + version

def load_file():
    print("Loading file")

def analyze_word_count():
    print("Analyzing file")

def exit_application():
    print("Exiting application")
    exit()


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
    main_menu()  # Changed file to the Presentation +version