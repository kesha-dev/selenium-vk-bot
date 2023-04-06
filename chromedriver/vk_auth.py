from selenium import webdriver
import time
from fake_useragent import UserAgent
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from params import login, password

options = webdriver.ChromeOptions()

userAgent = UserAgent()
options.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     f"Chrome/112.0.0.0 Safari/537.36")

driver = webdriver.Chrome(
    executable_path=r"C:\Users\user\PycharmProjects\pythonProject\chromedriver.exe",
    options=options
)

try:
    driver.implicitly_wait(10)
    driver.get(url="https://vk.com")
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

