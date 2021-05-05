# Identify the **Fake Gold Bar** -- Excercise for the SDET role at Fetchrewards.

## Must Have's
    * Python 3.6+
    * PIP
    * Browsers: Chrome or Firefox


### Observations:
    * RESULT and RESET buttons have duplicate id's
    * Typo in success message. Should have been "Yay! You found it!"


## Setup
  To set up the Python environment and install dependencies, run:

      > pip install pipenv
      > pipenv install

  ### Running Tests
   To run tests, run the following command from the project's root directory:

      > pipenv run python -m pytest

    Note: To run tests on firefox, set the following property in config.json
    ` "browser" : "firefox" `
    Note: Only Chrome and Firefox are currently supported
