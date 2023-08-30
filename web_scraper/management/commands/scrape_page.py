import time
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service

class Command(BaseCommand):
    help = "Deletes all folders from a given directory"

    def click_show_more_button(self, driver):
        while True:
            try:
                show_more_button = driver.find_element(By.ID, "showMoreResult")
                show_more_button.click()
                time.sleep(2)
                break
            except Exception as e:
                if e.__class__.__name__ == "ElementNotInteractableException":
                    break
                raise e

    def handle(self, *args, **options):
        # Create a new instance of the Chrome driver (you can replace this with Firefox or other browsers)
        service = Service(executable_path="./drivers/chromedriver")
        driver = webdriver.Chrome(service=service)  # Make sure you have the correct WebDriver executable path
        # Navigate to the website
        driver.get("https://votaciones.hcdn.gob.ar/")

        try:
            # Click the dropdown button
            time.sleep(3)
            dropdown_button = driver.find_element(
                By.CSS_SELECTOR, "button[data-id='select-ano']"
            )
            dropdown_button.click()
            # Choose a specific year from the dropdown menu
            year = "2001"
            year_option = driver.find_element(
                By.XPATH, f"//ul[contains(@class, 'inner')]//span[text()='{year}']"
            )
            year_option.click()
            time.sleep(3)

            # Click the "Ver más" button until it disappears
            self.click_show_more_button(driver)

            # Find all buttons with the text "Ver expedientes" and click on them
            ver_expedientes_buttons = driver.find_elements(
                By.XPATH, "//a[text()='Ver expedientes']"
            )
            for button in ver_expedientes_buttons:
                while True:
                    try:
                        button.click()
                        break
                    except Exception as e:
                        if e.__class__.__name__ == "ElementNotInteractableException":
                            self.click_show_more_button(driver)
                            continue
                        raise e
                time.sleep(1)
            import pdb

            pdb.set_trace()
            # Retrieve the resulting HTML content of the website
            result_html = driver.page_source

            # Print the HTML content or save it to a file as needed
            print(result_html)

        finally:
            # Close the browser window
            driver.quit()
