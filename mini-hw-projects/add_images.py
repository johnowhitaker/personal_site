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

    if not os.path.exists('mini-hw-projects\images'):
        os.makedirs('mini-hw-projects\images')

    for url in image_urls:
        if 'http' in url:
            file_name = os.path.basename(urlparse(url).path)
            save_path = f'mini-hw-projects\images\{file_name}'
            download_image(url, save_path)
            content = content.replace(url, f'images/{file_name}')

    with open(file_path, 'w') as file:
        file.write(content)

# Example usage
import glob

markdown_files = ['mini-hw-projects\\2013-07-04-ir_webcam.md', 'mini-hw-projects\\2013-08-03-easy_3d_scanner.md', 'mini-hw-projects\\2013-09-02-junk_vdg.md',  'mini-hw-projects\\2013-12-01-diy_cellphone_macro_lens.md', 'mini-hw-projects\\2014-01-01-multitouch_surface.md', 'mini-hw-projects\\2023-09-30-text_to_print.md', 'mini-hw-projects\\2023-11-020-work_timer.md', 'mini-hw-projects\\bagpipes.md', 'mini-hw-projects\\cirts.md', 'mini-hw-projects\\dorm.md', 'mini-hw-projects\\kwese.md', 'mini-hw-projects\\micromouse.md', 'mini-hw-projects\\minilaser.md', 'mini-hw-projects\\mini_pcb.md', 'mini-hw-projects\\octo.md', 'mini-hw-projects\\osc.md', 'mini-hw-projects\\printer.md', 'mini-hw-projects\\seitis.md']
for markdown_file in markdown_files:
    print(markdown_file)
    print("###")
    process_markdown(markdown_file)
