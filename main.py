from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

print("\n\nThe prefix + means a positive point and - means a negative point. If you encounter any issues, make sure to inform us via GitHub or send e-mail at sakeef.mushfique@outlook.com\n\n")

url = input("Enter the full URL of the page: ")

try:
  # Initial variables
  html = urlopen(url)  
  keyword = input("Enter your seo keyword: ").casefold()
  data = BeautifulSoup(html, "html.parser")

  # Functions

  # Check Title of the page
  def check_title(keyword, data):
    if data.title:
      print("+ Title is available for this page.")

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
    else: print("- Title is not available for this page.")
  
  # Check description of the page
  def check_desc(keyword, data):
    # Get the description
    for tag in data.find_all('meta'):
      if tag.get('name') == "description":
        desc = tag.get('content')
        break
    
    if desc:
      print("+ Meta description is avaliable")

      # Check keyword
      print("+ Keyword found in meta description." if keyword in desc else "- Keyword not found in meta description.")

      # Check length
      if len(desc) > 49 and len(desc) < 161: print("+ Meta description length is fit.")
      elif len(desc) < 50: print("- Meta description is too short. Make it more than 50.")
      else: print("- Meta description is too big. Make it upto 160.")

      # Check for double quotes
      print("- Double quotes found in the description." if '"' in desc else "+ No double quotes found in the description.")

    else: print("Meta description is not available")





  # Recall the functions
  check_title(keyword, data)
  check_desc(keyword, data)

except:
  print("Failed to process the URL :(. The url might be broken.")