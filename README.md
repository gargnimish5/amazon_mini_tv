# Amazon MiniTV Series Playback Automation

This project automates the playback of a series on Amazon MiniTV using Python, Appium, and pytest. The automation includes navigating the Amazon app, searching for a series, verifying its description, and playing the first episode of each season.

## Directory Structure

amazon_minitv_test/<br/> 
|<br/>
│<br/>
├── pages/<br/>
│ ├── init.py<br/>
│ ├── base_page.py<br/>
│ ├── home_page.py<br/>
│ ├── search_page.py<br/>
│ └── series_page.py<br/>
│<br/>
├── tests/<br/>
│ ├── init.py<br/>
| ├── conftest.py<br/>
│ └── test_minitv_playback.py<br/>
│<br/>
├── config/<br/>
│ └── properties.py<br/>
│<br/>
└── pytest.ini<br/>


# Project Structure Explanation

# Pages
base_page.py: Contains the BasePage class with common methods for interacting with web elements.<br/>
home_page.py: Contains the HomePage class with methods to verify the home page.<br/>
search_page.py: Contains the SearchPage class with methods to search for a series and verify its description.<br/>
series_page.py: Contains the SeriesPage class with methods to interact with the series details page and play episodes.<br/>

# Tests
test_minitv_playback.py: Contains the test cases for verifying home page display, searching for a series, and playing the first episode of each season.<br/>
conftest.py: Contains pytest fixtures for setting up and tearing down the WebDriver.<br/>

# Config
properties.py: Contains configuration details such as desired capabilities and the series name.<br/>

# pytest.ini
Contains pytest configuration for generating HTML reports.<br/>

# Notes
Ensure that the Amazon app is installed and configured on your device/emulator.<br/>
Make sure Appium server is running before executing the tests.<br/>
Modify the properties.py file to include the correct desired capabilities for your setup.<br/>
And also update the xpath and id according to the app.<br/>
