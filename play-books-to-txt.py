import bs4, requests
#import time
#from selenium import webdriver

#pageHTML = requests.get('https://books.google.com/books?op=library&hl=en&source=data_dashboard') 
myacc = open('myacc.html')
pageSoup = bs4.BeautifulSoup(myacc, "lxml")
authSoup = pageSoup.find_all('div', class_="slider-annotation-author")
titSoup = pageSoup.find_all('a', class_="slider-annotation-title", href=True)

fp = open('gpb-list.txt', 'w')

for i in range(len(authSoup)):
    if authSoup[i].text == '_USER_VOLUME_UNKNOWN_' or titSoup[i].text == '_USER_VOLUME_UNKNOWN_':
        continue
#        author[i] = ''
#        title[i] = ''
#        browser = webdriver.Firefox()
#        browser.get(titSoup[i]['href'])
#        #time.sleep(100)
#        ukHtml = browser.page_source
#        time.sleep(5)
#        ukHtml2 = browser.execute_script("return document.body.outerHTML")
#        ukSoup = bs4.BeautifulSoup(ukHtml2, "lxml")
#        uktit.append(ukSoup.find('title'))
#        browser.quit()
#        print(uktit)
    else:
        fp.write(titSoup[i].text + ' - ' + authSoup[i].text + '\n')

    i += 1
fp.close()
