import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys


# BASE_DIR = os.path.dirname(os.path.dirname(__file__))

class RobotBase():
    def __init__(self):
        self.driver = WebDriver(executable_path=os.path.join('apps/robotone/', 'driver', 'chromedriver'))

    def run(self, **kwargs):
        pass


class RobotElUniversal(RobotBase):
    def run(self, *args):
        kwords = [word+" " for word in args]
        self.driver.get('http://www.eluniversal.com.co/')
        search = self.driver.find_element_by_id('edit-search-nuevo')
        search.send_keys(kwords)
        search.send_keys(Keys.RETURN)
        page = 0
        news = []
        url = self.driver.current_url
        while True:
            self.driver.get(url + '?page=' + str(page))
            if len(self.driver.find_elements_by_class_name('title')) == 1:
                break
            [news.append([new.text, new.find_element_by_xpath(".//*").get_attribute('href')])
             for new in self.driver.find_elements_by_class_name('title') if new.text != "SITE"]
            page += 1
        self.driver.quit()
        return news
