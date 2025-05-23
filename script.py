import os
import re

DATA_DIR = "DATA"  # Change this to your actual data folder if needed

def build_url_map(data_dir):
    url_map = {}
    for folder in os.listdir(data_dir):
        folder_path = os.path.join(data_dir, folder)
        index_path = os.path.join(folder_path, "index.html")
        if os.path.isdir(folder_path) and os.path.isfile(index_path):
            with open(index_path, encoding="utf-8") as f:
                content = f.read()
                m = re.search(r'data-scrapbook-source="([^"]+)"', content)
                if m:
                    url = m.group(1)
                    url_map[url] = f"{folder}/index.html"
    return url_map

def replace_links_in_file(file_path, url_map):
    with open(file_path, encoding="utf-8") as f:
        content = f.read()
    def repl(match):
        href = match.group(1)
        for url, local_path in url_map.items():
            if href.startswith(url):
                # Always use just the folder/index.html, not a relative path
                return f'href="{local_path}"'
        return match.group(0)
    new_content = re.sub(r'href="([^"]+)"', repl, content)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    url_map = build_url_map(DATA_DIR)
    for folder in os.listdir(DATA_DIR):
        folder_path = os.path.join(DATA_DIR, folder)
        index_path = os.path.join(folder_path, "index.html")
        if os.path.isdir(folder_path) and os.path.isfile(index_path):
            replace_links_in_file(index_path, url_map)

if __name__ == "__main__":
    main()