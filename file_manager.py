import os
import sys
import shutil

def get_folder_contents_sorted_by_size(directory):
    try:
        # List all items in the directory with their sizes
        items = [(item, os.path.getsize(os.path.join(directory, item))) for item in os.listdir(directory)]
        # Sort items by size (smallest to largest)
        sorted_items = sorted(items, key=lambda x: x[1])
        return sorted_items
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return []

def display_items(items):
    print("\nContents sorted by size:")
    for i, (name, size) in enumerate(items, 1):
        print(f"{i}. {name} - {size} bytes")

def handle_deletion(path):
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f"File {path} deleted.")
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Folder {path} deleted.")
        else:
            print(f"{path} does not exist.")
    except Exception as e:
        print(f"Error deleting {path}: {e}")

def explore_folder(folder_path):
    if not os.path.isdir(folder_path):
        print(f"{folder_path} is not a valid folder.")
        return
    
    items = get_folder_contents_sorted_by_size(folder_path)
    display_items(items)
    
    while True:
        choice = input("\nEnter the number of a file to delete it, or 'back' to return: ")
        if choice.lower() == "back":
            break
        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(items):
                file_name = items[file_index][0]
                file_path = os.path.join(folder_path, file_name)
                handle_deletion(file_path)
                items = get_folder_contents_sorted_by_size(folder_path)
                display_items(items)
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number or 'back'.")

def main():
    directory = input("Enter the directory to scan: ").strip()
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)
    
    while True:
        contents = get_folder_contents_sorted_by_size(directory)
        display_items(contents)
        
        choice = input("\nEnter the number of a folder to open it, 'delete' to delete a folder, or 'exit' to quit: ")
        if choice.lower() == "exit":
            print("Exiting program.")
            sys.exit(0)
        elif choice.lower() == "delete":
            folder_index = input("Enter the number of the folder to delete: ")
            try:
                folder_index = int(folder_index) - 1
                if 0 <= folder_index < len(contents):
                    folder_name = contents[folder_index][0]
                    folder_path = os.path.join(directory, folder_name)
                    handle_deletion(folder_path)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            try:
                folder_index = int(choice) - 1
                if 0 <= folder_index < len(contents):
                    folder_name = contents[folder_index][0]
                    folder_path = os.path.join(directory, folder_name)
                    explore_folder(folder_path)
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    main()
