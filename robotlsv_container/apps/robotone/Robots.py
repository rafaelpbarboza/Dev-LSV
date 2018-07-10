import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


# BASE_DIR = os.path.dirname(os.path.dirname(__file__))


def robot_eluniversal(kwords):
    driver = WebDriver(executable_path=os.path.join('apps/robotone/', 'driver', 'chromedriver'))
    driver.get('http://www.eluniversal.com.co/')
    search = driver.find_element_by_id('edit-search-nuevo')
    search.send_keys(kwords)
    search.send_keys(Keys.RETURN)
    page = 0
    news = []
    url = driver.current_url
    while True:
        driver.get(url + '?page=' + str(page))
        if len(driver.find_elements_by_class_name('title')) == 1:
            break
        [news.append([new.text, new.find_element_by_xpath(".//*").get_attribute('href')])
         for new in driver.find_elements_by_class_name('title') if new.text != "SITE"]
        page += 1
    driver.quit()
    return news
