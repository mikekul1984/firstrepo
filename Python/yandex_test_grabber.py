# -*- coding: utf-8 -*- 
from selenium import webdriver
import re
import lxml.html
import time
import urlparse
from urllib import urlencode
import sys;
reload(sys);
#import psycopg2
import optparse

RELEVANCE_MAPPING = {
                     'Vital' : 4.0,
                     'Useful' : 3.0,
                     'Relevant' : 2.0,
                     'Partial_relevant' : 1.0,
                     'Useless' : 0.0
                    }

RELEVANCE_UNDEFINED = set(['--',
                           'impossible',
                           'not_open',
                           'foreign_lang',
                           'specific_content',
                           'other_reason'])



#def getQueryDocRelevance(query, url):
#    conn = psycopg2.connect(database="assessment4dev", user="assess_developer", password="assessment", host="searchqa-db.search.km", port="5432")
#    cursor = conn.cursor()    
#    cursor.callproc('testing.get_scores_for_query_doc', [query, url])
#    results = cursor.fetchall()
#    conn.close()
#
#    filtered = filter(lambda x: x not in RELEVANCE_UNDEFINED, [res[1] for res in results])
#
#    return None if 0 == len(filtered) else sum([RELEVANCE_MAPPING[label] for label in filtered]) / len(filtered)




queries = ["genby", "путин","владимир путин" ]

def initialiseBrowser():
#    driver=webdriver.PhantomJS()
    driver=webdriver.PhantomJS(desired_capabilities={'phantomjs.page.settings.loadImages': False,  'javascriptEnabled': False})
    return driver
    
def searchGoogle(driver, query):
    query_decoded=query.decode("utf-8")
    #print query_decoded
    driver.get("http://google.ru/search?" + urlencode({'q': query}))
    time.sleep(2)
    html = driver.page_source
    html=html.encode("utf-8")
    return html


def searchYandex(driver, query):
    query_decoded=query.decode("utf-8")
    #print query_decoded
    driver.get("http://ya.ru")
    inputElement = driver.find_element_by_id("text")
    inputElement.send_keys(query_decoded)
    inputElement.submit()
    time.sleep(2)
    html = driver.page_source
    html=html.encode("utf-8")
    #f = open(query + '.html', 'w')
    #f.write(html)
    #f.close()
    #check if yandex banned query then std print error and continue
    if (("Нам очень жаль, но запросы, поступившие" in html) or ("Введите, пожалуйста, символы с картинки в поле ввода" in html)):
        print 'Yandex banned: ' + query_decoded + '\n'
        raise
    return html





def parseGoogle(html, query):
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
        number = number + 1
        print str(number) + ":" + href# + ":" + str(getQueryDocRelevance(query, href))



def parseYandexIssue(html):
    #print 'GoingToParse\n'
    parser = lxml.html.HTMLParser(encoding = 'utf-8')
    doc = lxml.html.document_fromstring(html, parser=parser)
    
    misspell = doc.xpath('//div[@class="b-misspell g-gap-horizontal"]/a')
    if (len(misspell) == 0):
        misspell = doc.xpath('//div[@class="misspell__message"]')
        if (len(misspell) == 0):
            # опечаток не замечено
            #print 'Опечаток в запросе не замечено\n'
            pass
        else:
            old_query = misspell[0].text_content()
            #print 'Old query:\t'+old_query
            goodspell = doc.xpath('//input[starts-with(@id, "uniq")]')
            new_query = goodspell[0].attrib['value']
            #print 'New query:\t'+ new_query
            new_query = new_query
            
    else:
        old_query = misspell[0].text_content()
        #print 'Old query:\t'+old_query
        goodspell = doc.xpath('//td[@class="b-search__input"]/span/span/input[starts-with(@id, "uniq")]')
        new_query = goodspell[0].attrib['value']
        #print 'New query:\t'+ new_query
        new_query = new_query
    
    lis = doc.xpath('//div[contains(@class,"b-body-items")]/ol/li')
    divs = 0
    if not lis:
        divs = doc.xpath('//div[contains(@class, "serp-list")]')
        #print 'Lost lis\n'
    else:
        #print 'There are lis\n'
        pass
    number = 0
    if divs:
        #print 'In Divs\n'
        div = divs[0]
        h2s = div.xpath('.//h2[contains(@class, "serp-item__title")]')
        for h2 in h2s:
            #print 'In h2s\n'
            link = h2.xpath('.//a[contains(@class,"serp-item__title-link")]')
            if  (len(link) == 0):
                link = h2.xpath('.//a[@class="b-link"]')
                if (len(link) == 0):
                    # может случиться, если это сепаратор
                    continue
            href = link[0].attrib['href']
            if 'yabs.yandex.ru' in href:
                continue
            number = number + 1
            print str(number) + ' ' + href

            continue

    for li in lis:
        num = li.xpath('.//b[@class="b-serp-item__number"]')
        if (len(num) == 0):
            # это вставка яндекса - нужно парсить, чтобы узнать, какая именно
            link = li.xpath('.//a[@class="b-serp-item__title-link"]')
            if  (len(link) == 0):
                link = li.xpath('.//a[@class="b-link"]')
                if (len(link) == 0):
                    # может случиться, если это сепаратор
                    #print 'I think it is separator\n'
                    continue

        href = url[0].attrib['href']
        print number + ' ' + href
if __name__ == '__main__':   
	opts_parser = optparse.OptionParser()
	opts_parser.add_option('--docsSource', action='store', dest = 'docsSource')

	opts, args = opts_parser.parse_args()

	print opts.docsSource
	if opts.docsSource is None:
		raise RuntimeError("Must specify --docsSource")
	if opts.docsSource not in ('yandex',  'google'):
		raise RuntimeError("Source must be \'yandex\' or \'google\'")

	browser = initialiseBrowser()
#	browser.implicitly_wait(30)
	for query in queries:
		if opts.docsSource == 'google':
			html = searchGoogle(browser, query)
			if html:
				print "query:" + query
				parseGoogle(html, query)
		if opts.docsSource == 'yandex':
			#    html = searchGoogle(browser, query)
			html = searchYandex(browser, query)
			if html:
				print "query:" + query
				parseYandexIssue(html)

	browser.quit()
