from enum import Enum

class Element(Enum):
    INPUT_USERNAME = '//input[@name=\"username\"]'
    INPUT_PASSWORD =  '//input[@name=\"password\"]'
    BUTTON_SUBMIT = '//button[@type="submit"]'
    BUTTON_NEXT_TIME = '//button[contains(text(), "稍後再說")]'
    BUTTON_LIKE = '//article//section//button//*[@aria-label="讚"]'
    BUTTON_DISLIKE = '//article//section//button//*[@aria-label="收回讚"]'
