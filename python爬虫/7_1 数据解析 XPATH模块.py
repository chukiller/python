from lxml import etree

xml = '''
<book>
    <id>1</id>
    <name>张三</name>
    <price>1.23</price>
    <author>
        <nick id="1001">张1</nick>
        <nick id="1002">张2</nick>
        <nick class="jj1">张3</nick>
        <nick class="jj2">张4</nick>
        <div>
            <nick>哈哈哈1</nick>
        </div>
        <span>
            <nick>哈哈哈2</nick>
        </span>
    </author>
    <partner>
        <nick id="1003">阿萨德</nick>
        <nick id="1004">卡萨丁</nick>
    </partner>
</book>
'''

tree = etree.XML(xml)

# 查找name节点里的文本
# res = tree.xpath("/book/name/text()")
# print(res)

# res = tree.xpath("/book/author/nick/text()")
# print(res)

# 查找author节点下的所有nick节点
# res = tree.xpath("/book/author//nick/text()")
# print(res)

# 查找author节点下最后节点的nick
res = tree.xpath("/book/author/*/nick/text()")
print(res)