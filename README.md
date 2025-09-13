# Assignment4
Task 1:

Simple File Reader
A basic Python script for reading and displaying the contents of a text file, demonstrating fundamental file I/O and error handling.

Usage
To run this script, simply execute file.py with Python 3. Make sure the sample.txt file is in the same directory.
Bash
python file.py

Features
Reads Text Files: Opens and reads a specified text file line by line.
Line-by-Line Output: Prints each line with a corresponding line number for easy readability.
Robust Error Handling: Includes a try...except block to prevent crashes if the target file is not found.

Contents
file.py: The Python script.
sample.txt: A sample text file for the script to read.


Task 2:

Place the write_append.py script in a folder.
Open your terminal or command prompt in that folder.
Run the script using Python 3:
  Bash
  python write_append.py
The script will guide you with on-screen prompts.
First, it will ask you to enter some text. 
This will overwrite any previous content in Output.txt. 
Then, it will prompt you for more text to add to the end of the file. 
Finally, it will print everything inside the file for you to see the results.

What the Code Does
The first part of the script uses the 'w' (write) mode to open Output.txt. 
This mode overwrites the file's content, replacing everything inside it with the new text you enter.
The second part uses the 'a' (append) mode. 
This is different because it adds new text to the end of the file without deleting the existing content.
\Finally, the script opens the file in 'r' (read) mode to display the combined content of both operations.
This simple script is a hands-on way to understand these common file modes and how they change a file's content.

