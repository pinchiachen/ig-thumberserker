from selenium import webdriver
from time import sleep
from secret import get_account
from target import get_target_account
from element import Element

USERNAME, PASSWORD = get_account()
TARGET_ACCOUNT = get_target_account()

BASE_URL = 'https://instagram.com'
SCROLL_PAGE = 2
IS_LIKE = False

class InstagramBot:
    def __init__(self, username, password, like = True):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password
        self.like = like

    def login(self):
        self.driver.get(BASE_URL)
        sleep(2)
        self.driver.find_element_by_xpath(Element.INPUT_USERNAME.value)\
            .send_keys(self.username)
        self.driver.find_element_by_xpath(Element.INPUT_PASSWORD.value)\
            .send_keys(self.password)
        self.driver.find_element_by_xpath(Element.BUTTON_SUBMIT.value)\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath(Element.BUTTON_NEXT_TIME.value)\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath(Element.BUTTON_NEXT_TIME.value)\
            .click()
        sleep(4)
    
    def go_target(self, url):
        self.driver.get(url)
        sleep(2)

    def browse(self):
        pic_hrefs = []
        hrefs_exist = dict()
        for _ in range(SCROLL_PAGE):
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                hrefs_in_view = [
                    elem.get_attribute('href')
                    for elem in hrefs_in_view
                    if '.com/p/' in elem.get_attribute('href')
                ]
                for href in hrefs_in_view:
                    if href not in hrefs_exist:
                        pic_hrefs.append(href)
                        hrefs_exist[href] = 1
                sleep(3)
            except Exception:
                continue
        return pic_hrefs

    def manipulate_pics(self, pic_hrefs):
        for pic_href in pic_hrefs:
            try:
                self.driver.get(pic_href)
                self.__like_pic() if self.like else self.__dislike_pic()
            except Exception:
                continue
    
    def __like_pic(self):
        self.driver.find_element_by_xpath(Element.BUTTON_LIKE.value)\
            .click()
        sleep(2)

    def __dislike_pic(self): 
        self.driver.find_element_by_xpath(Element.BUTTON_DISLIKE.value)\
            .click()
        sleep(2)

def main():
    inst_bot = InstagramBot(USERNAME, PASSWORD, IS_LIKE)
    inst_bot.login()
    target_url = f'{BASE_URL}/{TARGET_ACCOUNT}'
    inst_bot.go_target(target_url)
    pics = inst_bot.browse()
    inst_bot.manipulate_pics(pics)
    print('---end---')

if __name__ == "__main__":
    main()