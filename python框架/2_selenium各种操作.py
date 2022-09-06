from selenium.webdriver import Chrome


def main():
    # 创建浏览器对象
    web = Chrome()

    web.get('http://lagou.com')

    print(web.title)


if __name__ == '__main__':
    main()
