# Automated WhatsApp Response System

This Python script is designed to automate responses on WhatsApp based on received messages. It uses PyAutoGUI for GUI automation, Selenium for web scraping, and Pyperclip for clipboard operations.

## Requirements

- Python 3.x
- PyAutoGUI
- Pyperclip
- Selenium
- Chrome WebDriver

## Installation

1. Install Python from [python.org](https://www.python.org/downloads/).
2. Install required Python packages:


3. Download Chrome WebDriver from [ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your system PATH or provide the path to it in the script.

## Usage

1. Ensure that Google Chrome is installed and logged into WhatsApp Web.
2. Run the script.
3. Keep WhatsApp Web open and wait for messages.
4. Messages containing specific patterns will trigger automated responses. Currently supported patterns are for canceling or refilling orders.
5. The script will process incoming messages, extract relevant information, and perform actions accordingly.

## Configuration

- Update the paths to image files used for locating elements on the screen (e.g., "smiley.png", "circle.png") if needed.
- Set up the path to the existing user data directory of Google Chrome for Selenium WebDriver (`user-data-dir` argument in `chrome_options`).

## Important Notes

- Ensure that Chrome WebDriver is compatible with the version of Chrome installed on your system.
- Adjust the confidence levels in PyAutoGUI's `locateOnScreen` function calls as needed to accurately locate elements on the screen.
- Make sure that your system is set up to handle the interactions and that the script operates correctly before leaving it unattended.
- Handle exceptions and errors gracefully to prevent unexpected behavior.

## Credits

- This script was developed by [Abdul Hannan].


