import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# Base URL ng website
base_urls = [
"https://lawphil.net/judjuris/juri2023/jan2023/jan2023.html",
"https://lawphil.net/judjuris/juri2023/feb2023/feb2023.html",
"https://lawphil.net/judjuris/juri2023/mar2023/mar2023.html",
"https://lawphil.net/judjuris/juri2023/apr2023/apr2023.html",
"https://lawphil.net/judjuris/juri2023/may2023/may2023.html",
"https://lawphil.net/judjuris/juri2023/jun2023/jun2023.html",
"https://lawphil.net/judjuris/juri2023/jul2023/jul2023.html",
"https://lawphil.net/judjuris/juri2023/aug2023/aug2023.html",
"https://lawphil.net/judjuris/juri2023/sep2023/sep2023.html",
"https://lawphil.net/judjuris/juri2023/oct2023/oct2023.html",
"https://lawphil.net/judjuris/juri2023/nov2023/nov2023.html",
"https://lawphil.net/judjuris/juri2023/dec2023/dec2023.html"
]
# Directory to save the files
download_dir = "C:/Users/Admin/Downloads/Decisions/2023"

# Function to download files from a page
def download_files(url):
    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 23.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.123 Safari/537.3'}
    response = requests.get(url, headers=headers, timeout=10) # Timeout duration set to 23 seconds
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to get {url}")
        return
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")
    # Find all links on the page
    links = soup.find_all("a")
    # Loop through all links
    for link in links:
        # Get the href attribute of the link
        href = link.get("href")
        # Check if the link is a file
        if href and (href.endswith(".pdf") or href.endswith(".doc") or href.endswith(".html")):
            # Construct the absolute URL of the file
            file_url = urljoin(url, href)
            # Extract the filename
            filename = os.path.join(download_dir, href.split("/")[-1])
            # Download the file
            with open(filename, "wb") as f:
                f.write(requests.get(file_url).content)
                print("Downloaded:", filename)

# Create the download directory if it doesn't exist
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Start downloading all files
for url in base_urls:
    download_files(url)
