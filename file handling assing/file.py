import os

def main():
    while True:
        file_name = input("Enter the file name: ").strip()
        
        if os.path.exists(file_name):
            print(f"Error: The file '{file_name}' already exists.")
            choice = input("Do you want to overwrite the file? (yes/no): ").strip().lower()
            
            if choice == 'yes':
                print(f"Overwriting the file '{file_name}'.")
                break
            else:
                new_file_name = input("Enter the new file name: ").strip()
                
                if new_file_name == file_name:
                    print("Error: You entered the same file name. Please enter a different name.")
