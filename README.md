# Identify the **Fake Gold Bar** -- Excercise for the SDET role at Fetchrewards.

## Must Have's
    * Python Preferably 3.7+
    * Pip
    * Browsers: Chrome or Firefox


### Observations:
    * RESULT and RESET buttons have duplicate id's
    * Typo in success message. Should have been "Yay! You found it!"


## Setup
     * git clone https://github.com/yadav-avanish/fetchrewards-sdet.git
     * cd <repo>
     * python setup.py install

## Running Tests
     * Run ``` pytest ``` from the project root.
     * To run Firefox, set the ``` "browser" : "firefox" ``` in config.json

    Note: Only supports Google Chrome and Firefox.
