# ② Third-party Library
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def go_to_inbox(driver: WebDriver) -> WebDriver:

    """수신접수함 메뉴로 이동"""

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "admin_ic08"))).click()
    driver.switch_to.window(driver.window_handles[-1])

    return driver
