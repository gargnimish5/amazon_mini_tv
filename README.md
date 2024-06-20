# Amazon MiniTV Series Playback Automation

This project automates the playback of a series on Amazon MiniTV using Python, Appium, and pytest. The automation includes navigating the Amazon app, searching for a series, verifying its description, and playing the first episode of each season.

## Directory Structure

amazon_minitv_test/
|
│
├── pages/
│ ├── init.py
│ ├── base_page.py
│ ├── home_page.py
│ ├── search_page.py
│ └── series_page.py
│
├── tests/
│ ├── init.py
| ├── conftest.py
│ └── test_minitv_playback.py
│
├── config/
│ └── properties.py
│
└── pytest.ini


# Project Structure Explanation

# Pages
base_page.py: Contains the BasePage class with common methods for interacting with web elements.
home_page.py: Contains the HomePage class with methods to verify the home page.
search_page.py: Contains the SearchPage class with methods to search for a series and verify its description.
series_page.py: Contains the SeriesPage class with methods to interact with the series details page and play episodes.

# Tests
test_minitv_playback.py: Contains the test cases for verifying home page display, searching for a series, and playing the first episode of each season.
conftest.py: Contains pytest fixtures for setting up and tearing down the WebDriver.

# Config
properties.py: Contains configuration details such as desired capabilities and the series name.

# pytest.ini
Contains pytest configuration for generating HTML reports.

# Notes
Ensure that the Amazon app is installed and configured on your device/emulator.
Make sure Appium server is running before executing the tests.
Modify the properties.py file to include the correct desired capabilities for your setup.
And also update the xpath and id according to the app.
