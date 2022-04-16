import allure
from core import config
import time


class CheckPoint():

    def __init__(self):
        self.flag = 0

    @allure.step
    def equal(self, a, b):
        try:
            assert a == b

        except AssertionError:
            self.take_screenshot()
            print(f'the assertion fails，The expected result is【a=b】，actual result a={a}, b={b}')
            self.flag += 1

    @allure.step
    def not_null(self, a):
        try:
            assert a
        except AssertionError:
            self.take_screenshot()
            print(f'the assertion fails，The expected result is【a is not null】, actual result：a={a}')
            self.flag += 1

    @allure.step
    def list_not_empty(self, a):

        for i in a:
            try:
                self.not_null(i)
                self.take_screenshot()
            except AssertionError:
                self.take_screenshot()
                print(f'the assertion fails，The expected result is【list not null】, actual result：{a}')
                self.flag += 1

    @allure.step
    def more_than(self, a, b):
        try:
            assert a > b

        except AssertionError:
            self.take_screenshot()
            print(f'the assertion fails，The expected result is【a>b】，actual result a={a}, b={b}')
            self.flag += 1

    @allure.step
    def title_contains_words(self, title, l):
        try:
            for i in l:
                if i in title.lower():
                    print(f"{title.lower()} contains {i.lower()}")
                    self.take_screenshot()
                    return True
            else:
                self.flag += 1
                self.take_screenshot()
        except AssertionError:
            self.take_screenshot()
            print(f'The assertion fails，The expected result is【s contains any item of a】，actual result s={s}, a={a}')
            self.flag += 1

    @allure.step
    def take_screenshot(self, test="Screenshot"):
        tmp = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        config.DIRVER.save_screenshot(
            "/Users/cathy/Documents/Gitrep/google_search_UI_automation/screenshots/" + tmp + ".png")
        img = config.DIRVER.get_screenshot_as_base64()
        allure.attach(f"<img src='data:image/png;base64,{img}'/>", test, allure.attachment_type.HTML)

    @allure.step
    def result(self):
        if self.flag > 0:
            assert False, "checkpoint Failed！"
