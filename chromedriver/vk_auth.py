from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from params import login, password
import os



cur_directory = os.getcwd()

options = webdriver.ChromeOptions()

options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     f"Chrome/112.0.0.0 Safari/537.36")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(f"user-data-dir={cur_directory}/user")
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(
    executable_path=f"{cur_directory}/chromedriver.exe",
    options=options
)

try:
    driver.implicitly_wait(10)
    driver.get(url="https://vk.com")
    time.sleep(10)
    email_input = driver.find_element(By.ID,"index_email")
    email_input.clear()
    email_input.send_keys(login)
    email_input.send_keys(Keys.ENTER)
    driver.find_element(By.CLASS_NAME, "vkc__Bottom__switchToPassword").click()
    pass_input = driver.find_element(By.NAME,"password")
    ActionChains(driver).move_to_element(pass_input).click(pass_input).perform()
    pass_input.clear()
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.ENTER)
    time.sleep(15)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

