import requests

login_url = 'https://passport.17k.com/ck/user/login'

param = {
    'loginName': '18359914140',
    'password': 'a123123'
}

# 会话
session = requests.session()

res = session.post(url=login_url, data=param)

book_res = session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')

for it in book_res.json().get('data'):
    print('书名: %s' % (it.get('bookName')))
    print('作者: %s' % (it.get('authorPenName')))
    print('简介: %s' % (it.get('introduction')))
    print()
