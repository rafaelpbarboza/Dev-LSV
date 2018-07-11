import os

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

BASE_DIR = os.path.dirname(__file__)


class RobotBase():
    def __init__(self):
        self.driver = WebDriver(executable_path=os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver'))
        self.page = 1

    def run(self, *args):
        pass

    def query(self):
        pass


class RobotElUniversal(RobotBase):
    def __init__(self, kwords, max_pagination=0):
        RobotBase.__init__(self)
        self.max_pagination = max_pagination
        self.kwords = kwords

    def run(self):
        news = []
        self.page = 0
        while self.page != self.max_pagination or self.max_pagination == 0:
            self.query()
            if len(self.driver.find_elements_by_class_name('pager')) == 0:
                break
            [news.append([new.text, new.find_element_by_tag_name('a').get_attribute('href')])
             for new in self.driver.find_elements_by_class_name('title') if new.text != "SITE"]
        self.driver.quit()
        return news

    def query(self):
        url = "http://www.eluniversal.com.co/search/site/" + self.kwords + "?page=" + str(self.page)
        self.driver.get(url)
        self.page += 1


class RobotElTiempo(RobotBase):
    def __init__(self, kwords, max_pagination=0):
        RobotBase.__init__(self)
        self.max_pagination = max_pagination + 1
        self.kwords = kwords

    def run(self):
        news = []
        while self.page != self.max_pagination or self.max_pagination == 1:
            self.query()
            if len(self.driver.find_elements_by_class_name('pagination')) == 0:
                break
            [news.append([new.text, new.get_attribute('href')]) for new in
             self.driver.find_elements_by_class_name('title') if new.text != ""]
        self.driver.quit()
        return news

    def query(self):
        url = 'http://www.eltiempo.com/buscar/' + str(self.page) + '?q=' + self.kwords
        self.driver.get(url)
        self.page += 1


class RobotGoogle(RobotBase):
    def run(self, *args):
        kwords = [word + " " for word in args]
        self.driver.get('http://www.google.com/')
        self.driver.find_element_by_name('q').send_keys(kwords, Keys.RETURN)
        self.driver.quit()
