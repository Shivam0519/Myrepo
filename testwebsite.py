import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode for CI/CD pipelines
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Create Chrome driver
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:8081")
    yield driver
    driver.quit()

def test_check_title(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_is("Login System"))
        assert driver.title == "Login System"
    except TimeoutException:
        pytest.fail("Test failed: Page title is incorrect or took too long to load.")

def test_login_check(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("jane")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(5)
        driver.refresh()
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")

def test_wrong_login_check(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("shivam")
        driver.find_element(By.ID, "password").send_keys("hello123")
        driver.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(2)
        driver.refresh()
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")

def test_register_user(driver):
    try:
        driver.find_element(By.ID, "createAccountLink").click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "new-username")))
        driver.find_element(By.ID, "new-username").send_keys("shivam")
        driver.find_element(By.ID, "new-password").send_keys("hello123")
        driver.find_element(By.ID, "re-enter-password").send_keys("hello123")
        driver.find_element(By.ID, "email").send_keys("shv38@g.com")
        driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
        time.sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")
