import requests
from bs4 import BeautifulSoup

def simple_crawl(url, max_pages=5):
    visited = set()
    to_visit = [url]

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                print(f"Visited: {current_url}")
                visited.add(current_url)

                for link in soup.find_all('a', href=True):
                    href = link['href']
                    if href.startswith('http') and href not in visited:
                        to_visit.append(href)
        except Exception as e:
            print(f"Error visiting {current_url}: {e}")

if __name__ == "__main__":
    start_url = "https://example.com"
    simple_crawl(start_url)
