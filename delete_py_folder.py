import os
from tkinter import filedialog, Tk

def delete_python_files_in_directory(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                full_file_path = os.path.join(root, file)
                print(f"Deleting file: {full_file_path}")
                os.remove(full_file_path)

def select_directory_for_deletion():
    root = Tk()
    root.withdraw() 
    directory_path = filedialog.askdirectory()
    if directory_path:  
        delete_python_files_in_directory(directory_path)
        print("Deletion complete.")

select_directory_for_deletion()
