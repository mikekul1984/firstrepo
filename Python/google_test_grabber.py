# -*- coding: utf-8 -*- 
from selenium import webdriver
import re
import lxml.html
import time
import urlparse
from urllib import urlencode
import sys;
reload(sys);

queries = ["genby", "путин","владимир путин" ]

def initialiseBrowser():
    #driver=webdriver.PhantomJS()
    driver=webdriver.PhantomJS()
    return driver
    
def searchGoogle(driver, query):
    query_decoded=query.decode("utf-8")
    #print query_decoded
    driver.get("http://google.ru/search?" + urlencode({'q': query}))
    #inputElement = driver.find_element_by_id("lst-ib")
    #inputElement.send_keys(query_decoded)
    #inputElement.submit()
    time.sleep(2)
    html = driver.page_source
    html=html.encode("utf-8")
    #f = open(query + '.html', 'w')
    #f.write(html)
    #f.close()
    #check if yandex banned query then std print error and continue
#    if (("Нам очень жаль, но запросы, поступившие" in html) or ("Введите, пожалуйста, символы с картинки в поле ввода" in html)):
#        print 'Yandex banned: ' + query_decoded + '\n'
#        raise
    return html

def parseGoogle(html):
    #print 'GoingToParse\n'
    parser = lxml.html.HTMLParser(encoding = 'utf-8')
    doc = lxml.html.document_fromstring(html, parser=parser)
   
    lis = doc.xpath('//div[contains(@id,"ires")]/ol/li')
    divs = 0
    if not lis:
        divs = doc.xpath('//li[contains(@class, "g")]')
        #print 'Lost lis\n'
    else:
        #print 'There are lis\n'
        pass
    number = 0
    if divs:
        #print 'In Divs\n'
        div = divs[0]
        #h2s = div.xpath('.//h3[contains(@class, "r")]')
        for h2 in divs:
            href = h2[0].attrib['href']
            number = number + 1
            print str(number) + " : "  + href
            #self.urls.append([number, href])
            continue
    number = 0
    for li in lis:
        #divv = li.xpath('//div[@class="rc"]')
        res = li.xpath('.//h3[@class="r"]')
        url = res[0].xpath('.//a[@target="_blank"]')
        if (len(url) == 0):
            #print 'During lis there is no url\n'
            # почему-то нет урла может быть, если это сепаратор
            continue
        href_from_html ="http://www.google.ru" + url[0].attrib['href']
        href_query = urlparse.urlparse(href_from_html).query
        que = urlparse.parse_qs(href_query)
        href = que['q'][0]
        #print url[0]
        print str(number) + ":" + href
        number = number + 1
   
browser = initialiseBrowser()
for query in queries:
    html = searchGoogle(browser, query)
    if html:
        # страница плохая
        print "query:" + query
        parseGoogle(html)

browser.quit()
