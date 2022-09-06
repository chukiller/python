import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    # 防盗链
    'Referer': 'https://www.pearvideo.com/video_1731975'
}

url = 'https://www.pearvideo.com/video_1731975'
contId = url.split('_')[1]

videoStatusUrl = 'https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.904578136906016'

res = requests.get(videoStatusUrl, headers=headers)

print(res.text)

