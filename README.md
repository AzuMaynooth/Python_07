In this exercise, you're tasked to create a Python script called 'reader.py' that modifies a CSV file based on user-provided changes, displays its content in the terminal, and saves the modified file to a provided destination.

1. The script should be run as `reader.py <src> <dst> <change1> <change2> ...`. 'src' is the path of the CSV file to be modified.
    - If the file does not exist or the path specified is not a file, display an error message and the filenames in the same directory.

2. 'dst' is the target path where the modified CSV file will be saved.

3. 'change1' ... 'changeN' are strings of the form "X,Y,value". 'X' is the column (also counting from 0), 'Y' is the row to modify (counting from 0), and 'value' is the new value for the given cell.

4. After applying all changes, the script should display the content of the modified CSV file in the terminal and save it to the destination path.
