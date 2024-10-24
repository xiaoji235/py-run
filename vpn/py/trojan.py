import requests
from bs4 import BeautifulSoup

# 目标URL
url = 'https://clashnode.cc/node-real-time-update/'

# 自定义headers
headers = {
'Cookie': '_ga_QFS5X6BRSK=GS1.1.1729738735.1.1.1729738882.0.0.0; _ga=GA1.1.1842555548.1729738735',
'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
}

# 发送GET请求
response = requests.get(url, headers=headers)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找所有具有data-value属性的元素
    data_values = soup.find_all(attrs={"data-value": True})

    # 遍历并输出所有data-value的值
    for element in data_values:
        print(element['data-value'])
else:
    print(f"请求失败，状态码：{response.status_code}")