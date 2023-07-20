import shutil
import os

def main():
    source_dir = input('Enter the source directory path: ')
    destination_dir = input('Enter the destination directory path: ')
    if not os.path.exists(source_dir):
        print("sdirectory dne.")
        return

    # makedir
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    files_to_copy = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    for filename in files_to_copy:
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)
        shutil.copy(source_path, destination_path)

    print("This Works")

if __name__ == "__main__":
    main()

