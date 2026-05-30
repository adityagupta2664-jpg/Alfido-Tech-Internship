import os
import shutil

# Create a folder to store files
FOLDER = "Files"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)


# Create File
def create_file():
    try:
        filename = input("Enter file name (without extension): ")
        content = input("Enter file content: ")

        filepath = os.path.join(FOLDER, filename + ".txt")

        with open(filepath, "w") as file:
            file.write(content)

        print("File created successfully!")

    except Exception as e:
        print("Error:", e)


# Read File
def read_file():
    try:
        filename = input("Enter file name: ")
        filepath = os.path.join(FOLDER, filename + ".txt")

        with open(filepath, "r") as file:
            print("\n----- FILE CONTENT -----")
            print(file.read())

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# Rename File
def rename_file():
    try:
        old_name = input("Enter current file name: ")
        new_name = input("Enter new file name: ")

        old_path = os.path.join(FOLDER, old_name + ".txt")
        new_path = os.path.join(FOLDER, new_name + ".txt")

        os.rename(old_path, new_path)

        print("File renamed successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# Move File
def move_file():
    try:
        filename = input("Enter file name: ")

        destination_folder = "MovedFiles"

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        source = os.path.join(FOLDER, filename + ".txt")

        shutil.move(source, destination_folder)

        print("File moved successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# Delete File
def delete_file():
    try:
        filename = input("Enter file name: ")

        filepath = os.path.join(FOLDER, filename + ".txt")

        os.remove(filepath)

        print("File deleted successfully!")

    except FileNotFoundError:
        print("File not found!")

    except Exception as e:
        print("Error:", e)


# List Files
def list_files():
    try:
        files = os.listdir(FOLDER)

        if len(files) == 0:
            print("No files available.")

        else:
            print("\nAvailable Files:")
            for file in files:
                print(file)

    except Exception as e:
        print("Error:", e)


# Main Program
while True:

    print("\n========== FILE MANAGEMENT SYSTEM ==========")
    print("1. Create File")
    print("2. Read File")
    print("3. Rename File")
    print("4. Move File")
    print("5. Delete File")
    print("6. List Files")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        read_file()

    elif choice == "3":
        rename_file()

    elif choice == "4":
        move_file()

    elif choice == "5":
        delete_file()

    elif choice == "6":
        list_files()

    elif choice == "7":
        print("Thank you for using File Management System.")
        break

    else:
        print("Invalid choice! Please try again.")