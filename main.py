import time

import buttons
from settings import *
import button as button
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from buttons import *

driver = webdriver.Chrome()

# register

# driver.get('https://stepik.org/catalog?auth=registration')
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_full-name')]").send_keys('rick morty')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_email')]").send_keys('store2_korzinka@mail.ru')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_password')]").send_keys('isa2516530')
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/button").click()

#driver.quit()

#------------------------------- авторизация и выбор курса---------------------

driver.get('https://stepik.org/catalog?auth=login')
#driver.find_element(By.XPATH, "//input[contains(@id, 'id_login_email')]").send_keys('store2_korzinka@mail.ru')
driver.find_element(By.ID, login_email).send_keys(valid_mail)
driver.find_element(By.XPATH, login_password).send_keys(valid_password)
driver.find_element(By.XPATH, submit_btn).click()
time.sleep(3)
driver.get(course_link)
#driver.find_element(By.CSS_SELECTOR, '#ember106 > button').click()
time.sleep(10.0)
#driver.find_element(By.XPATH, continue_btn).click()
driver.find_element((By.XPATH, first_lesson)).click()





# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()