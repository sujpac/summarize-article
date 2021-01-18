from newspaper import Article

# Unneeded imports:
# import nltk
# pip install nltk
# pip install newspaper3k

url = 'https://www.cnn.com/2021/01/10/politics/paid-sick-leave-covid-benefit-expiration/index.html'
article = Article(url)
article.download()
article.parse()
article.nlp()
# additional article properties
# useful_state = [
#     article.authors,
#     article.publish_date,
#     article.top_image,
#     article.keywords,
#     article.text,
# ]
print('Article Summary:\n', article.summary)
