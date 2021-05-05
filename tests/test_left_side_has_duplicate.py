from pages.game import Game

import pytest


# @pytest.mark.skip()
def test_left_side_has_duplicates(browser):
    GAME = Game(browser)
    GAME.load()
    GAME.fill_board("022", "345", 3)
    GAME.click_weigh(wait_for="alert")
    assert GAME.check_alert() == "Inputs are invalid: Left side has duplicates"