from header import *

#todo cleanup code
#todo make downloader script

base_url = 'http://kisscartoon.me'
driver = webdriver.Chrome(DRIVER_PATH)

def get_element(element_id):
    while True:
        try:
            element = driver.find_element_by_id(element_id)
            break
        except NoSuchElementException:
            time.sleep(1)
    return element
                
#go to login page
driver.get(LOGIN_PAGE)

#traverse elements
get_element('username').send_keys(USERNAME)
get_element('password').send_keys(PASSWORD)
get_element('btnSubmit').click()

#return to main tab from pop-up
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.PAGE_UP)

#go to target page
parent_page = TARGET_PAGE
try:
    driver.get(parent_page)
except UnexpectedAlertPresentException:
    driver.switch_to_alert().accept()
    driver.find_element_by_tag_name('body').send_keys('Escape')
    driver.get(parent_page)

#get episode listing
try:
    soup = BeautifulSoup(driver.page_source,'html.parser')
except UnexpectedAlertPresentException:
    driver.switch_to_alert().accept()
    soup = BeautifulSoup(driver.page_source,'html.parser')
    
table = soup.find('table').find_all('a')

ep_links = []
for item in table:
    ep_links.append({'url':base_url+item.get('href').replace('&amp;','&'),'title':item.text.lstrip()})

#get download links
dl_links = []
for item in ep_links:
    print('\nCRAWLING THE PAGE OF '+item['title'])
    try:
        try:
            driver.set_page_load_timeout(10)
            driver.get(item['url'])
            print('SPIDER: That page was fast!')
        except TimeoutException:
            print('SPIDER: I will crawl this timed out page instead...')
            pass
    except UnexpectedAlertPresentException:
        driver.switch_to_alert().accept()
        driver.find_element_by_tag_name('body').send_keys('Escape')
        driver.get(item['url'])
        while True:
            try:
                time.sleep(1)
            except TimeoutException:
                #the page has "loaded"
                break

    while True:
        try:
            try:
                link = driver.find_element_by_link_text('1280x720.mp4').get_attribute('href').replace('&amp;','&')
                break
            except TimeoutException:
                #reload the damn page with a lenient timeout
                print('-SPIDER: Using a lenient timeout for this one...')
                driver.set_page_load_timeout(30)
                driver.get(item['url'])
        except NoSuchElementException:
            print('-SPIDER: Help! I think I bumped into a CAPTCHA! D:')
            time.sleep(5)
            
    print('-SPIDER: Got the link now! On to the next! :D')
    dl_links.append(link)

    
driver.quit()
with open('dl_links.txt','w') as f:
    json.dump({'value':dl_links},f)
    
    
    

    

    
