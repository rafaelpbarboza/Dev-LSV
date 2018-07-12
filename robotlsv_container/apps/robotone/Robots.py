import os
import threading

import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys


class RobotBase():
    def __init__(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        self.driver = WebDriver(executable_path=os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver'))

    def run(self, *args):
        pass

    def query(self):
        pass


class RobotElUniversal(RobotBase):
    def __init__(self, kwords, max_pagination=0):
        RobotBase.__init__(self)
        self.max_pagination = max_pagination
        self.kwords = kwords
        self.page = 0

    def run(self):
        news = []
        while self.page != self.max_pagination or self.max_pagination == 0:
            self.query()
            if len(self.driver.find_elements_by_class_name('pager')) == 0:
                break
            [news.append([new.text, new.find_element_by_tag_name('a').get_attribute('href'), 'El Universal'])
             for new in self.driver.find_elements_by_class_name('title') if new.text != "SITE"]
        self.driver.quit()
        return news

    def query(self):
        url = "http://www.eluniversal.com.co/search/site/" + self.kwords + "?page=" + str(self.page)
        self.driver.get(url)
        self.page += 1


class RobotElTiempo(RobotBase):
    def __init__(self, kwords, max_pagination=0):
        self.page = 1
        self.max_pagination = max_pagination + 1
        self.kwords = kwords
        self.browser = 3
        self.goon = True

    def run(self):
        news = []
        threads = []
        if self.max_pagination-1 < self.browser and self.max_pagination != 1:
            self.browser = self.max_pagination-1
        while (self.page < self.max_pagination or self.max_pagination == 1) and self.goon:
            for i in range(self.browser):
                # change to paginatesoup
                t = threading.Thread(target=self.paginate, args=(news,))
                threads.append(t)
                t.start()
                self.page += 1
            [thread.join() for thread in threads]
        return news

    def paginate(self, news):
        if self.page >= self.max_pagination and self.max_pagination != 1:
            self.goon = False
            return
        page = self.query()
        #Validate if wasn't found any pagination and no found results in the search
        if len(page.find_elements_by_class_name('pagination')) == 0 and len(page.find_elements_by_class_name('no-results')) == 1:
            self.goon = False
            return
        #Validate if search wasn't found
        search = page.find_elements_by_class_name('search-results-container')
        if len(search) == 0:
            self.goon = False
            return
        [news.append([new.text,
                      new.get_attribute('href'), 'El Tiempo']) for new in
         search[0].find_elements_by_class_name('title')]
        page.quit()
        return

    def query(self):
        from selenium.webdriver.chrome.webdriver import WebDriver
        url = 'http://www.eltiempo.com/buscar/' + str(self.page) + '?q=' + self.kwords
        driver = WebDriver(executable_path=os.path.join(os.path.dirname(__file__), 'driver', 'chromedriver'))
        driver.get(url)
        return driver
        # Paginate for Beautiful Soup

    def paginatesoup(self, news):
        if self.page >= self.max_pagination and self.max_pagination != 1:
            self.goon = False
            return
        page = self.querysoup()
        if len(page.find_all('div', class_='pagination')) == 0 and len(page.find_all('div', class_='no-results')) == 1:
            self.goon = False
            return
        #Validate if search wasn't found
        search = page.find('div', class_='search-results-container')
        if search is None:
            self.goon = False
            return
        [news.append([(new.text.replace('\n', '')).strip(),
                      'http://eltiempo.com' + str(new.attrs['href']), 'El tiempo']) for new in
         search.find_all('a', class_='title')]
        return

    def querysoup(self):
        url = 'http://www.eltiempo.com/buscar/' + str(self.page) + '?q=' + self.kwords
        soup = BeautifulSoup(requests.get(url).text, "html.parser")
        return soup

    # def run(self):
    #     news = []
    #     while self.page != self.max_pagination or self.max_pagination == 1:
    #         self.query()
    #         if len(self.driver.find_elements_by_class_name('pagination')) == 0:
    #             break
    #         [news.append([new.text, new.get_attribute('href')]) for new in
    #          self.driver.find_elements_by_class_name('title') if new.text != ""]
    #     self.driver.quit()
    #     return news


class RobotGoogle(RobotBase):
    def run(self, *args):
        kwords = [word + " " for word in args]
        self.driver.get('http://www.google.com/')
        self.driver.find_element_by_name('q').send_keys(kwords, Keys.RETURN)
        self.driver.quit()