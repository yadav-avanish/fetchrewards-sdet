##########
This repo solves the Fake Goladbar game for the SDET role at Fetchrewards.

Must Have's
    * Python 3.5+
    * PIP
    * Browsers: Firefox


#########

DEFECTS:
    * RESULT and RESET buttons have duplicate id's


TESTS:
    duplicate warning - same side and both sides
    similar single, double, all inputs on both sides
    YAY message
    Inject wrong input via JavaScript

  # Setup
  This project requires Python 3.

  To set up the Python environment and install dependencies, run:

      > pip install pipenv
      > pipenv install

  ## Running Tests
  You will need a CrossBrowserTesting license to run the tests in this project.
  You can obtain a trial license from https://crossbrowsertesting.com/.
  Add your username and authentication key to `cbt_config.json`.

  To run tests, run the following command from the project's root directory:

      > pipenv run python -m pytest

  The terminal will print the pytest banner.
  Be patient - tests may take a few seconds to complete.
  You can also check results on the CrossBrowserTesting website.
