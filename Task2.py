# Task 2: Write and Append Data to a File

# Step 1: Write user input to output.txt
user_input = input("Enter some text to write into the file: ")

with open("output.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
extra_input = input("Enter some text to append to the file: ")

with open("output.txt", "a") as file:
    file.write(extra_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of 'output.txt':\n")
with open("output.txt", "r") as file:
    print(file.read())
