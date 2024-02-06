import argparse
from fastbook import *
import os

def get_images(query: str, max_images: int = 10):
    current_directory = os.path.abspath(os.getcwd())
    save_path = os.path.join(current_directory, f"images/{query}/")
    urls = search_images_ddg(query, max_images=max_images)
    for i, url in enumerate(urls):
        try:
            download_url(url, os.path.join(save_path, f"{query}_{i}.jpg"))
        except Exception as e:
            print(f'Not able to download {url}: {e}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download images based on a query.")
    parser.add_argument("--query", type=str, default="burger", help="The search query for images (default: 'burger').")
    parser.add_argument("--max_images", type=int, default=10, help="Maximum number of images to download (default: 10).")
    args = parser.parse_args()

    get_images(args.query, args.max_images)
