import os
import shutil

def organize_workspace(target_directory):
    print(f"--- Activating File Management System on: {target_directory} ---")
    
    # 1. Verification: Make sure the target folder actually exists
    if not os.path.exists(target_directory):
        print("Error: Target directory does not exist.")
        return

    # 2. Extract a clean list of every file name inside that folder
    # This works exactly like your BeautifulSoup web matching lists!
    all_files = os.listdir(target_directory)
    
    # 3. Establish our folder rule definitions map
    # File Extension Tag : Target Destination Folder Name
    extension_map = {
        ".txt": "TextDocuments",
        ".png": "Images",
        ".pdf": "PDF_Reports",
        ".jpg": "and_JPEG_Images"
    }

    counter = 1
    for filename in all_files:
        # Construct the absolute physical file path location block
        file_path = os.path.join(target_directory, filename)
        
        # Safety Check: Skip directories/folders. We only want to move actual files!
        if os.path.isdir(file_path):
            continue

        # Extract the extension string out of the file name (e.g., "report.pdf" -> ".pdf")
        # 'os.path.splitext' splits a filename into a tuple: ('report', '.pdf')
        file_extension = os.path.splitext(filename)[1].lower()

        # 5. EXECUTE THE MOVE: Check if the extension exists inside our rules map
        if file_extension in extension_map:
            new_name = f"ScrapedAsset_{counter}{file_extension}"

            os.rename(file_path, os.path.join(target_directory, new_name)) # Rename the file to a new name with a counter
            counter += 1
            
    print("\n[Success] Local system file reorganization process complete!")

if __name__ == "__main__":
    # Test it on a folder path (use "." to target the current directory where your script lives)
    organize_workspace("scraped_images")