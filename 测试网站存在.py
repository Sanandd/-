import requests
from bs4 import BeautifulSoup

def check_url_alive(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"URL {url} 可能无法访问，状态码: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"访问 {url} 时发生错误: {e}")
        return None

def extract_title(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    title_tag = soup.find('title')
    if title_tag:
        return title_tag.text.strip()
    return "没有找到标题"

def scan_websites(urls):
    for url in urls:
        print(f"正在检查: {url}")
        html_content = check_url_alive(url)
        if html_content:
            title = extract_title(html_content)
            print(f"网站标题: {title}")
        else:
            print(f"{url} 无法访问\n")
urls = [
   "xxx"
]
if __name__ == "__main__":
    scan_websites(urls)
