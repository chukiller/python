from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

driver_path = Service(r'C:\Program Files\Python310\chromedriver.exe')


def main():
    username = '18359914140'
    password = 'a123123'
    web = Chrome(service=driver_path)
    web.get('https://www.chaojiying.com/user/login')
    # 输入用户名
    web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys(username)
    # 输入密码
    web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys(password)
    # 获取验证码
    img = web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
    cc = Chaojiying_Client(username, password, '938683')
    dic = cc.PostPic(img, 1902)
    code = dic['pic_str']
    # 输入验证码
    web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code)
    # 点击登录
    # web.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()


if __name__ == '__main__':
    main()
