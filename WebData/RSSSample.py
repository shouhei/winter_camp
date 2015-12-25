from urllib import request
import xml.etree.ElementTree as ET

if "__main__" == __name__:
    data = request.urlopen("http://d.hatena.ne.jp/naoya/rss")
    # data = request.urlopen("http://news.yahoo.co.jp/pickup/rss.xml")
    utf8_data = data.read().decode()
    tree_data = ET.fromstring(utf8_data)
    del tree_data[0]
    for post in tree_data:
        print(post[0].text)
