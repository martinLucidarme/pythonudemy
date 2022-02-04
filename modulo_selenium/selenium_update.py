from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pathlib import Path
from time import sleep

# caminho para raiz do projeto
ROOT_FOLDER = Path(__file__).parent.parent.parent
# caminho para pasta do Chromedriver
CHROME_DRIVER_PATH = 'chromedriver'


def make_chrome_browser(*options: str):
    chrome_options = webdriver.ChromeOptions()

    if options:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(service=chrome_service,
                               options=chrome_options
                               )

    return browser


if __name__ == '__main__':
    ...
    options = ('--disable-gpu', '--no-sandbox',)
    browser1 = make_chrome_browser(*options)

    browser1.get('https://www.google.com')

    input_element = browser1.find_element(By.NAME, 'q')
    input_element.send_keys('Python')

    input_element.send_keys(Keys.ENTER)
    sleep(3)
    browser1.quit()
