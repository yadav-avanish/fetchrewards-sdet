from pages.game import Game

import pytest



"""
Validates the alert for duplicate values in the right bowl
"""
# @pytest.mark.skip()
def test_right_side_has_duplicates(browser):
    GAME = Game(browser)
    GAME.load()
    GAME.fill_board("9876", "3442", 4)
    GAME.click_weigh(wait_for="alert")
    assert GAME.check_alert() == "Inputs are invalid: Right side has duplicates"
