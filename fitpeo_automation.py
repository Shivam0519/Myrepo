from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

def initialize_driver():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://fitpeo.com/")
        return driver
    except WebDriverException as e:
        print(f"Error initializing the WebDriver: {e}")
        raise

def click_element(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
    except NoSuchElementException:
        print(f"Element not found for XPath: {xpath}")
    except Exception as e:
        print(f"Error clicking element with XPath {xpath}: {e}")

def scroll_window(driver, x, y):
    try:
        driver.execute_script(f"window.scrollBy({x},{y});")
    except Exception as e:
        print(f"Error scrolling window: {e}")

def move_slider(driver, xpath, xoffset):
    try:
        slider = driver.find_element(By.XPATH, xpath)
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(xoffset=xoffset, yoffset=0).release().perform()
    except NoSuchElementException:
        print(f"Slider not found for XPath: {xpath}")
    except Exception as e:
        print(f"Error moving slider with XPath {xpath}: {e}")

def reset_slider(driver, slider_xpath, reset_xoffset):
    try:
        slider = driver.find_element(By.XPATH, slider_xpath)
        actions = ActionChains(driver)
        # Click and hold the slider
        actions.click_and_hold(slider)
        # Move the slider to the reset position
        actions.move_by_offset(xoffset=reset_xoffset, yoffset=0)
        # Release the slider
        actions.release().perform()
    except Exception as e:
        print(f"Error resetting slider: {e}")


def set_input_value(driver, element_id, value):
    try:
        input_field = driver.find_element(By.ID, element_id)
        input_field.clear()
        time.sleep(2)
        driver.execute_script(f"arguments[0].value = '{value}';", input_field)
    except NoSuchElementException:
        print(f"Input field not found with ID: {element_id}")
    except Exception as e:
        print(f"Error setting value for input field with ID {element_id}: {e}")

def main():
    driver = None
    try:
        driver = initialize_driver()
        time.sleep(3)

        click_element(driver, "/html/body/div[1]/div/header/div/div[3]/div[6]/a")
        time.sleep(3)

        scroll_window(driver, 0, 200)
        time.sleep(3)

        move_slider(driver, "/html/body/div[2]/div[1]/div[1]/div[2]/div/div/span[1]/span[3]", 94)
        time.sleep(5)

        set_input_value(driver, ":r0:", "560")
        time.sleep(3)

        click_element(driver, "/html/body/div[2]/div[1]/div[2]/div[1]/label/span[1]/input")
        scroll_window(driver, 0, 300)

        click_element(driver, "/html/body/div[2]/div[1]/div[2]/div[2]/label/span[1]/input")
        click_element(driver, "/html/body/div[2]/div[1]/div[2]/div[3]/label/span[1]/input")

        scroll_window(driver, 0, 50)
        click_element(driver, "/html/body/div[2]/div[1]/div[2]/div[8]/label/span[1]/input")

        time.sleep(5)
        set_input_value(driver, ":r0:", "820")
        time.sleep(30)

    except TimeoutException:
        print("Timeout occurred while waiting for elements.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
