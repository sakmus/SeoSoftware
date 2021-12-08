from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input("Enter the full URL of the page: ")

try:
  # Initial variables
  html = urlopen(url)  
  keyword = input("Enter your seo keyword: ").casefold()
  data = BeautifulSoup(html, "html.parser")

  # Functions
  def key_title(keyword, data):
    return (keyword in data.title.text.casefold()) if data.title else None

  def stop_title(data):
    if data.title:
      words = 0
      ls_words = []
      with open('stopwords.txt', 'r') as f:
        for line in f:
          if re.search('r\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
            words += 1
            ls_words.append(line.rstrip('\n'))
      return f"{words} stop word(s) found in title. Consider removing {ls_words}" if words else "No stop word found"


  # Recall the functions
  print(key_title(keyword, data))
  print(stop_title(data))

except:
  print("Failed to process the URL :(. The url might be broken.")