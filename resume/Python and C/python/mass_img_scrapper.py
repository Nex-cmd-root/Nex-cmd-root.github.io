import os
import requests
from bs4 import BeautifulSoup

def batch_download_images():
    # Target our primary sandbox hub site
    url = "https://books.toscrape.com/"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to access web page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # 1. EXTRACT ALL: Grab a list of every image present on the layout sheet
    all_images = soup.find_all("img")
    print(f"Discovered {len(all_images)} total image assets on the webpage.\n")

    # 2. FILE MANAGEMENT: Automatically build a target folder if it doesn't exist
    folder_name = "scraped_images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 3. THE BATCH LOOP: Process each asset link one by one
    for i, img_tag in enumerate(all_images, start=1):
        img_relative_path = img_tag.get("src")
        
        if not img_relative_path:
            continue # Skip any image tag missing a source attribute path

        # Cleanly isolate the file name string
        img_name = img_relative_path.split("/")[-1]
        
        # Ensure our absolute link reconstruction stays perfectly clean
        # If path starts with a slash, strip it so we don't form double slashes
        if img_relative_path.startswith("/"):
            img_relative_path = img_relative_path.lstrip("/")
            
        img_full_url = "https://books.toscrape.com/" + img_relative_path
        print(f"[{i}/{len(all_images)}] Downloading: {img_full_url}")

        # Stream the binary packet
        try:
            img_response = requests.get(img_full_url, stream=True, timeout=10)
            if img_response.status_code == 200:
                # ROUTING: Join the folder name and file name together safely
                file_path = os.path.join(folder_name, img_name)
                
                with open(file_path, "wb") as image_file:
                    for chunk in img_response.iter_content(chunk_size=1024):
                        image_file.write(chunk)
            else:
                print(f"   -> Skipped: Server responded with code {img_response.status_code}")
        except Exception as e:
            print(f"   -> Connection Error pulling asset: {e}")
            
    print(f"\n[Success] Batch harvest complete! Check your '{folder_name}' directory.")

if __name__ == "__main__":
    batch_download_images()