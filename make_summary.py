import sys
from newspaper import Article

example_url = 'https://www.cnn.com/2021/01/18/us/inauguration-protests-vigilant/index.html'
example_url2 = 'https://mashable.com/article/github-fired-over-nazi-concern/'

def generate_summary(url=example_url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    return article.summary

if __name__ == '__main__':
    article_url = None if len(sys.argv) < 2 else sys.argv[1]
    kwargs = dict(url=article_url)
    summary = generate_summary(**{k: v for k, v in kwargs.items() if v is not None})
    print(summary)
