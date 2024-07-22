import sys
import csv
import os

# If file not found diplay error sms
def display_directory_contents(directory):
    print(f"Error: File not found. Files in the directory '{directory}':")
    for filename in os.listdir(directory):
        print(filename)

# Read file
def read_csv(file_path):
    with open(file_path, 'r', newline='') as file:
        reader = csv.reader(file)
        return list(reader)

# Add fields to be modify
def apply_changes(data, changes):
    for change in changes:
        try:
            x, y, value = change.split(',')
            x = int(x)
            y = int(y)
            data[y][x] = value
        except (ValueError, IndexError):
            print(f"Invalid change format or index out of range: {change}")

# Save changes in out.csv if file does not existe creat it
def save_csv(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def print_content(data):
    for row in data:
        print(",".join(row))

def main():

    if len(sys.argv) < 4:
        print("Usage: editingCSV.py <src> <dst> <change1> <change2> ...")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    if not os.path.isfile(src):
        display_directory_contents(os.path.dirname(src) or '.')
        sys.exit(1)

    data = read_csv(src)
    print("\nOriginal content of the CSV file:")
    print_content(data)

    apply_changes(data, changes)

    print("\nModified content of the CSV file:")
    print_content(data)

    save_csv(dst, data)
    #print(f"\nModified CSV file saved to '{dst}'.")

if __name__ == "__main__":
    main()
