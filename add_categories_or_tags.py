import os
import re

def add_blogs_tag(markdown_file):
    with open(markdown_file, 'r+', encoding='utf-8') as file:
        content = file.read()
        frontmatter_end = content.find('---', 3)
        frontmatter = content[:frontmatter_end+3]

        # Check if 'categories' field is present and if 'blogs' is one of them
        categories_pattern = re.compile(r'categories:\s*\n((?:\s+- "[^"]+"\n)*)')
        match = categories_pattern.search(frontmatter)
        
        if match:
            categories = match.group(1)
            if '- "blogs"' not in categories:
                # 'blogs' category not found, adding it
                updated_categories = categories + '  - "blogs"\n'
                updated_frontmatter = frontmatter.replace(categories, updated_categories)
                content = updated_frontmatter + content[frontmatter_end+3:]
        else:
            # No categories field present, adding it with 'blogs'
            categories_block = '\ncategories:\n  - "blogs"\n'
            insertion_point = frontmatter_end - 1
            content = content[:insertion_point] + categories_block + content[insertion_point:]

        # Write the updated content back to the file
        file.seek(0)
        file.write(content)
        file.truncate()

def process_markdown_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            add_blogs_tag(os.path.join(directory, filename))

# Replace 'your_directory_path' with the path to your directory containing markdown files.
process_markdown_files('dsc')
