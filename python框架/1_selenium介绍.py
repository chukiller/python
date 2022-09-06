# 能让程序连接到浏览器，让浏览器完成复杂操作
# selenium：自动化测试工具
# 开发者可以通过selenium提取网页上的各种信息
# pip install selenium
# 下载浏览器驱动：https://npm.taobao.org/mirrors/chromedriver/
# 把解压后的chromedriver放在python解释器所在的文件夹
from selenium.webdriver import Chrome

def main():
    # 创建浏览器对象
    web = Chrome()

    web.get('http://www.baidu.com')

    print(web.title)

if __name__ == '__main__':
    main()
