from lxml import etree

parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('python爬虫/a.html', parser=parser)

# 取指定位置的某个
# res = tree.xpath('/html/body/ul/li[1]/text()')
# print(res)

# 属性筛选 取href=dapao的
# res = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')
# print(res)

# 获取列表
lst = tree.xpath('/html/body/ol/li')
for it in lst:
    a = it.xpath('./a/text()')
    print(a)
    href = it.xpath('./a/@href')
    print(href)

print(tree.xpath('/html/body/ul/li/text()'))
print(tree.xpath('/html/body/ul/li/@href'))