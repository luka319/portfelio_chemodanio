# Скачиваем все изображения со страницы

# Следующий скрипт скачает все изображения 
# и сохранит их в downloaded_images/. Только 
# сначала не забудьте создать соответствующий каталог.


import requests  
from lxml import html  
import sys  

# import urlparse  # in py2
import urllib.parse # in py3

response = requests.get('https://500px.com')  
parsed_body = html.fromstring(response.text)

# Парсим ссылки с картинками
images = parsed_body.xpath('//img/@src')  
# images = parsed_body.xpath('/html/body/section[5]/div[3]/div[1]/div[1]/div[1]/a')

if not images:  
    sys.exit("Found No Images")

# Конвертирование всех относительных ссылок в абсолютные
images = [urllib.parse.urljoin(response.url, url) for url in images]  

print( 'Found %s images' % len(images))

# Скачиваем только первые 10
for url in images[0:10]:  
    r = requests.get(url)
    # f = open('downloaded_images/%s' % url.split('/')[-1], 'w')
    f = open('500px_images/%s' % url.split('/')[-1], 'wb')
  
# https://500px.com/photo/80626185/refreshments-by-tim-santasombat
            
    f.write(r.content)
    f.close()
