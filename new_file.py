import requests
from bs4 import BeautifulSoup
from typing import List

# A class to represent the webpage
class Website:
    def __init__(self, url: str):
        self.url = url
        self.links: List[str] = []
        self.title: str = ""
        self.body: str = ""
        self.text: str = ""

        response = requests.get(url)
        self.body = response.content
        soup = BeautifulSoup(self.body, 'html.parser')
        self.title = soup.title.string if soup.title else "no title found"
        # Initialize links first
        links = [link.get('href') for link in soup.find_all('a')]
        self.links = [link for link in links if link]
        
        # Then handle the body text
        if soup.body:
            # Remove irrelevant tags
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            self.text = soup.body.get_text(separator="\n", strip=True)
        else:
            self.text = ""

    def get_contents(self):
        return f"webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"

# Example usage
ed = Website("https://edwarddonner.com")
print("Title:", ed.title)
print("Links found:", len(ed.links) if hasattr(ed, 'links') else 'No links attribute')
print("Attributes:", dir(ed))