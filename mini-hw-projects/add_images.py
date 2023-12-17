import re
import os
import requests
from urllib.parse import urlparse

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download {url}")

def process_markdown(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    image_urls = re.findall(r'!\[\]\((.*?)\)', content)

    if not os.path.exists('dsc\images'):
        os.makedirs('dsc\images')

    for url in image_urls:
        if 'http' in url:
            file_name = os.path.basename(urlparse(url).path)
            save_path = f'dsc\images\{file_name}'
            download_image(url, save_path)
            content = content.replace(url, f'images/{file_name}')

    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
import glob
markdown_files = glob.glob('dsc/*.md')
for markdown_file in markdown_files:
    print(markdown_file)
    print("###")
    try:
        process_markdown(markdown_file)
    except Exception as e:
        print(e)
