# To start with my web scraper, I went to my Windows command prompt and installed requests, lxml and bs4 also known as Beautiful Soup
# Once that has been downloaded, the next step is to go into my jupyter notebook and import requests and bs4

import requests
import bs4

# This is to get a response from the website
result = requests.get("https://www.google.com")

type(result)
result.text

soup= bs4.BeautifulSoup(result.text,"lxml")

soup

# This will help you grab raw elements from the website
soup.select("title")
soup.select("header")
soup.select("p")