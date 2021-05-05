"""
This module contains the Game for the game.
the page object for the Game.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

import random


class Game:

    # App URL
    
    URL = 'http://ec2-54-208-152-154.compute-1.amazonaws.com/'

    # Locators
    
    LEFT_0 = (By.ID, 'left_0')
    LEFT_1 = (By.ID, 'left_1')
    LEFT_2 = (By.ID, 'left_2')
    LEFT_3 = (By.ID, 'left_3')
    LEFT_4 = (By.ID, 'left_4')
    LEFT_5 = (By.ID, 'left_5')
    LEFT_6 = (By.ID, 'left_6')
    LEFT_7 = (By.ID, 'left_7')
    LEFT_8 = (By.ID, 'left_8')

    RIGHT_0 = (By.ID, 'right_0')
    RIGHT_1 = (By.ID, 'right_1')
    RIGHT_2 = (By.ID, 'right_2')
    RIGHT_3 = (By.ID, 'right_3')
    RIGHT_4 = (By.ID, 'right_4')
    RIGHT_5 = (By.ID, 'right_5')
    RIGHT_6 = (By.ID, 'right_6')
    RIGHT_7 = (By.ID, 'right_7')
    RIGHT_8 = (By.ID, 'right_8')

    # TODO Duplicate id/css is set for RESULT and RESET Buttons. Requires change from the dev folks
    RESULT_BUTTON = (By.XPATH, '/html/body/div/div/div[1]/div[2]/button')
    RESET_BUTTON = (By.XPATH, '/html/body/div/div/div[1]/div[4]/button[1]')
    WEIGHT_BUTTON = (By.ID, 'weigh')
    WEIGHING = (By.CLASS_NAME, 'game-info')

    COIN_0 = (By.ID, 'coin_0')
    COIN_1 = (By.ID, 'coin_1')
    COIN_2 = (By.ID, 'coin_2')
    COIN_3 = (By.ID, 'coin_3')
    COIN_4 = (By.ID, 'coin_4')
    COIN_5 = (By.ID, 'coin_5')
    COIN_6 = (By.ID, 'coin_6')
    COIN_7 = (By.ID, 'coin_7')
    COIN_8 = (By.ID, 'coin_8')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    """
    Fills out the game board
    accepts input:
    returns: 
    """
    def fill_board(self, left_input, right_input, seed=1):
        left_cells = ["LEFT_{}".format(_) for _ in sorted(random.sample(range(0, 9), seed))]
        right_cells = ["RIGHT_{}".format(_) for _ in sorted(random.sample(range(0, 9), seed))]
        for _ in range(seed):
            self.browser.find_element(*getattr(self, left_cells[_])).send_keys(left_input[_])
            self.browser.find_element(*getattr(self, right_cells[_])).send_keys(right_input[_])

    # for troubleshooting purpose
    def single_cell_fill(self):
        self.browser.find_element(*getattr(self, "LEFT_0")).send_keys("2")

    # click_weigh and click_reset can be combined into one method,
    # however, that would convolute readability
    """
    clicks on the Weigh button
    """
    def click_weigh(self, wait_for="result_button"):
        result_button = self.browser.find_element(*self.WEIGHT_BUTTON)
        self._highlight(result_button)
        result_button.click()
        wait = WebDriverWait(self.browser, 10)
        if wait_for == "result_button":
            wait.until_not(
                EC.text_to_be_present_in_element(self.RESULT_BUTTON, '?'))
        else:
            wait.until(EC.alert_is_present())
    """
    Performs click on the reset button
    """
    def click_reset(self):
        reset_button = self.browser.find_element(*self.RESET_BUTTON)
        self._highlight(reset_button)
        reset_button.click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(
            EC.text_to_be_present_in_element(self.RESULT_BUTTON, "?"))
    """
    only reads the value on the result button
    """
    def read_result(self):
        return self.browser.find_element(*self.RESULT_BUTTON).text

    """
    grabs the steps with weighing results
    """
    def read_weighings(self):
        return self.browser.find_element(By.CSS_SELECTOR, "#root > div > div.game > div.game-info > ol").text

    """
    clicks on coins below the game board
    returns the alert text as well
    """
    # TODO Move grabbing the alert text to a seperate method
    def click_on_coin(self, coin):
        ele = self.browser.find_element(*getattr(self, coin))
        self._highlight(ele)
        ele.click()
        alert = self.browser.switch_to.alert
        alert_txt = alert.text
        alert.accept()
        return alert_txt

    """
    returns title"""
    def title(self):
        return self.browser.title

    """
    waits until an alert is found and grabs the alert text
    """
    def check_alert(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        alert.accept()
        print(alert_text)
        return alert_text.rstrip()

    """
    highlights an element being interacted with, thereby making it easier to see what's happenig. 
    Only for manual execution. 
    """
    def _highlight(self, element):
        driver = element._parent
        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)
        original_style = element.get_attribute('style')
        apply_style("background: yellow; border: 2px solid red;")
        # Un-comment the below line to to enjoy _highlights in action.
        # sleep(.3)
        apply_style(original_style)

    """
    returns individual value of the given cell
    """
    def _get_cell_value(self, locator_string):
        return self.browser.find_element(*getattr(self, locator_string)).get_attribute("value").rstrip()

    """
    Verifies if the cells on the game board are empty
    """
    def is_game_board_reset(self):
        for i in range(9):
            if self._get_cell_value("LEFT_{}".format(i)) != "" \
                and self._get_cell_value("RIGHT_{}".format(i)) != "":
                return False
        return True



