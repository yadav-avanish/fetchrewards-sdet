"""
This module contains the game play.
Tests use Selenium WebDriver
Fixtures set up and clean the WebDriver instance.
"""

import traceback
import pytest

from pages.game import Game

GAME = None
FAKE_BAR = None
WEIGHING_STEPS = ""

# @pytest.mark.skip()
@pytest.mark.dependency()
def test_fake_bar(browser):
    try:
        global GAME
        global FAKE_BAR
        global WEIGHING_STEPS

        GAME = Game(browser)
        GAME.load()

        GAME.fill_board("012", "345", 3)
        GAME.click_weigh()

        if GAME.read_result() == "=":
            GAME.click_reset()
            WEIGHING_STEPS += "[0,1,2] = [3,4,5]\n"
            GAME.fill_board("6", "7")
            GAME.click_weigh()
            result = GAME.read_result()

            if result == "=":
                FAKE_BAR = 8
                WEIGHING_STEPS += "[6] = [7]"
            elif result == "<":
                FAKE_BAR = 6
                WEIGHING_STEPS += "[6] < [7]"
            elif result == ">":
                FAKE_BAR = 7
                WEIGHING_STEPS += "[6] > [7]"
            else:
                print("Illegal result {} found. Error in the App.".format(GAME.read_result()))

        elif GAME.read_result() == "<":
            GAME.click_reset()
            WEIGHING_STEPS += "[0,1,2] < [3,4,5]\n"
            GAME.fill_board("0", "1")
            GAME.click_weigh()
            result = GAME.read_result()

            if result == ">":
                FAKE_BAR = 1
                WEIGHING_STEPS += "[0] > [1]"
            elif result == "<":
                FAKE_BAR = 0
                WEIGHING_STEPS += "[0] < [1]"
            elif result == "=":
                FAKE_BAR = 2
                WEIGHING_STEPS += "[0] = [1]"
            else:
                print("Illegal result {} found. Error in the App.".format(GAME.read_result()))

        elif GAME.read_result() == ">":
            GAME.click_reset()
            WEIGHING_STEPS += "[0,1,2] > [3,4,5]\n"
            GAME.fill_board("3", "4")
            GAME.click_weigh()
            result = GAME.read_result()

            if result == ">":
                FAKE_BAR = 4
                WEIGHING_STEPS += "[3] > [4]"
            elif result == "<":
                FAKE_BAR = 3
                WEIGHING_STEPS += "[3] < [4]"
            elif result == "=":
                FAKE_BAR = 5
                WEIGHING_STEPS += "[3] = [4]"
            else:
                print("Illegal result {} found. Error in the App.".format(GAME.read_result()))

        else:
            print("Illegal result {} found. Error in the App.".format(GAME.read_result()))
    except Exception as ex:
        print("Exception occured: \n", traceback.format_exc())
        raise ex

    assert GAME.title() == "React App"

# TODO Ask dev to change the sentence to "Yay! You found it!"
# @pytest.mark.skip()
@pytest.mark.dependency(depends=["test_fake_bar"])
def test_coin_selector():
    assert GAME.click_on_coin("COIN_{}".format(FAKE_BAR)) == "Yay! You find it!"

# @pytest.mark.skip()
@pytest.mark.dependency(depends=["test_fake_bar"])
def test_weighings():
    assert GAME.read_weighings() == WEIGHING_STEPS

# @pytest.mark.skip()
@pytest.mark.dependency(depends=["test_fake_bar"])
def test_try_again_popups():
    for i in range(8):
        if i != FAKE_BAR:
            assert GAME.click_on_coin("COIN_{}".format(i)) == "Oops! Try Again!"





