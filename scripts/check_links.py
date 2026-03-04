import sys, requests
from bs4 import BeautifulSoup

def check(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith('http')][:10]
        print(f"Checking top {len(links)} external links on {url}...")
        for link in links:
            try:
                r = requests.head(link, timeout=3)
                print(f"[{r.status_code}] {link}")
            except:
                print(f"[FAIL] {link}")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check(sys.argv[1])
