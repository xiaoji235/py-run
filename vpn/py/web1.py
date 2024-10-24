import requests
from bs4 import BeautifulSoup

url = 'https://blog.banyunxiaoxi.icu'
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

first_title = soup.find_all(class_='title')[0].a['href']
#print(first_title)
new_url = first_title
response = requests.get(new_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

blockquote = soup.find('blockquote')
if blockquote:
    p = blockquote.find('p')
    if p:
        blockquote_content = p.get_text().replace('<br />', '')
        print(blockquote_content)
    else:
        print("")
else:
    print("")
