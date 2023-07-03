from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

ROOT_FOLDER = Path(__file__).parent
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH)
    )

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return chrome_browser


if __name__ == '__main__':
    TIME_TO_WAIT = 5
    # Exemple:
    # options = ('--headless', '--disable-gpu')
    # more Chrome Options:
    # https://peter.sh/experiments/chromium-command-line-switches/

    # Get browser
    options = ()
    browser = make_chrome_browser(*options)

    # Open google in browser
    browser.get('https://www.google.com/')

    # wait to find input
    search_box = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_box.send_keys("One piece")
    search_box.send_keys(Keys.ENTER)

    # click on the first survey link
    # results = browser.find_element(By.ID, 'search')
    # links = results.find_elements(By.TAG_NAME, 'a')
    # links[0].click()

    # Open images
    tags_box = browser.find_element(By.CLASS_NAME, 'xhjkHe')
    search_types = tags_box.find_elements(By.TAG_NAME, 'a')
    search_types[0].click()

    # Sleep for 10 seconds
    time.sleep(TIME_TO_WAIT)
