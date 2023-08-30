import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from web_scraper.custom_logger import CustomLogger


class Scraper:
    logger = CustomLogger()

    @classmethod
    def _click_show_more_button(cls, driver):
        while True:
            try:
                show_more_button = driver.find_element(By.ID, "showMoreResult")
                show_more_button.click()
                cls.logger.info("Clicking on 'Ver más' button until it disappears...")
                time.sleep(2)
                break
            except Exception as e:
                if e.__class__.__name__ == "ElementNotInteractableException":
                    break
                raise e

    @classmethod
    def scrape_page(cls, year="2023"):
        # Create a new instance of the Chrome driver (you can replace this with Firefox or other browsers)
        chrome_options = Options()
        service = Service(executable_path="./drivers/chromedriver")
        # get driver from drivers path
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument(
            "--disable-gpu"
        )  # Disable GPU acceleration in headless mode
        driver = webdriver.Chrome(service=service, options=chrome_options) 

        # Navigate to the website
        url = "https://votaciones.hcdn.gob.ar/"
        driver.get(url)
        cls.logger.info(f"Navigating to {url}...")
        time.sleep(3)

        try:
            # Click the dropdown button
            dropdown_button = driver.find_element(
                By.CSS_SELECTOR, "button[data-id='select-ano']"
            )
            dropdown_button.click()
            # Choose a specific year from the dropdown menu
            year_option = driver.find_element(
                By.XPATH, f"//ul[contains(@class, 'inner')]//span[text()='{year}']"
            )
            year_option.click()
            cls.logger.info(f"Selecting year {year}...")
            time.sleep(3)

            # Click the "Ver más" button until it disappears
            cls._click_show_more_button(driver)

            ver_expedientes_buttons = driver.find_elements(
                By.XPATH, "//a[text()='Ver expedientes']"
            )
            cls.logger.info(f"Retrieved {len(ver_expedientes_buttons)} buttons...")
            for button in ver_expedientes_buttons:
                while True:
                    try:
                        button.click()
                        break
                    except Exception as e:
                        if e.__class__.__name__ == "ElementNotInteractableException":
                            cls._click_show_more_button(driver)
                            continue
                        raise e
                time.sleep(1)
            cls.logger.info("Returning info...")
            return driver.page_source

        finally:
            # Close the browser window
            driver.quit()
