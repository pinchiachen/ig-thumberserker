from enum import Enum

class Element(Enum):
    INPUT_USERNAME = '//input[@name=\"username\"]'
    INPUT_PASSWORD =  '//input[@name=\"password\"]'
    BUTTON_SUBMIT = '//button[@type="submit"]'
    BUTTON_NEXT_TIME = '//button[contains(text(), "稍後再說")]'
    BUTTON_LIKE = '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button/div/span'
