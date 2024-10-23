# WordCounterPy
```bash
__        __            _    ____                  _                       
\ \      / /__  _ __ __| |  / ___|___  _   _ _ __ | |_ ___ _ __            
 \ \ /\ / / _ \| '__/ _` | | |   / _ \| | | | '_ \| __/ _ \ '__|           
  \ V  V / (_) | | | (_| | | |__| (_) | |_| | | | | ||  __/ |              
   \_/\_/ \___/|_|  \__,_|  \____\___/ \__,_|_|_|_|\__\___|_|          __  
__      _(_) |_| |__               _| || |_   / (_)_ __      _ __  _   \ \ 
\ \ /\ / / | __| '_ \             |_  ..  _| | || | '_ \    | '_ \| | | | |
 \ V  V /| | |_| | | |            |_      _| | || | | | |  _| |_) | |_| | |
  \_/\_/_|_|\__|_| |_|              |_||_|   | ||_|_| |_| (_) .__/ \__, | |
       / ___| | | |_ _|  _ __ ___   ___ _ __  \_\ _         |_|    |___/_/ 
      | |  _| | | || |  | '_ ` _ \ / _ \ '_ \| | | |                       
      | |_| | |_| || |  | | | | | |  __/ | | | |_| |                       
       \____|\___/|___| |_| |_| |_|\___|_| |_|\__,_|                       

  ```

## Table of Contents
- [Intro](#introduction)
- [Installation and Setup](#installation-and-setup)
- [Dependencies](#dependencies)
- [Future Improvements](#future-improvements)
- [Notes](#notes)

## Intro

WordCounterPy is the python port of my Java version of Word-Counter. Features a user menu, presentation, file selection, file analysis and result viewing and sorting. As of v1.1.3+ features separate GUI.

## Installation and Setup

Steps to run WordCounterPy (Linux Mint)

1. **Install Python:**
   Make sure you have Python installed. If not, download it from [Python's official website](https://www.python.org/downloads/).

2. **Install Dependencies:**
   Use `pip` to install all required libraries. Open a terminal or command prompt and run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Application:**

How to use:
   No UI - To launch the application, navigate to the project directory, where wordcounter.py is, and run 
   ```bash
    python3 wordcounter.py
   ```
   With UI - To launch the application, navigate to the project directory, where wordcounter.py is, and run 
   ```bash
    python3 wordcounter.py --gui
   ```

## Dependencies
The following Python libraries are required to run this project:

Core Libraries:

- `PyQt5`: For GUI development

## Implementations
1. **File selection:**
    - Allows user to select a file, navigating to a file, and select it for analysis. (Hint:
        This is when it gets the Results)

2. **File analysis:**
    - Will manipulate selected file, printing contents, mapping occurrances of individual 
        words, along with printing the results. Also has a provisional sorting feature.

## Future Improvements
The following features are planned for future releases:


1. **Result sorting: WIP**
    - Allows user sort the results in different orders or filters. 
    - Will add more sorting methods (e.g. without words shorter/longer than x chars)
    - Considering adding a search feature

2. **Constant matching**
    - Continously implementing CLI code to be used in GUI

## Notes
- For non-GUI run : File path starts in the same dir as `wordcounter.py`
