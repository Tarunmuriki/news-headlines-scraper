import requests
from bs4 import BeautifulSoup

def fetch_headlines(url, output_file="headlines.txt"):
    try:
        # Send GET request with headers to mimic a browser
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            print(f"Failed to fetch page, status code: {response.status_code}")
            return

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (using h2 tags as example)
        headlines = soup.find_all("h2")

        with open(output_file, "w", encoding="utf-8") as f:
            for i, h in enumerate(headlines, 1):
                text = h.get_text(strip=True)
                if text:
                    f.write(f"{i}. {text}\n")

        print(f"✅ Headlines saved to {output_file}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Example: BBC News (you can change to another site)
    url = "https://www.bbc.com/news"
    fetch_headlines(url)
