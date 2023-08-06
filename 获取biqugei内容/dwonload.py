import requests
from lxml import etree


headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
http = 'http://www.biqugei.net/read/'
postHttp = 'http://www.biqugei.net/api/reader_js.php'
filePath = '小说保存在自己电脑上的位置，从盘符开始'
def download(articleid,chapterid):
    while True:
        # 获取章节信息
        get_http = http + articleid + '/'  + chapterid + '.html'
        get_html = requests.get(get_http)
        req_html = etree.HTML(get_html.content, etree.HTMLParser())
        title = req_html.xpath('///html/head/title/text()')
        title_content = str(title[0]).split('_')[0] 
        print('章节名称： {}'.format(title_content))
        # 获取小说内容
        params = {'articleid':articleid,'chapterid':chapterid}
        res = requests.post(postHttp,data=params,headers=headers)
        save_content = str(res.text).replace('<p>','    ').replace('</p>','\n').replace('<!--<divalign="center">','---------------\n')
        f = open(filePath, "a")
        f.write(title_content + '\n' + save_content)
        f.close()
        # 获取下一章地址
        linkNext = req_html.xpath('//a[@id="linkNext"]/@href')
        linkNextStr = str(linkNext[0]).split('/')
        articleid = linkNextStr[2]
        chapterid = linkNextStr[3].split('.')[0]
# download('99462','5619522');