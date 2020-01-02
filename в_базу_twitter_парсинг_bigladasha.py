import  urllib
from urllib import urlopen
from bs4 import BeautifulSoup

url = 'https://twitter.com/bigladasha'
page = urlopen(url)
soup = BeautifulSoup(page,'html.parser')

count = 0                                           # счетчик
all_tweets_count = soup.find('a',{'class':'ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav'})\
    .findAll('span')[1].text                        # количество твитов
all_tweets_count = all_tweets_count.replace(',','') # 1,152 -> 1152


while count < all_tweets_count:
    print soup.findAll('div', {'class': 'js-tweet-text-container'})[count].find('p').text
    print '---------------------------------------------------------------'
    count += 1

