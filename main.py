import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import unquote, urljoin, urlparse

def spider(url, visited=set(), scope=[], referer=""):

    url_parsed = urlparse(url)

    if not scope:
        new_scope = ('.'.join(url_parsed.netloc.split('.')[-2:]))
        scope.append(new_scope)
        print(f"{new_scope} was added to scope")

    url = unquote(url)

    url = urljoin(referer, url)

    if url in visited or not any([x in url for x in scope]):
        return

    visited.add(url)

    print(f"Spidering URL: {url}")

    with open("links.txt", "a") as f:
        f.write(url + '\n')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        "Referer": referer
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
  
    html = response.content
    soup = BeautifulSoup(html, "html.parser")
  
    for link in soup.find_all("a"):
        link_url = link.get("href")
        if link_url:
            spider(link_url, visited, scope, referer=url)

def main():
    parser = argparse.ArgumentParser(description='Spider a website')
    parser.add_argument('url', help='Full URL to spider (e.g. https://www.youtube.com)')
    parser.add_argument('--scope', help='Scope of the spider', default=[])
    args = parser.parse_args()
    URL = args.url
    SCOPE = args.scope

    with open("links.txt", "w"):
        pass

    spider(URL, visited=set(), scope=SCOPE)


if __name__ == "__main__":
    main()
