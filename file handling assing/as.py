import os

def main():
    file_name = input("Enter the file name: ").strip()
    
    if os.path.exists(file_name):
        print(f"Error: The file '{file_name}' already exists.")
        choice = input("Do you want to overwrite the file? (yes/no): ").strip().lower()
        
        if choice == 'yes':
            print(f"Overwriting the file '{file_name}'.")
        else:
            new_file_name = input("Enter a new file name: ").strip()
            file_name = new_file_name
    
    # Create or overwrite the file
    with open(file_name, 'w') as file:
        file.write("This is a sample content.")
    
    print(f"File '{file_name}' has been created/overwritten.")

if __name__ == "__main__":
    main()
