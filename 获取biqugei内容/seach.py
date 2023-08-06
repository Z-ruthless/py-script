import requests
from lxml import etree
import dwonload


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
# 传入url和请求头
searchHttp = 'http://www.biqugei.net/search/?searchkey='
searchDetail = 'http://www.biqugei.net'
print('请输入文本:')
while True:
    line = input()
    print('您输入的文本为： {}'.format(line))
    search = requests.get(searchHttp + line,headers=headers)
    print('搜索结果： {}'.format(search))
    status = search.status_code
    print('请求结果： {}'.format(status))
    html = etree.HTML(search.content, etree.HTMLParser())
    if status == 200:
        href = html.xpath('//div[@class=\"caption\"]/h4/a/@href')
        print('获取到的详情地址： {}'.format(href))
        name = html.xpath('//div[@class=\"caption\"]/h4/a/text()')
        print('名称： {}'.format(name[0]))
        author = html.xpath('//div[@class=\"caption\"]/small/text()')
        print('作者: {}'.format(author[0]))
        briefly = html.xpath('//div[@class=\"caption\"]/p/text()')
        print('简介： {}'.format(briefly[0]))
        detail_http = searchDetail + href[0]
        print('请求地址： {}'.format(detail_http))
        detail = requests.get(detail_http,headers=headers)
        detail_html = etree.HTML(detail.text, etree.HTMLParser())
        read_http = detail_html.xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/a[1]/@href')
        if(read_http != None):
            xsName = detail_html.xpath('//title/text()')
            articleid = read_http[0].split("/")[2]
            chapterid = read_http[0].split("/")[3].split(".")[0]
            dwonload.download(articleid,chapterid)
    else:
        print('查询失败')