# WordCounterPy
Python version of Word-Counter (menu version)

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
   To launch the application, navigate to the project directory, where wordcounter.py is, and run 
   ```bash
    python3 wordcounter.py
   ```

## Dependencies
The following Python libraries are required to run this project:

Core Libraries:

- `PyQt5`: For GUI development

## Future Improvements
The following features are planned for future releases:

1. **File selection:**
    - Allows user to select a file, eventually by navigating to a file, and select it for analysis

2. **File alaysis:**
    - Will analyze selected file, mapping occurrances of individual words, along with a way to present the results

3. **Result sorting:**
    - Allows user sort the results in different orders or filters


## Notes
(for later):
To set a file path, you will need to type in/paste the path to your file
ex. ~/WordCounterPy/file.type
