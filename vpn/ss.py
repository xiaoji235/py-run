import requests

# 目标API URL
api_url = 'https://api.github.com/repos/Barabama/FreeNodes/contents/nodes'

def get_txt_urls(api_url):
    # 获取json数据
    response = requests.get(api_url)
    # 确保请求成功
    response.raise_for_status()
    # 解析json数据
    content_list = response.json()
    # 筛选出所有txt文件的URL
    txt_urls = [content['download_url'] for content in content_list if content['name'].endswith('.txt')]
    return txt_urls

def merge_txt_contents(txt_urls):
    merged_content = ''
    for url in txt_urls:
        # 获取txt文件的内容
        response = requests.get(url)
        # 确保请求成功
        response.raise_for_status()
        # 合并内容
        merged_content += response.text
    return merged_content

def main():
    try:
        txt_urls = get_txt_urls(api_url)
        merged_content = merge_txt_contents(txt_urls)
        print(merged_content)
    except requests.RequestException as e:
        print(f'请求错误: {e}')

if __name__ == '__main__':
    main()
