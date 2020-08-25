from selenium import webdriver
from time import sleep
from secret import get_username, get_password, get_target_account

USERNAME = get_username()
PASSWORD = get_password()
TARGET_ACCOUNT = get_target_account()
SCROLL_PAGE = 1

class InstagramBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.username = username
        self.password = password

    def login(self):
        self.driver.get('https://instagram.com')
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

    def start(self):
        pic_hrefs = []
        for i in range(SCROLL_PAGE):
            try:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                hrefs_in_view = self.driver.find_elements_by_tag_name('a')
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view\
                                    if '.com/p/' in elem.get_attribute('href')]
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print(f'pic_hrefs is {pic_hrefs}')
                sleep(3)
            except Exception:
                continue
        
        for pic_href in pic_hrefs:
            try:
                self.driver.get(pic_href)
                self.like_pic()
            except Exception:
                continue
    
    def like_pic(self): 
        like = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span') 
        like.click()
        sleep(2) 

def main():
    inst_bot = InstagramBot(USERNAME, PASSWORD)
    inst_bot.login()
    inst_bot.go_target()
    inst_bot.start()
    print('---end---')

if __name__ == "__main__":
    main()