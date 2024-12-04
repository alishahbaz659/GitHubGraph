import os
import random
from datetime import datetime

def create_random_file():
    # Define the folder name
    folder_name = "random_files"
    
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Created folder: {folder_name}")
    
    # Generate random content
    random_content = f"Random Content: {random.randint(1, 10000)}"
    file_name = f"{folder_name}/random_file_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    
    # Write content to a file inside the folder
    with open(file_name, "w") as file:
        file.write(random_content)
    
    print(f"Created file: {file_name}")

if __name__ == "__main__":
    create_random_file()
