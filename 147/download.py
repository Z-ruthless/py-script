import requests
from lxml import etree

header = {
    # ':authority':'www.147xiaoshuo.com',
    # ':method':'GET',
    # ':path':'/book/5876/88141.html',
    # ':scheme':'https',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control':'max-age=0',
    'Cookie':'cf_clearance=XQYMt.Nzsvmu7LWcTcAeLFj58XP1PNl9BC7CqZTQ1Co-1691331610-0-1-446f0421.5723b051.739eeb7a-0.2.1691331610',
    'Dnt':'1',
    'If-Modified-Since':'Sun, 06 Aug 2023 12:32:40 GMT',
    'Sec-Ch-Ua':'"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'"Windows"',
    'Sec-Fetch-Dest':'document',
    'Sec-Fetch-Mode':'navigate',
    'Sec-Fetch-Site':'none',
    'Sec-Fetch-User':'?1',
    'Sec-Gpc':'1',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188'
}


http = 'https://www.147xiaoshuo.com'
filePath = '小说保存在自己电脑上的位置，从盘符开始'
def download(linkNext):
    while True:
        # 获取章节信息
        get_http = http + linkNext
        print('请求地址： {}'.format(get_http))
        get_html = requests.get(get_http,headers=header )
        print('请求状态 = {}'.format(get_html.status_code))
        print('请求状态原因 = {}'.format(get_html.reason))
        req_html = etree.HTML(get_html.content, etree.HTMLParser())
        title = req_html.xpath('/html/head/title/text()')
        title_content = str(title[0]).split('_')[0] 
        print('章节名称： {}'.format(title_content))
        # 获取小说内容
        save_p = req_html.xpath('//div[@id="content"]/text()')
        print('save_p = {}'.format(save_p))
        save_content = str(save_p).replace('<p>','    ').replace('</p>','\n')
        f = open(filePath, "a")
        f.write(title_content + '\n' + save_content)
        f.close()
        # 获取下一章地址
        linkNextStr = req_html.xpath('/html/body/div/div[5]/div[7]/a[3]/@href')
        linkNext = str(linkNextStr[0])

download('/book/5876/88141.html')