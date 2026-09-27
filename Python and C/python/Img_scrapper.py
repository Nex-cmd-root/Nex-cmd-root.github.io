import requests
from bs4 import BeautifulSoup

def download_web_image():
    # Target URL of our previous quotes page
    url = "https://toscrape.com/"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to access web page.")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    
    # 1. Look for the logo or any image tag on the page
    # Let's say we want to find the first <img> tag present on the website
    img_tag = soup.find("img")
    
    if img_tag is None:
        print("No images found on this webpage.")
        return

    # 2. Extract the source URL path inside the image tag (the 'src' attribute)
    # This might give us a partial path like "/static/logo.png"
    img_relative_path = img_tag.get("src")

    img_name = img_relative_path.split("/")[-1]
    
    # Construct the full absolute web address link to the physical file
    img_full_url = "https://toscrape.com/" + img_relative_path
    print(f"Located image link: {img_full_url}")

    # 3. Stream the raw binary image data over the network
    # We add stream=True to handle large files efficiently
    img_response = requests.get(img_full_url, stream=True)
    
    if img_response.status_code == 200:
        # 4. Open a local file in 'wb' (Write Binary) mode
        with open(img_name, "wb") as image_file:
            # Write the raw incoming internet chunks straight to your hard drive disk
            for chunk in img_response.iter_content(chunk_size=1024):
                image_file.write(chunk)
                
        print(f"[Success] Image downloaded and saved as '{img_name}'!")
    else:
        print("Could not download the physical image file.")

if __name__ == "__main__":
    download_web_image()