import os
import sys
from selene.support.shared import browser
from selenium.webdriver import Keys


def select_gender_male():
    gender_male = browser.element("#gender-radio-1").double_click()
    gender_male.double_click()


def select_date_of_birthday():
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").type("April")
    browser.element(".react-datepicker__year-select").type("1993")
    browser.element("[aria-label='Choose Monday, April 19th, 1993']").click()


def fill_date_of_birthday(date):
    name_os = sys.platform
    if name_os == 'darwin':
        browser.element("#dateOfBirthInput").send_keys(Keys.COMMAND + 'a').type(date).press_enter()
    else:
        browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL + 'a').type(date).press_enter()


def submit():
    browser.element('#submit').press_enter()


def select_hobby_music():
    browser.element("[for=hobbies-checkbox-3]").click()


def download_picture():
    # browser.element("#uploadPicture").send_keys(os.path.abspath("../images/meme.jpg"))
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'images/meme.jpg'))
    )


def select_state_and_city(state, city):
    state_ = browser.element("#react-select-3-input")
    state_.type(state).press_enter()
    city_ = browser.element("#react-select-4-input")
    city_.type(city).press_enter()