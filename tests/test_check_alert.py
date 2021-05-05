from pages.game import Game

import pytest


# For troubleshooting/understadning the capfd workflow
# makes it to easy to debug by capturing from stdout
@pytest.mark.skip()
def test_check_alert(browser, capfd):
    GAME = Game(browser)
    GAME.load()
    GAME.fill_board("2", "2", 1)
    GAME.click_weigh(wait_for="alert")
    GAME.check_alert()

    out, err = capfd.readouterr()
    assert out == "Inputs are invalid: Both sides have coin(s): 2\n"
