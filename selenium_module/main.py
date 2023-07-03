from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER)
    )

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options,
    )

    return chrome_browser


if __name__ == '__main__':
    # Exemple:
    # options = ('--headless', '--disable-gpu')
    # more Chrome Options:
    # https://peter.sh/experiments/chromium-command-line-switches/

    # Get browser
    options = ()
    browser = make_chrome_browser(*options)

    # Open google in browser
    browser.get('htpps://www.google.com.br/')

    # Sleep for 10 seconds
    time.sleep(10)
