from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()


wait = WebDriverWait(driver, 10)
el_switchto = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='header']/descendant::ul[1]/li[4]/a")))
el_switchtoWin = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='header']/descendant::ul[2]/li[2]/a")))

print(driver.title)
actions = ActionChains(driver)
actions.move_to_element(el_switchto).perform()
actions.move_to_element(el_switchtoWin).click().perform()

el_NewSepWin = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a")))
el_NewSepWin.click()

el_Clk = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='Seperate']/button")))
el_Clk.click()

home_windle = driver.current_window_handle
win_handels = driver.window_handles
for handle in win_handels:
    if handle != home_windle:
        driver.switch_to.window(handle)

el_Clk = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='navbar']/a[1]")))
el_Clk.click()
driver.quit()




# win_name = driver.title
# print(win_name)
# driver.switch_to.window(Frames & windows)
# print(driver.current_window_handle)
# el_SepWin = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Open New Seperate Windows')]")))
# actions.move_to_element(el_SepWin).click().perform()