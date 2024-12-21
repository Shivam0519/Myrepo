import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

# Setup the driver with options
@pytest.fixture(scope="module")
def driver():
    # Create Edge driver without specifying path, assuming it's in your PATH environment variable
    driver = webdriver.Edge()  # Use webdriver.Edge() for Edge
    driver.get("file:///C:/Users/ssing397/OneDrive%20-%20Capgemini/Desktop/index.html")  # Update with your file or URL
    yield driver
    driver.implicitly_wait(10)


# Test 1: Check page title
def test_check_title(driver):
    try:
        WebDriverWait(driver, 10).until(EC.title_is("Login System"))
        print(f"Page title: {driver.title}")
        assert driver.title == "Login System"
        print("Title found correctly")
    except TimeoutException:
        pytest.fail("Test failed: Page title is incorrect or took too long to load.")


# Test 2: Login with correct credentials

def test_login_check(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("jane")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(5)
        driver.refresh()  # Simulate a page reload after login
    except TimeoutException:
        pytest.fail("Test failed: Dashboard title not found within the timeout period.")
    except ElementNotInteractableException:
        pytest.fail("Test failed: Element not interactable during login process.")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")


# Test 3: Login with incorrect credentials
def test_wrong_login_check(driver):
    try:
        driver.find_element(By.ID, "username").send_keys("shivam")
        driver.find_element(By.ID, "password").send_keys("hello123")
        driver.find_element(By.XPATH, "/html/body/div[1]/form/button").click()
        time.sleep(2)
        driver.refresh()

    except TimeoutException:
        pytest.fail("Test failed: No alert shown for incorrect login.")
    except ElementNotInteractableException:
        pytest.fail("Test failed: Element not interactable during incorrect login.")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")


# Test 4: User registration process
def test_register_user(driver):
    try:
        driver.find_element(By.ID, "createAccountLink").click()

        # Wait for the registration form to appear
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "new-username")))

        # Fill in the registration details
        driver.find_element(By.ID, "new-username").send_keys("shivam")
        driver.find_element(By.ID, "new-password").send_keys("hello123")
        driver.find_element(By.ID, "re-enter-password").send_keys("hello123")
        driver.find_element(By.ID, "email").send_keys("shv38@g.com")
        driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
        time.sleep(1)
        # Handle the alert after registration
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        print("The user is registered successfully")

    except TimeoutException:
        pytest.fail("Test failed: Timeout while waiting for registration page or alert.")
    except ElementNotInteractableException:
        pytest.fail("Test failed: Element not interactable during registration process.")
    except Exception as e:
        pytest.fail(f"Test failed: {str(e)}")

