from selenium import webdriver
# from core.config import DIRVER
import csv
from selenium.webdriver.support.select import Select
from core import config
from selenium.webdriver.chrome.options import Options


class Locator():

    def __init__(self):

        self.driver = webdriver.Chrome(
            executable_path="/Users/cathy/Documents/Gitrep/google_search_UI_automation/chromedriver")
        # chrome_option = Options()
        # chrome_option.add_argument('--headless')
        # chrome_option.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(
        #     executable_path="/Users/cathy/Documents/Gitrep/google_search_UI_automation/chromedriver",
        # chrome_options=chrome_option)
        config.DIRVER = self.driver

    def element(self, page, name):
        # 通过page和name，找到key和value
        with open("./data/objectlib.csv", "r", encoding="utf-8") as f:
            for i in csv.reader(f):
                if page == i[0] and name == i[1]:
                    key = i[2]
                    value = i[3]
                    break
            else:
                raise Exception(f"object is not defined in the objctlib:{page} and {name}")

        if key == "id":
            try:
                return self.driver.find_element_by_id(value)
            except:
                raise Exception(f"The specified element was not found：by {key}, {value}")

        elif key == "name":
            try:
                return self.driver.find_element_by_name(value)
            except:
                raise Exception(f"The specified element was not found：by {key}, {value}")

        elif key == "class":
            try:
                return self.driver.find_element_by_class_name(value)
            except:
                raise Exception(f"The specified element was not found, Location info：by {key}, {value}")

        elif key == "xpath":
            try:
                return self.driver.find_element_by_xpath(value)
            except:
                raise Exception(f"The specified element was not found, Location info：by {key}, {value}")
        elif key == "link_text":
            try:
                return self.driver.find_element_by_class_name(value)
            except:
                raise Exception(f"The specified element was not found, Location info：by {key}, {value}")
        elif key == "tag":
            try:
                return self.driver.find_element_by_tag_name(value)
            except:
                raise Exception(f"The specified element was not found, Location info：by {key}, {value}")

    def elements(self, page, name):
        with open("./data/objectlib.csv", "r", encoding="utf-8") as f:
            for i in csv.reader(f):
                if page == i[0] and name == i[1]:
                    key = i[2]
                    value = i[3]
                    break
            else:
                raise Exception(f"object is not defined in the objctlib:{page}{name}")
        if key == "class":
            return self.driver.find_elements_by_class_name(value)
        elif key == "xpath":
            return self.driver.find_elements_by_xpath(value)

    def click(self, page, name):
        self.element(page, name).click()

    def send_keys(self, page, name, text):
        self.element(page, name).send_keys(text)

    def get_text_value(self, page, name):
        return self.element(page, name).text

    def get_multiple_strs(self, page, name):
        elements_list = self.elements(page, name)
        texts_list = []
        for e in elements_list:
            texts_list.append(e.text[1:-3])

        return texts_list

    def go_to(self, url):
        self.driver.get(url)

    def get_current_title(self):
        title_name  = self.driver.title
        return title_name

    def switch_to_frame(self, i):
        self.driver.switch_to.frame(i)

    @property
    def close(self):
        self.driver.close()

    @property
    def maximize_the_window(self):
        self.driver.maximize_window()

    def wait(self, s):
        self.driver.implicitly_wait(s)

    def select_by_index(self, page, name, i):
        Select(self.element(page, name)).select_by_index(i)
