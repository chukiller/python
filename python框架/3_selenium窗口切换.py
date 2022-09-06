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
    sleep(1)
    # 找到输入框，输入python，回车
    web.find_element(By.XPATH, '//*[@id="search_input"]').send_keys('python', Keys.ENTER)
    sleep(1)
    # 点击打开新窗口
    # 在selenium眼中，当前窗口还在旧窗口，需要切换
    web.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
    web.switch_to.window(web.window_handles[-1])
    # 在新窗口中提取内容
    job_detail = web.find_element(By.XPATH, '//*[@id="container"]/div[1]')
    print(job_detail.text)
    # 关闭新窗口，回到旧窗口
    web.close()
    web.switch_to.window(web.window_handles[0])
    # iframe
    # iframe = web.find_element('//*[@id="iframexxxxx"]')
    # web.switch_to.frame(iframe)
    # 切回原来的页面
    # web.switch_to.default_content()


if __name__ == '__main__':
    main()
