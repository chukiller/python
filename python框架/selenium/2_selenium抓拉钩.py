from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# 指定驱动位置，防止闪退
driver_path = Service(r'C:\Program Files\Python310\chromedriver.exe')


def main():
    # 创建浏览器对象
    web = Chrome(service=driver_path)
    web.get('http://lagou.com')
    # 点击【全国】按钮
    web.find_element(By.XPATH, '//*[@id="changeCityBox"]/p[1]/a').click()
    # 找到输入框，输入python，回车
    web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)
    sleep(3)
    # 查找存放数据的位置并提取
    li_list = web.find_elements(By.CLASS_NAME, 'item__10RTO')
    for li in li_list:
        org = li.find_element(By.XPATH, './div[1]/div[2]/div[1]/a')
        title = li.find_element(By.TAG_NAME, 'a')
        price = li.find_element(By.CLASS_NAME, 'money__3Lkgq')
        print(org.text, title.text, price.text)
    web.close()


if __name__ == '__main__':
    main()
