# Built by Meeran Hassan
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin, urlparse

def spider(url, visited=set(), scope=[], referer=""):

    # URL will be broken down into its components
    url_parsed = urlparse(url)

    # If scope is empty, add the domain to the scope
    if not scope:
        new_scope = ('.'.join(url_parsed.netloc.split('.')[-2:]))
        scope.append(new_scope)
        print(f"{new_scope} was added to scope")

    # Decode the URL
    url = unquote(url)

    # Making sure any relative URLs are converted to absolute URLs
    url = urljoin(referer, url)

    # Skip the URL if it has already been visited or is not in the scope
    if url in visited or not any([x in url for x in scope]):
        return

    # Mark the URL as visited
    visited.add(url)

    # Log the URL to the terminal before writing
    print(f"Spidering URL: {url}")

    # Write the links to the file
    with open("links.txt", "a") as f:
        f.write(url + '\n')

    # Set a legit user-agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": referer
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()
  
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
  
    # Recursively spider the webpage for links
    for link in soup.find_all("a"):
        link_url = link.get("href")
        if link_url:
            spider(link_url, visited, scope, referer=url)

def main():
    # Parse the arguments supplied
    parser = argparse.ArgumentParser(description='Spider a website')
    parser.add_argument('url', help='Full URL to spider (e.g. https://www.youtube.com)')
    parser.add_argument('--scope', help='Scope of the spider', default=[])
    args = parser.parse_args()
    URL = args.url
    SCOPE = args.scope

    # Create/empty a file to store the links
    with open("links.txt", "w"):
        pass

    # Start the spider
    spider(URL, visited=set(), scope=SCOPE)


if __name__ == "__main__":
    main()
