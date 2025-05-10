import os
import shutil
from pathlib import Path
from docx import Document
import fitz

def get_file(file_path: str) -> str:
    home = Path.home()
    absolute_file_path = (home/file_path).expanduser().resolve()
    if not absolute_file_path.exists():
        return f"File not found: {absolute_file_path}"
    try:
        file = open(absolute_file_path, 'rb')
        return file
    except Exception as e:
        return f"Error reading file: {str(e)}"



def search_file(file_name: str, extension: str, search_dir: str) -> str:
    for root, dirs, files in os.walk(search_dir):  
        for file in files:
            if file == f"{file_name}{extension}":
                return os.path.join(root, file)
    return f"File '{file_name}{extension}' not found in '{search_dir}'"


def copy_file(source_path: str, destination_path: str):
    home = Path.home()
    absolute_source_path = (home/source_path).expanduser().resolve()
    absolute_destination_path = (home/destination_path).expanduser().resolve()
    try:
        if not absolute_source_path.exists():
            return f"Source file not found: {absolute_source_path}"
        
        absolute_destination_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(absolute_source_path, absolute_destination_path)
        return f"File copied successfully from {absolute_source_path} to {absolute_destination_path}"
    except Exception as e:
        return f"Error copying file: {str(e)}"

def delete_file(file_path: str):
    home = Path.home()  
    absolute_file_path = (home/file_path).expanduser().resolve()
    try:
        if not absolute_file_path.exists():
            return f"File not found: {absolute_file_path}"
        os.remove(absolute_file_path)
        return f"File deleted successfully: {absolute_file_path}"
    except Exception as e:
        return f"Error deleting file: {str(e)}"

if __name__ == "__main__":
    print(get_file("desktop\\hmm\\Servers\\functions\\test.docx"))
    #print(copy_file("desktop\\hmm\\Servers\\functions\\demo.txt", "desktop\\demo2.txt"))
    #print(read_file("desktop\\demo2.txt"))
    #print(delete_file("desktop\\demo2.txt"))

    
