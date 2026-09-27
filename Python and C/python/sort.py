import os

# function to sort files
def sortfile():
    # get all files in the current directory
    files = os.listdir()
    # sort files alphabetically
    files.sort()
    # get the current directory path
    current_dir = os.getcwd()
    # loop through all sorted files
    for file in files:
        # check if the file is a regular file (not a directory)
        if os.path.isfile(file):
            # get the full file path
            file_path = os.path.join(current_dir, file)
            # move the file to the sorted directory
            os.rename(file_path, os.path.join(current_dir, file))
