import re
import requests

url = 'https://fanyi.baidu.com/sug'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
# }

dic = {
    'kw': 'dog'
}

# res = requests.post(url, dic, headers=headers)
res = requests.post(url, dic)
print(res)
print(res.json())
res.close()