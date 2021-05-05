from pages.game import Game

import pytest


# @pytest.mark.skip()
def test_click_reset_button(browser):
    GAME = Game(browser)
    GAME.load()
    GAME.fill_board("012345678", "876543210", 9)
    GAME.click_reset()
    assert GAME.is_game_board_reset() == True
