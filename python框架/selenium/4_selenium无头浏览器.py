from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# 指定驱动位置，防止闪退
driver_path = Service(r'C:\Program Files\Python310\chromedriver.exe')
# 隐藏浏览器
opt = Options()
opt.add_argument('--headless')
opt.add_argument('--disable-gpu')


# 无头浏览器，让浏览器后台运行
def main():
    # 创建浏览器对象
    web = Chrome(service=driver_path, options=opt)
    web.get('https://www.endata.com.cn/BoxOffice/BO/Year/index.html')
    # 获取页面代码
    print(web.page_source)
    sleep(1)
    # 定位到下拉框
    sel_el = web.find_element(By.XPATH, '//*[@id="OptionDate"]')
    sleep(1)
    sel = Select(sel_el)
    # 让浏览器选择下拉框
    for i in range(len(sel.options)):   # i 就是每个下拉框的索引
        sel.select_by_index(i)
        sleep(2)
        table = web.find_element(By.ID, 'TableList')
        print(table.text)


if __name__ == '__main__':
    main()
