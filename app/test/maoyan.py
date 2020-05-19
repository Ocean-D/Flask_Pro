import requests

def get_html():
    url = 'https://maoyan.com/board'
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        html = r.text
        return html

    except Exception as e:
        raise e

result = get_html()
print(result)