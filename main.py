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
  def check_title(keyword, data):
    if data.title:
      # Check Keyword
      print("+ Keyword found in title." if keyword in data.title.text.casefold() else "- Keyword is not in title.")

      # Check stop words
      words = 0
      ls_words = []
      with open('stopwords.txt', 'r') as f:
        for line in f:
          if re.search('r\b' + line.rstrip('\n') + r'\b', data.title.text.casefold()):
            words += 1
            ls_words.append(line.rstrip('\n'))
      print("- {words} stop word(s) found in title. Try removing: {ls_words}" if words else "+ No stop word found in title.")

      # Check length
      leng = len(data.title.text)
      if leng > 49 and leng < 61: print("+ Title is fit by length.")
      elif leng > 60: print("- Title is too big. Trim it down to 60.")
      else: print("- Title is too short. Add some characters to make it more than 50.")

  # Recall the functions
  check_title(keyword, data)

except:
  print("Failed to process the URL :(. The url might be broken.")