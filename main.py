from selenium import webdriver
from time import sleep
from secret import get_account
from target import get_target_account

USERNAME, PASSWORD = get_account()
TARGET_ACCOUNT = get_target_account()

SCROLL_PAGE = 1
BASE_URL = 'https://instagram.com'

class InstagramBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.driver.get(BASE_URL)
        sleep(2)
        self.driver.find_element_by_xpath('//input[@name=\"username\"]')\
            .send_keys(self.username)
        self.driver.find_element_by_xpath('//input[@name=\"password\"]')\
            .send_keys(self.password)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), '稍後再說')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), '稍後再說')]")\
            .click()
        sleep(4)
    
    def go_target(self):
        self.driver.get(f'https://instagram.com/{TARGET_ACCOUNT}')
        sleep(2)

    def browse(self):
        pic_hrefs = []
        for _ in range(SCROLL_PAGE):
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                hrefs_in_view = [
                    elem.get_attribute('href')
                    for elem in hrefs_in_view
                    if '.com/p/' in elem.get_attribute('href')
                ]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                sleep(3)
            except Exception:
                continue
        return pic_hrefs

    def like_pics(self, pic_hrefs):
        for pic_href in pic_hrefs:
            try:
                self.driver.get(pic_href)
                self.like_pic()
            except Exception:
                continue
    
    def like_pic(self): 
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span')\
            .click()
        sleep(2)

def main():
    inst_bot = InstagramBot(USERNAME, PASSWORD)
    inst_bot.login()
    inst_bot.go_target()
    pics = inst_bot.browse()
    inst_bot.like_pics(pics)
    print('---end---')

if __name__ == "__main__":
    main()