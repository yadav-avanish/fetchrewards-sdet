from pages.game import Game

import pytest

"""
validates the alert produced if the user enters same input on
both the left and right bowls
"""
# @pytest.mark.skip()
def test_both_sides_have_duplicates(browser):
    GAME = Game(browser)
    GAME.load()
    GAME.fill_board("0754", "1294", 4)
    GAME.click_weigh(wait_for="alert")
    assert GAME.check_alert() == "Inputs are invalid: Both sides have coin(s): 4"



