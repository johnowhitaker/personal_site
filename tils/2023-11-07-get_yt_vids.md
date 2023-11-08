---
date: "2023-11-07"
categories: 
  - "TIL"
---

# Getting My YouTube Videos as MarkDown pages for this Quarto blog

Step 1 was getting the video info:

```
 youtube-dl --get-filename -o "%(upload_date)s,%(id)s,%(duration)s,%(title)s,%(description)s" https://www.youtube.com/@datasciencecastnet > yt_vids.txt
```

Then I processed the resulting file with

```python
import os, glob

# Define a function to fix the URLs in the description
def fix_urls(description):
    return description.replace(" -_", "://").replace("_", "/").replace("https -", "https://")

# Read the input file
with open('yt_vids.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Directory to store markdown files
output_dir = 'misc'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(os.path.join(output_dir, 'thumbnails'), exist_ok=True)

# Process each line in the file
for line in lines:
    date, video_id, duration, title, description = line.strip().split(',', 4)

    # Reformat date
    date = date[:4] + '-' + date[4:6] + '-' + date[6:]
    
    # Create a markdown file for each line
    filename = f"{date}-{title.replace('/', '_').replace(' ', '_')}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Fix the URLs in the description
    description = fix_urls(description)
    
    # Video URL
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    # Download the thumbnail
    cmd = f"youtube-dl --write-thumbnail --skip-download {video_url} -o {os.path.join(output_dir, 'thumbnails', video_id)}"
    # os.system(cmd)

    # Get extension of thumbnail
    thumbnail = glob.glob(os.path.join(output_dir, 'thumbnails', video_id + '.*'))[0]
    thumbnail_ext = thumbnail.split('.')[-1]


    # Write the markdown content
    with open(filepath, 'w', encoding='utf-8') as md_file:
        md_file.write('---\n')
        md_file.write(f'title: "{title}"\n')
        md_file.write(f'date: {date}\n')
        md_file.write('categories: \n')
        md_file.write('  - "Video"\n')
        md_file.write(f'image: "thumbnails/{video_id}.{thumbnail_ext}"\n')
        md_file.write('---\n\n')

        md_file.write(f'### {title}\n\n')
        
        # Video link/preview (depending on your markdown processor, you might need a different embedding code)
        md_file.write("{{< video https://www.youtube.com/embed/"+video_id+" >}}\n\n")
        
        # Write the video description
        md_file.write(description + '\n')
```