import os
import shutil

class FileManipulator:
    @staticmethod
    def read(f_name):
        try:
            with open(f"{f_name}.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("File not found.")

    @staticmethod
    def write(f_name, value):
        try:
            with open(f"{f_name}.txt", "a") as file:
                file.write(value + "\n")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def newFolder(folder_name):
        try:
            os.mkdir(folder_name)
        except FileExistsError:
            print("Folder already exists.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def remove(remove):
        try:
            os.remove(f"{remove}.txt")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def exist(exist):
        try:
            with open(f"{exist}.txt", "r") as file:
                print("File exists.")
        except FileNotFoundError:
            print("File does not exist.")

    @staticmethod
    def copy(source, destination):
        try:
            shutil.copy(f"{source}.txt", f"{destination}.txt")
            print(f"Copied {source}.txt to {destination}.txt")
        except FileNotFoundError:
            print("Source file not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

while True:
    try:
        option = int(input("options:\n\t1) read\n\t2) write\n\t3) new_folder\n\t4) remove\n\t5) exist or not\n\t6) copy\n\t7) exit\n"))

        if option == 1:
            f_name = input("Enter the file name: ")
            FileManipulator.read(f_name)

        elif option == 2:
            f_name = input("Enter the file name: ")
            value = input("Enter the text: ")
            FileManipulator.write(f_name, value)

        elif option == 3:
            folder_name = input("Enter the folder name: ")
            FileManipulator.newFolder(folder_name)

        elif option == 4:
            remove = input("Enter the file name which you want to remove: ")
            FileManipulator.remove(remove)

        elif option == 5:
            exist = input("Enter the file name: ")
            FileManipulator.exist(exist)

        elif option == 6:
            source = input("Enter the source file name: ")
            destination = input("Enter the destination file name: ")
            FileManipulator.copy(source, destination)

        elif option == 7:
            print("Goodbye!")
            break
    except ValueError:
        print("Invalid option")
