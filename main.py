from urllib.request import urlopen
from bs4 import BeautifulSoup

'''
About the author,
Author: Sakeef Mushfique
E-mail: sakeef.mushfique@outlook.com
Newsletter: sakeef.substack.com
'''

url = input("Enter the full URL of the page: ")
keyword = input("Enter your seo keyword: ")

try:
  html = urlopen(url)  
except ValueError as e:
  print(e)
  exit()

data = BeautifulSoup(html, "html.parser")

def seo_title(keyword, data):
  if keyword.casefold() in data.title.text.casefold():
    status = "Found"
  else:
    status = "Not found"
  return status

print(seo_title(keyword, data))