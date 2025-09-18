# Task 1: Read a File and Handle Errors

try:
    # Try opening and reading the file
    with open("sample.txt", "r") as file:
        print("File content:\n")
        for line in file:
            print(line.strip())  # strip() removes newline characters
except FileNotFoundError:
    # Handle case when file does not exist
    print("Error: The file 'sample.txt' does not exist. Please check the filename and try again.")
