import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

url = 'https://www.cnn.com/2021/01/10/politics/paid-sick-leave-covid-benefit-expiration/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') # optional: try lxml instead
headline = soup.find('h1').get_text()
div_tags = soup.findAll('div', {'class': 'zn-body__paragraph'})
#p_tags = soup.findAll('p', {'class': 'zn-body__paragraph'})
div_tags_text = [tag.get_text().strip() for tag in div_tags]
