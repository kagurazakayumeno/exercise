from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from bs4 import BeautifulSoup
from time import sleep
import requests
import threading
import os
import re


def photo_download(name, link):
    photo = requests.get(link)
    filename = 'photo/' + name + '.jpg'
    with open(filename, 'wb') as f:
        f.write(photo.content)


def main(page=5):
    url = 'https://sh.zu.fang.com/'
    option = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    option.add_experimental_option("prefs", prefs)
    # option.add_argument('headless')
    driver = webdriver.Chrome(options=option, executable_path='C:\Program Files\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
    driver.set_window_size(1920, 2000)
    try:
        driver.find_element_by_id('closecover').click()
        sleep(1)
    except NoSuchElementException:
        pass
    except ElementNotInteractableException:
        pass
    driver.find_element_by_id('input_key').send_keys('闵行')
    driver.find_element_by_id('rentid_39').click()
    sleep(1)
    for _ in range(page):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        info = soup.find_all(class_='list hiddenMap rel')
        if not os.path.exists('photo'):
            os.mkdir('photo')
        for i in info:
            addr = i.find('p', class_="gray6 mt12").get_text(strip=True)
            price = i.find('p', class_="mt5 alingC").get_text(strip=True)
            price = re.sub('/', '-', price)
            link = i.find('img').get('data-src')
            if link.startswith('//'):
                link = 'https:' + link
            name = addr + "-" + price
            threading.Thread(target=photo_download, args=(name,link)).start()
            while threading.active_count() > 3:
                sleep(3)
        driver.find_element_by_link_text('下一页').click()
        sleep(1)
        try:
            driver.find_element_by_id('closecover').click()
            sleep(1)
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass


if __name__ == '__main__':
    main()
