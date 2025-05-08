import requests

def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:
        f.write(r.text)
    print(f"✅ File saved to {path}")

url = "https://timesofindia.indiatimes.com/education/news/the-world-university-rankings-2025-iisc-leads-india-check-the-list-of-top-10-indian-institutes-here/articleshow/114071088.cms"

fetchAndSaveToFile(url, "data/times.html")
