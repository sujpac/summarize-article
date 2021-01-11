import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

url = 'https://www.cnn.com/2021/01/10/politics/paid-sick-leave-covid-benefit-expiration/index.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser') # Optional: try lxml instead
headline = soup.find('h1').get_text()
body_tags = soup.findAll(['div', 'p'], {'class': 'zn-body__paragraph'})
body_tags_text = [tag.get_text().strip() for tag in div_tags]

# Filter out sentences that contain newline or don't have periods
sentences = [sentence for sentence in body_tags_text if not '\n' in sentence]
sentences = [sentence for sentence in sentences if '.' in sentence]
article_text = ' '.join(sentences)

# Set size of summary to be one fourth of the article size
summary = summarize(article_text, ratio=0.25)

print('Length of article: ', len(article_text))
print('Length of summary: ', len(summary), '\n')
print('Article Summary: \n', summary)
