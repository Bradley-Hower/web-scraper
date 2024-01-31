import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Hip_dysplasia'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

def get_citations_needed_count():
  """Locates links within paragraphs with the title 'Wikipedia:Citation needed'. This anchor title allows the citation-needed paragraphs to be identified."""
  global soup

  count = 0

  page_paragraphs = soup.select("p > sup > i > a")

  for item in page_paragraphs:
    if item["title"] == "Wikipedia:Citation needed":
      count += 1
  print(count)
  print("\n")

def get_citations_needed_report():
  """Using the citation-needed locator, found in the title attribute of certain anchor tags, is able to scope up the heiarchy to the paragraph tag, thus locating the paragraph lacking citation."""
  global soup

  page_paragraphs = soup.select("p > sup > i > a")

  for item in page_paragraphs:
    if item["title"] == "Wikipedia:Citation needed":
      print(item.parent.parent.parent.text)
      print("-----------------")

get_citations_needed_count()
get_citations_needed_report()