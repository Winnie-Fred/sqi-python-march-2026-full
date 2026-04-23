import requests

from bs4 import BeautifulSoup

url = "https://www.netflix.com/ng/"


try:
    response = requests.get(url)
except requests.exceptions.RequestException as e:
    print("Something went wrong. Check your internet connection and try again")
else:
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        with open("netflix-homepage.html", "w", encoding="utf-8") as f:
            f.write(soup.prettify())
    else:
        print(f"Unexpected status code: {response.status_code}")
        